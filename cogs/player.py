import discord
from discord.ext import commands
import requests, json
from helpers import key
from helpers.errors import *
from helpers.utils import *
from helpers.player import *

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
        if (not name):
            name = ctx.author.display_name
        else:
            name = name[0]
        try:
            uuid = getUUID(name)
            embed=discord.Embed(title=f"{name}", description=uuid, color=0xdc6565)
            embed.set_footer(text="Stella Bot by Over#6203")
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        except PlayerNotFound:
            embed=discord.Embed(title="Error ◆ PlayerNotFound", description=f"Player `{name}` not found.", color=0xdc6565)
            embed.set_footer(text="Stella Bot by Over#6203 ")
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)

    @commands.command(name="player",
        brief="Returns a player summary",
        help=(
        "**stella player [ign]**\n"
        "Returns a summary of a player's SkyBlock statistics.\n"
        "Notes: \n "
        "• If a player argument is not given, the user's discord display name will be used instead."
        "• More stats and tabs are available to players who have APIs enabled."
        )
    )
    async def get_player(self, ctx, name, *profile):
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
        #Main Tab
        player_tab=discord.Embed(title=user.name, description=f"Profile: {user.fruit}\nAll Profiles: {' '.join(map(str, user.profile_list))}", color=0xdc6565)
        player_tab.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        player_tab.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{user.uuid}")
        if user.api_enabled:
            player_tab.set_footer(text="Stella Bot by Over#6203")
        else:
            player_tab.set_footer(text="Stella Bot by Over#6203 ◆ Features May Not Be Available (Certain APIs are Disabled)")
        if user.guild:
            player_tab.add_field(name=f"Guild: {user.guild}",value="\u200b",inline=False)
        player_tab.add_field(name=f"Skill Average: {user.skill_average}",value="\u200b",inline=False)
        player_tab.add_field(name="Skills", value=user.skills_message, inline=False)
        if user.api_enabled:
            user.get_slayer_dungeon_message()
            player_tab.add_field(name="Slayers",value=user.slayer_message +"\n**Dungeons**\n"+ user.dungeon_message,inline=False)
        output = await ctx.reply(embed=player_tab)
        await output.add_reaction("<:player:801091911166984232>")
        await output.add_reaction("<:golden_hoe:801205315806167050>")
        if user.api_enabled: #Tabs only available to users with APIs enabled
            await output.add_reaction("<:pie_chart:809912045410451456>")

        reaction = None
        while True:
            if str(reaction) == "<:player:801091911166984232>":
                await output.edit(embed=player_tab)
            elif str(reaction) == "<:golden_hoe:801205315806167050>": #Farmig/Jacob Contest Tab
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

            try:
                reaction, member = await self.bot.wait_for("reaction_add", timeout=45.0, check=check)
                await output.remove_reaction(reaction, member)
            except Exception as exception: #For Debugging ~~ Remove Later
                print(exception)
                break
        await output.clear_reactions()
        await output.add_reaction("🛑")

    @commands.command(name="test")
    async def test(self, ctx, name, *profile):
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

        await ctx.reply(embed=jacob_tab)


def setup(bot):
    bot.add_cog(Player_Commands(bot))
