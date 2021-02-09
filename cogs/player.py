import discord
from discord.ext import commands
import requests, json
from helpers import key
from helpers.errors import *
from helpers.utils import *

class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="uuid")
    async def fetch_uuid(self, ctx, name):
        try:
            uuid = getUUID(name)
            embed=discord.Embed(title=f"{name}", description=uuid, color=0xdc6565)
            embed.set_footer(text="Stella Bot by Over#6203")
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        except PlayerNotFound:
            embed=discord.Embed(title="Error ◆ PlayerNotFound", description=f"User `{name}` not found.", color=0xdc6565)
            embed.set_footer(text=f"Stella Bot by Over#6203 ")
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Player(bot))
