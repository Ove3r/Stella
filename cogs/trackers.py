import discord
from discord.ext import commands
from helpers.utils import *

class Trackers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["status","location"])
    async def check_player_location(self, ctx, *name):
        if (not name):
            name = ctx.author.display_name
        else:
            name = name[0]
        try:
            uuid = getUUID(name)
        except PlayerNotFound:
            embed=discord.Embed(title="Error ◆ PlayerNotFound", description=f"Player `{name}` not found.", color=0xdc6565)
            embed.set_footer(text=f"Stella Bot by Over#6203 ")
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            return
        status = get_player_status(uuid)
        embed=discord.Embed(title=name, description="\u200b", color=0xdc6565)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Stella Bot by Over#6203")
        embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
        if not status:
            embed.add_field(name="**Current Location**",value="Not connected to mc.hypixel.net.")
        elif status = "DYNAMIC":
            embed.add_field(name="**Current Location**",value="A Personal Skyblock Island.")
        else:
            embed.add_field(name="**Current Location**",value=status)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Trackers(bot))
