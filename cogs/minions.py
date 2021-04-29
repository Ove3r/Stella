import discord
from discord.ext import commands
from helpers.player import Player
from helpers.errors import *

class Minions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="minion", aliases=["minions"])
    
    async def command_minions(self, ctx, name, *profile):
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

        speed = 0
        modifiers = ""
        # Asks the user for a minion item
        query_embed = discord.Embed(title="What Minion Item Will You Use?", color=0xdc6565)
        query_embed.add_field(name="Note",value="It is assumed that one of your minion items will be a Dwarven Super Compactor 3000.")
        query_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        query_embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{user.uuid}")
        query_embed.set_footer(text="Stella Bot by Over#6203\nClick on the reactions for other tabs.")
        
        output = await ctx.reply(embed=query_embed)
        await output.add_reaction("<:diamond_spreading:837124543939346472>")
        await output.add_reaction("<:flycatcher:837124689176428605>")
        await output.add_reaction("🚫")

        # Check for reaction menus
        def check(reaction, user):
            # Ensures that the reaction is from the author and on the output message
            return user == ctx.author and reaction.message.id == output.id

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
                modifiers += "🚫 No Minion Upgrade"
                break

            try: #Timeout
                reaction, member = await self.bot.wait_for("reaction_add", timeout=45.0, check=check)
                await output.remove_reaction(reaction, member)
            except:
                await output.clear_reactions()
                await output.add_reaction("🛑")
                return

        await output.clear_reactions()
        
        query_embed = discord.Embed(title="What Minion Fuel Will You Use?", color=0xdc6565)
        query_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        query_embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{user.uuid}")
        query_embed.set_footer(text="Stella Bot by Over#6203\nClick on the reactions for other tabs.")






        embed_list = []

        main_embed = discord.Embed(title="Minions", description=f"`{user.name}` ~ `{user.fruit}`", color=0xdc6565)
        main_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        main_embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{user.uuid}")
        main_embed.set_footer(text="Stella Bot by Over#6203\nClick on the reactions for other tabs.")
        main_embed.add_field(name="Minion Slots", value=f"**{user.unlocks}**")
        main_embed.add_field(name="Unique Unlocks", value=f"**{user.unique_minion_count}**")

        # Profits Page
        user.get_yield_per_hour(modifier=speed)

        profit_embed = discord.Embed(title="Minions", description=f"`{user.name}` ~ `{user.fruit}`", color=0xdc6565)
        profit_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        profit_embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{user.uuid}")
        profit_embed.set_footer(text="Stella Bot by Over#6203\nClick on the reactions for other tabs.")
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
        

        await ctx.reply(embed=profit_embed)

        

        # Upgrade Cost Page
        upgrade_embed = discord.Embed(title="Minions", description=f"`{user.name}` ~ `{user.fruit}`", color=0xdc6565)
        upgrade_message = []
        for entry in user.upgrade_costs:
            if len(upgrade_message) > 10:
                break
            else:
                count = max(user.constants[entry[0]]['list'])
                upgrade_message.append(f"**{entry[0]}** ({count} --> {count+1}): **{'{:,}'.format(entry[1])}**")

        upgrade_embed.add_field(name="Cheapest Upgrades", value="\n".join(upgrade_message))
        upgrade_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        upgrade_embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{user.uuid}")
        upgrade_embed.set_footer(text="Stella Bot by Over#6203\nClick on the reactions for other tabs.")

        await ctx.reply(embed=upgrade_embed)
        


def setup(bot):
    bot.add_cog(Minions(bot))