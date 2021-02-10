import discord
from discord.ext import commands
import requests, json, statistics, random
from helpers import key
from helpers.ahparse import *
from helpers.utils import *


class Auctions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="price")
    async def check_price(self, ctx, *item):
        item = " ".join(item)
        sellers, prices = search_BIN(item)

        cheapest = min(prices)
        cheapestIndex = prices.index(cheapest)
        cheapestPrice = "{:,}".format(min(prices))
        cheapestSeller = getName(sellers[cheapestIndex])

        message = f"BIN Volume: `{'{:,}'.format(len(sellers))}\n`"
        message += f"Current Median Price: `{'{:,}'.format(statistics.median(prices))}`\n"
        message += f"Current Mean Price: `{'{:,}'.format(round(statistics.mean(prices)))}`\n"
        message += f"Standard Deviation: `{'{:,}'.format(round(statistics.stdev(prices)))}`\n\n\n"
        message += f"Cheapest Seller: `{cheapestSeller}` at `{cheapestPrice}`\n"
        try:
            del sellers[cheapestIndex]
            del prices[cheapestIndex]

            secondCheapest = min(prices)
            secondCheapestIndex = prices.index(secondCheapest)
            secondCheapestPrice = "{:,}".format(min(prices))
            secondCheapestSeller = getName(sellers[secondCheapestIndex])
            message += f"Second Cheapest Seller: `{secondCheapestSeller}` at `{secondCheapestPrice}`\n"
        except:
            pass
        try:
            del sellers[secondCheapestIndex]
            del prices[secondCheapestIndex]
            thirdCheapest = min(prices)
            thirdCheapestIndex = prices.index(thirdCheapest)
            thirdCheapestPrice = "{:,}".format(min(prices))
            thirdCheapestSeller = getName(sellers[thirdCheapestIndex])
            message += f"Third Cheapest Seller: `{thirdCheapestSeller}` at `{thirdCheapestPrice}`\n"
        except:
            pass

        embed=discord.Embed(title="AH Tracker", description="Database is refreshed every 5 minutes", color=0xdc6565)
        embed.set_footer(text="Stella Bot by Over#6203 ◆ This command only returns BINS.")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.add_field(name=item, value=message)
        #Assigns a random auction house agent as a thumbnail
        randomNPC = random.randint(0, 4)
        if randomNPC == 0:
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/hypixel-skyblock/images/a/a8/Auction_Master.png/revision/latest?cb=20200818185002")
        if randomNPC == 1:
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/hypixel-skyblock/images/e/e1/Auction_Agent_1.png/revision/latest/scale-to-width-down/500?cb=20200818191314")
        if randomNPC == 2:
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/hypixel-skyblock/images/d/d9/Auction_Agent_2.png/revision/latest/scale-to-width-down/500?cb=20200818185004")
        if randomNPC == 3:
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/hypixel-skyblock/images/3/34/Auction_Agent_3.png/revision/latest/scale-to-width-down/500?cb=20200818185005")
        if randomNPC == 4:
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/hypixel-skyblock/images/f/fd/Auction_Agent_4.png/revision/latest/scale-to-width-down/500?cb=20200818185005")

        await ctx.send(embed=embed)

    @commands.command(aliases=["dah","da"])
    async def check_dark_auction(self, ctx):
        dark_auction, darker_auction = get_dark_auction()
        embed=discord.Embed(title="Dark Auctions", description="Dark Auction/Darker Auction Price Tracker", color=0xdc6565)
        embed.set_footer(text="Stella Bot by Over#6203 ◆ Prices are BIN Minimum")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/hypixel-skyblock/images/1/18/Sirius.png/revision/latest?cb=20200729005335")
        embed.add_field(name="Dark Auction",value=dark_auction,inline=True)
        embed.add_field(name="Darker Auction",value=darker_auction,inline=True)

        await ctx.send(embed=embed)

    @commands.command(aliases=["auctions","ah"])
    async def check_player_ah(self, ctx, *name):
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

        message, totalmessage = parse_player_ah(uuid)
        embed=discord.Embed(title=name, description="AH Data", color=0xdc6565)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Stella Bot by Over#6203")
        embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
        if message != "No Items":
            embed.add_field(name="Items", value=message, inline=False)
            embed.add_field(name="Totals", value=totalmessage,inline=False)
        else:
            embed.add_field(name="Error",value=f"There are no items up on `{name}`'s AH or sales to claim.",inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=["bits","bit"])
    async def bits_to_coins(self, ctx):
        loading = await ctx.send(embed=discord.Embed(title="Bits Calculator", description="Loading", color=0xdc6565))
        message = coins_per_bit()
        embed=discord.Embed(title="Bits Calculator", description="Values are in gold per bit", color=0xdc6565)
        embed.add_field(name="\u200b", value=message,inline=False)
        embed.add_field(name="\u200b", value="Equations can be found [here](http://bit.ly/2KOKXun).",inline=False)
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/hypixel-skyblock/images/d/d9/Elizabeth.png/revision/latest?cb=20200915233823")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Stella Bot by Over#6203")
        await loading.edit(embed=embed)



def setup(bot):
    bot.add_cog(Auctions(bot))
