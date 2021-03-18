import discord
from discord.ext import commands
import requests, json, statistics, random
from helpers import key
from helpers.ahparse import *
from helpers.utils import *
from googleapiclient.discovery import build

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

class Auctions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="price",
        brief="Returns BIN statistics for a given item",
         help = (
         "**stella price [item]**\n"
         "Returns the following BIN Statistics for the given item: \n ```BIN Volume, Median, Mean, Standard Deviation, Cheapesst Sellers```"
         "Notes: \n • This command requires exact spelling for items."
         )
    )
    async def check_price(self, ctx, *item):
        print(f"{ctx.author.name} sent price command in {ctx.guild}")
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

        await ctx.reply(embed=embed)

    @commands.command(name="da",
        brief="Returns Dark Auction Prices",
        help=(
        "**stella da**\n"
        "Returns the BIN Minimum Prices for all items available on the Dark Auction along with items avilable from Darker Auctions"
        )
    )
    async def check_dark_auction(self, ctx):
        print(f"{ctx.author.name} sent dark auction command in {ctx.guild}")
        dark_auction, darker_auction = get_dark_auction()
        embed=discord.Embed(title="Dark Auctions", description="Dark Auction/Darker Auction Price Tracker", color=0xdc6565)
        embed.set_footer(text="Stella Bot by Over#6203 ◆ Prices are BIN Minimum")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/hypixel-skyblock/images/1/18/Sirius.png/revision/latest?cb=20200729005335")
        embed.add_field(name="Dark Auction",value=dark_auction,inline=True)
        embed.add_field(name="Darker Auction",value=darker_auction,inline=True)

        await ctx.reply(embed=embed)

    @commands.command(name="ah",aliases=["auctions"],
        brief="Returns player AH",
        help=(
        "**stella ah [player]**\n"
        "Returns all items currently listed for a given player on the auction house.\n\n"
        "Notes: \n • If a player argument is not given, the user's discord display name will be used instead."
        )
    )
    async def auctions(self, ctx, *name):
        print(f"{ctx.author.name} sent auction player command in {ctx.guild}")
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
        await ctx.reply(embed=embed)

    @commands.command(name="bits",aliases=["bit"],
        brief="Returns gold values for bit items",
        help=(
        "**stella bits**\n"
        "Returns gold values for bits purchasable items."
        )
    )
    async def bits_to_coins(self, ctx):
        print(f"{ctx.author.name} sent bits command in {ctx.guild}")
        loading = await ctx.reply(embed=discord.Embed(title="Bits Calculator", description="Loading...", color=0xdc6565))
        crafted_message, raw_item = coins_per_bit()
        embed=discord.Embed(title="Bits Calculator", description="Values are in gold per bit", color=0xdc6565)
        embed.add_field(name="Raw Items", value=raw_item,inline=True)
        embed.add_field(name="Craftables", value=crafted_message,inline=True)
        embed.add_field(name="\u200b", value="Equations can be found [here](http://bit.ly/2KOKXun).",inline=False)
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/hypixel-skyblock/images/d/d9/Elizabeth.png/revision/latest?cb=20200915233823")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Stella Bot by Over#6203")
        await loading.edit(embed=embed)

    @commands.command(name="forge",
        brief="Returns g/h values of all foragable items",
        help=(
        "**stella forge**\n"
        "Returns gold per hour values of all foragable items.\n"
        "Notes: \n "
        "• Values reflected by the calculator may not guarantee profits.\n"
        "• The calculator does not account for the Quick Forge Specialization in the HOTM Skill Tree.\n"
        "• The Quick Forge Specialization does affect the profit or loss of the crafts, only the gold per hour values."
        )
    )
    async def forge_coins_per_hour(self, ctx):
        print(f"{ctx.author.name} sent forge command in {ctx.guild}")
        loading = await ctx.reply(embed=discord.Embed(title="Forge Calculator", description="Loading...", color=0xdc6565))
        forgeMessage, castingMessage = get_forge()
        embed=discord.Embed(title="Forge Calculator", description="Values are in gold per hour", color=0xdc6565)
        embed.add_field(name="Casting", value=castingMessage,inline=True)
        embed.add_field(name="Refinement", value=forgeMessage,inline=True)
        embed.add_field(name="\u200b", value="Equations can be found [Here](http://bit.ly/2LMbolc).",inline=False)
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/minecraft/images/c/c6/BlastFurnace.png/revision/latest?cb=20181219150603")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Stella Bot by Over#6203 \n◆ Indicates A Special Case - See Equations")
        await loading.edit(embed=embed)

    @commands.command(name="floor",aliases=["dungeons","dungeon"],
        brief="Returns dungeon values",
        help=(
        "**stella floor [floor number]**\n"
        "Returns gold values for end of loot dungeon items for a given floor.\n"
        "Notes: \n "
        "• Values updated every 5 minutes with the ah database refresh.\n"
        )
    )
    async def dungeon_coins(self,ctx, floor):
        print(f"{ctx.author.name} sent floor command in {ctx.guild} for floor {floor}")
        try:
            if int(floor) in range(1,8):
                books, armor = get_dungeon(floor)
            else:
                await ctx.reply("Improper usage. See `stella help floor`.")
                return
        except:
            result = google_search(floor, key.google_api_key, key.search_engine_id)
            embed=discord.Embed(title=f"{floor}", description=f"[{result['queries']['request'][0]['title']}]({result['items'][0]['link']})", color=0xdc6565)
            embed.add_field(name=result['items'][0]['title'],value=f"```{result['items'][0]['snippet']}```")
            embed.set_footer(text="Stella Bot by Over#6203 ~ Easter Eggs!")
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url,url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            await ctx.reply(embed=embed)
            return
        embed=discord.Embed(title=f"Dungeon Floor {floor}", description="End of Dungeon Prices", color=0xdc6565)
        embed.add_field(name="Books", value=books,inline=True)
        embed.add_field(name="Armor", value=armor,inline=True)
        thumbnails = [
            "https://static.wikia.nocookie.net/hypixel-skyblock/images/6/63/The_Catacombs_-_Floor_VII.png/revision/latest?cb=20201205062458",
            "https://static.wikia.nocookie.net/hypixel-skyblock/images/1/1f/Bonzo.png/revision/latest?cb=20200923184232",
            "https://static.wikia.nocookie.net/hypixel-skyblock/images/5/56/Scarf.png/revision/latest?cb=20201014204105",
            "https://static.wikia.nocookie.net/hypixel-skyblock/images/9/96/The_Professor.png/revision/latest?cb=20201101180239",
            "https://static.wikia.nocookie.net/hypixel-skyblock/images/8/89/Ghast.png/revision/latest?cb=20191207182644",
            "https://static.wikia.nocookie.net/hypixel-skyblock/images/1/13/Livid.png/revision/latest?cb=20201101032941",
            "https://static.wikia.nocookie.net/hypixel-skyblock/images/e/eb/Sadan.png/revision/latest?cb=20201101032732",
            "https://static.wikia.nocookie.net/hypixel-skyblock/images/7/7e/Necron.png/revision/latest?cb=20201118185458",
        ]
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=thumbnails[int(floor)])
        embed.set_footer(text="Stella Bot by Over#6203")
        await ctx.reply(embed=embed)

    @commands.command(name="mythos", aliases=["diana", "mithos", "Diana"],
        brief="Returns Mythos Prices",
        help=(
        "**stella mythos**\n"
        "Returns the BIN Minimum Prices for all items available from Diana's Mythological Event."
        )
    )
    async def check_mythos_prices(self, ctx):
        print(f"{ctx.author.name} sent mythos command in {ctx.guild}")
        auctionables, bazaarables = get_mithos()
        embed=discord.Embed(title=f"Mythological Event", description="Mythos Price Tracker", color=0xdc6565)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/hypixel-skyblock/images/5/5f/Diana.png/revision/latest?cb=20200912120658")
        embed.set_footer(text="Stella Bot by Over#6203 ◆ Prices are BIN Minimum")
        embed.add_field(name="Auctionables", value=auctionables,inline=True)
        embed.add_field(name="Bazaarables", value=bazaarables,inline=True)
        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(Auctions(bot))
