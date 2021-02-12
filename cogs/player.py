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

    @commands.command(name="uuid")
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

    @commands.command(name="player")
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
        player_tab.add_field(name=f"Skill Average: {user.skill_average}",value="\u200b",inline=False)
        player_tab.add_field(name="Skills", value=user.skills_message, inline=True)
        player_tab.add_field(name="\u200b",value="\u200b",inline=True)
        if user.api_enabled:
            #Add Slayers/Dungeons Message
            pass

        output = await ctx.reply(embed=player_tab)
        await output.add_reaction("<:player:801091911166984232>")
        if user.api_enabled: #Tabs only available to users with APIs enabled
            await output.add_reaction("<:pie_chart:809912045410451456>")

        reaction = None
        while True:
            if str(reaction) == "<:player:801091911166984232>":
                await output.edit(embed=player_tab)
            elif str(reaction) == "<:pie_chart:809912045410451456>" and user.api_enabled: #Pie Chart Tab
                try:
                    pie_chart_embed
                except:
                    path = user.get_player_xp_pie()
                    channel = self.bot.get_channel(798985613793689621)
                    special = await channel.send(file=discord.File(path, filename = "pie.png"))
                    pie_chart_url = special.attachments[0].url
                    pie_chart_embed=discord.Embed(title=user.name, description="Pie Chart", color=0xdc6565)
                    pie_chart_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                    pie_chart_embed.set_image(url=pie_chart_url)

                await output.edit(embed=pie_chart_embed)

            try:
                reaction, member = await self.bot.wait_for("reaction_add", timeout=60.0, check=check)
                await output.remove_reaction(reaction, member)
            except Exception as exception: #For Debugging ~~ Remove Later
                print(exception)
                break
        await output.clear_reactions()


def setup(bot):
    bot.add_cog(Player_Commands(bot))
