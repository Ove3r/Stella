import discord
from discord.ext import commands
import requests, json
from helpers import key
from helpers.errors import *
from helpers.utils import *
from helpers.player import *
from constants import constants_map
from helpers.map import get_player_status_image

class Player_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="uuid",
        brief="Returns a player's uuid",
        help=(
        "**stella uuid [ign]**\n"
        "Returns a player's Minecraft UUID."
        "Notes: \n "
        "• If a player argument is not given, the user's discord display name will be used instead."
        )
    )
    async def fetch_uuid(self, ctx, *name):
        print(f"{ctx.author.name} sent uuid command in {ctx.guild}")
        if (not name):
            name = ctx.author.display_name
        else:
            name = name[0]
        try:
            uuid = getUUID(name)
            embed=discord.Embed(title=f"{name}", description=uuid, color=0xdc6565)
            embed.set_footer(text="Stella Bot by Over#6203")
            embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        except PlayerNotFound:
            embed=discord.Embed(title="Error ◆ PlayerNotFound", description=f"Player `{name}` not found.", color=0xdc6565)
            embed.set_footer(text="Stella Bot by Over#6203 ")
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)

    @commands.command(name="player",
        brief="Returns a player summary",
        help=(
        "**stella player [ign] [optional: profile]**\n"
        "Returns a summary of a player's SkyBlock statistics.\n"
        "Notes: \n "
        "• More stats and tabs are available to players who have APIs enabled."
        )
    )
    async def get_player(self, ctx, name, *profile):
        print(f"{ctx.author.name} sent player command in {ctx.guild}")
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

        def check(reaction, member): #For Tab Menu
            return member == ctx.author

        user.get_player_summary()
        user.get_skills_message()
        location = get_player_status(user.uuid)
        #Main Tab
        player_tab=discord.Embed(title=f"{user.name} ({user.rank})", description=f"Profile: {user.fruit}\nAll Profiles: {' '.join(map(str, user.profile_list))}", color=0xdc6565)
        player_tab.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        player_tab.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{user.uuid}")
        if user.api_enabled:
            player_tab.set_footer(text="Stella Bot by Over#6203\nClick on the reactions for other tabs.")
        else:
            player_tab.set_footer(text="Stella Bot by Over#6203 ◆ Features May Not Be Available (Certain APIs are Disabled)\nClick on the reactions for other tabs.")
        if user.guild:
            player_tab.add_field(name=f"Guild: {user.guild}",value="\u200b",inline=False)
        player_tab.add_field(name=f"Skill Average: {user.skill_average}",value="\u200b",inline=False)
        player_tab.add_field(name="Skills", value=user.skills_message, inline=False)
        
        user.get_slayer_dungeon_message()
        player_tab.add_field(name="Slayers",value=user.slayer_message +"\n**Dungeons**\n"+ user.dungeon_message,inline=False)
        output = await ctx.reply(embed=player_tab)
        await output.add_reaction("<:player:801091911166984232>")
        await output.add_reaction("<:golden_hoe:801205315806167050>")
        await output.add_reaction("<:fishing:801090235542929448>")
        if location in constants_map.LOCATIONS:
            await output.add_reaction("🌎")
        if user.api_enabled: #Tabs only available to users with APIs enabled
            await output.add_reaction("<:pie_chart:809912045410451456>")


        reaction = None
        while True:
            if str(reaction) == "<:player:801091911166984232>":
                await output.edit(embed=player_tab)
            elif str(reaction) == "<:golden_hoe:801205315806167050>": #Farming/Jacob Contest Tab
                try:
                    jacob_tab
                except:
                    user.get_jacob_summary()
                    jacob_tab=discord.Embed(title=user.name, description="Farming Tab", color=0xdc6565)
                    jacob_tab.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                    jacob_tab.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{user.uuid}")
                    jacob_tab.set_footer(text="Stella Bot by Over#6203")
                    try:
                        jacob_tab.add_field(name="Perks",value=user.jacob_perks)
                        jacob_tab.add_field(name="Most Recent Claimed Contests",value=user.jacob_summary)
                    except:
                        pass

                await output.edit(embed=jacob_tab)
            elif str(reaction) == "<:fishing:801090235542929448>": #Fishing Stats
                try:
                    fishing_tab
                except:
                    user.get_fishing_stats()
                    fishing_tab=discord.Embed(title=user.name, description="Fishing Tab", color=0xdc6565)
                    fishing_tab.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                    fishing_tab.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{user.uuid}")
                    fishing_tab.set_footer(text="Stella Bot by Over#6203")
                    for entry in user.fishing_messages:
                        if user.fishing_messages[entry] != "":
                            fishing_tab.add_field(name=entry,value=user.fishing_messages[entry],inline=False)

                await output.edit(embed=fishing_tab)
            elif str(reaction) == "<:pie_chart:809912045410451456>" and user.api_enabled: #Pie Chart Tab
                try:
                    pie_chart_embed
                except:
                    path = user.get_player_xp_pie()
                    channel = self.bot.get_channel(798985613793689621)
                    image_workaround = await channel.send(file=discord.File(path, filename = "pie.png"))
                    pie_chart_url = image_workaround.attachments[0].url
                    pie_chart_tab=discord.Embed(title=user.name, description="Pie Chart", color=0xdc6565)
                    pie_chart_tab.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                    pie_chart_tab.set_image(url=pie_chart_url)

                await output.edit(embed=pie_chart_tab)
            elif str(reaction) == "🌎" and location in constants_map.LOCATIONS:
                try:
                    player_location_tab
                except:
                    path = get_player_status_image(user, location)
                    channel = self.bot.get_channel(798985613793689621)
                    map_image = await channel.send(file=discord.File(path,filename="map.png"))
                    map_image_url = map_image.attachments[0].url

                    player_location_tab=discord.Embed(title=user.name, description=f"[Current Location]({map_image_url})", color=0xdc6565)
                    player_location_tab.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                    player_location_tab.set_footer(text="Stella Bot by Over#6203 ◆ Refreshes on command load.")
                    player_location_tab.set_image(url=map_image_url)

                await output.edit(embed=player_location_tab)
            try: #Timeout
                reaction, member = await self.bot.wait_for("reaction_add", timeout=45.0, check=check)
                await output.remove_reaction(reaction, member)
            except: #For Debugging ~~ Remove Later
                break
        await output.clear_reactions()
        await output.add_reaction("🛑")


def setup(bot):
    bot.add_cog(Player_Commands(bot))
