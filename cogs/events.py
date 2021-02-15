import discord
import time, math
from discord.ext import commands
from helpers.utils import *

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="events",
        brief="Returns approximate timers for events",
        help=(
        "**stella events**\n"
        "Returns approximate timers for events."
        )
    )
    async def get_all_events(self, ctx):
        calendar_events = get_calendar_events()
        currentTime = time.time()*1000

        embed=discord.Embed(title="Events", description=f"Approximate Event Timers", color=0xdc6565)
        embed.set_footer(text="Stella Bot by Over#6203 ")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        for calendar in calendar_events:
            timeDifference = item[1] - currentTime
            difference = ms_to_standard(timeDifference)
            embed.add_field(name=item[0],value=difference,inline=False)
        await ctx.reply(embed=embed)


    @commands.command(name="jacob",
        brief="Returns next 3 Jacob Events",
        help=(
        "**stella jacob**\n"
        "Returns approximate timers for the next 3 jacob events along with the crops for those events."
        )
    )
    async def get_jacob_events(self, ctx):
        data = requests.get("https://sky.matcool.tk/api/upcomingEvents").json()
        currentTime = time.time()*1000
        entry = 0
        while data[entry]["timestamp"] <= currentTime:
            entry += 1

        embed=discord.Embed(title="Jacob Events", description=f"Approximate Event Timers", color=0xdc6565)
        embed.set_footer(text="Stella Bot by Over#6203 ")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        while entry <= (len(data)-1) and len(embed.fields) < 3:
            try:
                event = data[entry]
                time_difference = event["timestamp"] - currentTime
                event_time = str(math.floor(time_difference/(1000*60*60)%24)) + " hr. " + str(math.floor(time_difference/1000/60%60)) + " min. " + str(round((time_difference/1000) % 60)) + " sec."
                cropMessage = changeCrops(event["crops"][0]) + "\n" + changeCrops(event["crops"][1]) + "\n" + changeCrops(event["crops"][2])
                embed.add_field(name=event_time,value=cropMessage)
                entry += 1
            except:
                if len(embed.fields) == 0:
                    embed.add_field(name="More Jacob Farming Events will be accessible after the year starts.", value='\u200b',inline=False)
        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(Events(bot))
