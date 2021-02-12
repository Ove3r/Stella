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
            embed.set_footer(text=f"Stella Bot by Over#6203 ")
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

        user.get_player_summary()

        #Chart Tab
        path = user.get_player_xp_pie()
        file = discord.File(path, filename = "pie.png")
        embed=discord.Embed(title=name, description="Pie Chart", color=0xdc6565)
        embed.set_footer(text=f"Stella Bot by Over#6203 ")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_image(url="attachment://pie.png")
        await ctx.reply(embed=embed,file=file)

def setup(bot):
    bot.add_cog(Player_Commands(bot))
