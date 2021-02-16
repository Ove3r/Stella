import discord
import json
from discord.ext import commands
from helpers.utils import *

class Trackers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="status",aliases=["location"],
        brief="Returns the location of a player",
        help=(
        "**stella status [ign]**\n"
        "Returns the current skyblock location of a player.\n"
        "Notes: \n "
        "• If a player argument is not given, the user's discord display name will be used instead."
        )
    )
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
            await ctx.reply(embed=embed)
            return
        status = get_player_status(uuid)
        embed=discord.Embed(title=name, description="\u200b", color=0xdc6565)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Stella Bot by Over#6203")
        embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
        if not status:
            embed.add_field(name="**Current Location**",value="Not connected to mc.hypixel.net.")
        elif status == "dynamic":
            embed.add_field(name="**Current Location**",value="A Personal Skyblock Island.")
        else:
            embed.add_field(name="**Current Location**",value=status)
        await ctx.reply(embed=embed)

    @commands.command(name="afk",
        brief="Begins AFK Tracking",
        help=(
        "**stella afk [ign]**\n"
        "Adds a given player to a tracker that will notify you if the player leaves a personal island.\n"
        "Notes: \n "
        "• The tracker does a check once every minute.\n"
        "• If a player argument is not given, the user's discord display name will be used instead."
        )
    )
    async def add_afk(self, ctx, *name):
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
            await ctx.reply(embed=embed)
            return

        with open("data/afk.json") as afk_track:
            data = json.load(afk_track)
        with open("data/afk.json","w") as afk_track:
            entry = {
                "player": name,
                "uuid": uuid,
                "discord_id": ctx.author.id
            }
            data["tracking"].append(entry)
            afk_track.write(json.dumps(data))

        embed=discord.Embed(title="AFK Tracker", description=f"I will DM you if `{name}` is no longer on a personal island.", color=0xdc6565)
        embed.set_footer(text="Stella Bot by Over#6203 ◆ AFK Tracker refreshes every minute")
        embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Trackers(bot))
