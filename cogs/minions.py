import discord
from discord.ext import commands
from helpers.player import Player
from helpers.errors import *

class Minions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="minion", aliases=["minions"], 
        help=(
        "**stella minion [ign] [optional: profile]**\n"
        "Returns various stats related to minions for a player.\n"
        )
    )
    async def command_minions(self, ctx, name, *profile):
        if ctx.guild.id not in [604420816817356822, 606864572594257921]:
            await ctx.reply("This command is currently only available on the Skyborn Discord server for beta testing.")
            return
        print(f"{ctx.author.name} sent minions command in {ctx.guild}")
        try:
            if profile:
                user = Player(name,profile=profile[0])
            else:
                user = Player(name)
        except ProfileNotFound:
            await ctx.reply("ProfileNotFound Error")
            return
        except PlayerNotFound:
            await ctx.reply("PlayerNotFound Error")
            return

        # General embed for this command
        def get_embed(title, description=False):
            if description:
                embed = discord.Embed(title=title, description=f"`{user.name}` ~ `{user.fruit}`", color=0xdc6565)
            else:
                embed = discord.Embed(titel=title, color=0xdc6565)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{user.uuid}")
            embed.set_footer(text="Stella Bot by Over#6203\nClick on the reactions for other tabs.")

            return embed

        # Check for reaction menus
        def check(reaction, user):
            # Ensures that the reaction is from the author and on the output message
            return user == ctx.author and reaction.message.id == output.id
        

        # ------
        # Command Processing
        # ------
        speed = 0
        modifiers = ""

        # Asks the user for a minion item
        query_embed = get_embed("What Minion Item Will You Use?")
        query_embed.add_field(name="Note",value="It is assumed that one of your minion items will be a Dwarven Super Compactor 3000. \n<:diamond_spreading:837124543939346472> Diamond Spreading\n<:flycatcher:837124689176428605> Flycatcher\n🚫 No Minion Upgrade")
    
        
        output = await ctx.reply(embed=query_embed)
        await output.add_reaction("<:diamond_spreading:837124543939346472>")
        await output.add_reaction("<:flycatcher:837124689176428605>")
        await output.add_reaction("🚫")

 
        # Reaction menu for what item you added
        reaction = None
        while True:
            if str(reaction) == "<:diamond_spreading:837124543939346472>":
                user.modify_tiers_for_an_upgrade("DIAMOND", 0.1)
                modifiers += "<:diamond_spreading:837124543939346472> Diamond Spreading\n"
                break
            elif str(reaction) == "<:flycatcher:837124689176428605>":
                modifiers += "<:flycatcher:837124689176428605> Flycatcher\n"
                speed += 0.2
                break
            elif str(reaction) == "🚫":
                modifiers += "🚫 No Minion Upgrade\n"
                break

            try: # Timeout
                reaction, member = await self.bot.wait_for("reaction_add", timeout=45.0, check=check)
                await output.remove_reaction(reaction, member)
            except:
                await output.clear_reactions()
                await output.add_reaction("🛑")
                return

        await output.clear_reactions()

        # Fuel Question
        query_embed = get_embed("What Minion Fuel Will You Use?")
        
        query_embed.add_field(name="Minion Fuels",value="""
            <:enchanted_lava_bucket:838929144288772107> Enchanted Lava Bucket\n
            <:magma_bucket:838929187226124308> Magma Bucket\n
            <:plasma_bucket:838929230229536788> Plasma Bucket\n
            <:foul_flesh:838930441728950314> Foul Flesh\n
            <:hamster_wheel:838930233955975168> Hamster Wheel\n
            <:catalyst:838931725680640110> Catalyst\n
            <:hyper_catalyst:838931725752074250> Hyper Catalyst\n
            🚫 No Minion Fuel\n
            """)
    
        await output.edit(embed=query_embed)
        await output.add_reaction("<:enchanted_lava_bucket:838929144288772107>")
        await output.add_reaction("<:magma_bucket:838929187226124308>")
        await output.add_reaction("<:plasma_bucket:838929230229536788>")
        await output.add_reaction("<:foul_flesh:838930441728950314>")
        await output.add_reaction("<:hamster_wheel:838930233955975168>")
        await output.add_reaction("<:catalyst:838931725680640110>")
        await output.add_reaction("<:hyper_catalyst:838931725752074250>")
        await output.add_reaction("🚫")
        
        # Reaction menu for what item you added
        reaction = None
        while True:
            if str(reaction) == "<:enchanted_lava_bucket:838929144288772107>":
                speed += 0.25
                modifiers += "<:enchanted_lava_bucket:838929144288772107> Enchanted Lava Bucket\n"
                break
            elif str(reaction) == "<:magma_bucket:838929187226124308>":
                modifiers += "<:magma_bucket:838929187226124308> Magma Bucket\n"
                speed += 0.30
                break
            elif str(reaction) == "<:plasma_bucket:838929230229536788>":
                modifiers += "<:plasma_bucket:838929230229536788> Plasma Bucket\n"
                speed+= 0.35
                break
            elif str(reaction) == "<:foul_flesh:838930441728950314>":
                modifiers += "<:foul_flesh:838930441728950314> Foul Flesh\n"
                speed += 0.9
                break
            elif str(reaction) == "<:hamster_wheel:838930233955975168>":
                modifiers += "<:hamster_wheel:838930233955975168> Hamster Wheel\n"
                speed += 0.5
                break
            elif str(reaction) == "<:catalyst:838931725680640110>":
                modifiers += "<:catalyst:838931725680640110> Catalyst\n"
                user.modify_tiers_for_yield_changes(rate=3)
                break
            elif str(reaction) == "<:hyper_catalyst:838931725752074250>":
                modifiers += "<:hyper_catalyst:838931725752074250> Hyper Catalyst\n"
                user.modify_tiers_for_yield_changes(rate=4)
                break
            elif str(reaction) == "🚫":
                modifiers += "🚫 No Minion Fuel\n"
                break

            try: # Timeout
                reaction, member = await self.bot.wait_for("reaction_add", timeout=45.0, check=check)
                await output.remove_reaction(reaction, member)
            except:
                await output.clear_reactions()
                await output.add_reaction("🛑")
                return

        await output.clear_reactions()

        embed_list = []
        # Main embed with upgrade costs
        main_embed = get_embed("Minions", description=True)
        main_embed.add_field(name="Minion Slots", value=f"**{user.unlocks}**")
        main_embed.add_field(name="Unique Unlocks", value=f"**{user.unique_minion_count}**")
        upgrade_message = []
        for entry in user.upgrade_costs:
            if len(upgrade_message) > 8:
                break
            else:
                count = max(user.constants[entry[0]]['list'])
                upgrade_message.append(f"**{entry[0]}** ({count} --> {count+1}): **{'{:,}'.format(entry[1])}**")

        main_embed.add_field(name="Cheapest Upgrades", value="\n".join(upgrade_message),inline=False)

        # Profits Page
        user.get_yield_per_hour(modifier=speed)

        profit_embed = get_embed("Minions Profits", description=True)
        profit_message = []
        including_slots_message = []
        for entry in user.minion_profits:
            if len(profit_message) > 10:
                break
            else:
                profit_message.append(f"**{entry[0]} {max(user.constants[entry[0]]['list'])}** : **{'{:,}'.format(round(entry[1]))}**")
                including_slots_message.append(f"**{entry[0]} {max(user.constants[entry[0]]['list'])}** : **{'{:,}'.format(round(entry[1] * user.unlocks))}**")
        profit_embed.add_field(name="Modifiers", value=modifiers, inline=False)
        profit_embed.add_field(name="Highest Profits Per Hour (Single Minion)",value="\n".join(profit_message))
        profit_embed.add_field(name=f"Highest Profits Per Hour ({user.unlocks} Minions)",value="\n".join(including_slots_message))
        
        # Stats for top earner minions
        top_minions = get_embed("Minion Profits", description=True)
        top_minions.add_field(name="Modifiers", value=modifiers, inline=False)
        index = 0
        for entry in user.minion_profits:
            if index == 0:
                minion = entry
            elif index == 1:
                minion_2 = entry
            elif index == 2:
                minion_3 = entry
            else:
                break
            index += 1
        
        top_minions.add_field(name=f"**{minion[0]}** {max(user.constants[minion[0]]['list'])}", value=f"Per Hour Yield In Items (1 Minion)\n {user.get_yield_per_hour_minion(minion[0])}",inline=False)
        top_minions.add_field(name=f"**{minion_2[0]}** {max(user.constants[minion_2[0]]['list'])}", value=f"Per Hour Yield In Items (1 Minion)\n {user.get_yield_per_hour_minion(minion_2[0])}",inline=False)
        top_minions.add_field(name=f"**{minion_3[0]}** {max(user.constants[minion_3[0]]['list'])}", value=f"Per Hour Yield In Items (1 Minion)\n {user.get_yield_per_hour_minion(minion_3[0])}",inline=False)
    
        # Finalizes the embed list
        embed_list.append(main_embed)
        embed_list.append(profit_embed)
        embed_list.append(top_minions)

        await output.delete()

        # Final Menu
        output = await ctx.reply(embed=embed_list[0])
        # await output.add_reaction("⏮")
        await output.add_reaction("◀️")
        await output.add_reaction("▶️")
        # await output.add_reaction("⏭")
        pages = len(embed_list)
        current_page = 1
        reaction = None
        # Final Reaction Menu
        while True:
            if str(reaction) == "⏮":
                current_page = 1
                await output.edit(embed=embed_list[current_page-1])
            
            elif str(reaction) == "▶️" and current_page != pages:
                current_page += 1
                await output.edit(embed=embed_list[current_page-1])

            elif str(reaction) == "◀️" and current_page > 1:
                current_page -= 1
                await output.edit(embed=embed_list[current_page-1])
            
            elif str(reaction) == "⏭":
                current_page = pages
                await output.edit(embed=embed_list[current_page-1])
     
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)
                await output.remove_reaction(reaction, user)
            except:
                break

        await output.clear_reactions()
        await output.add_reaction("🛑")

        

def setup(bot):
    bot.add_cog(Minions(bot))