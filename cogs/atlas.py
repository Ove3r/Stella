## Prototype Command that is currently a proof of concept

import discord
from discord.ext import commands
import json
import requests


def bazaar(item, title="Bazaar Statistics", name="Bazaar", thumbnail="https://static.wikia.nocookie.net/hypixel-skyblock/images/c/c8/Bazaar.png/revision/latest?cb=20200729000145"):
    bazaar_data = requests.get("https://api.hypixel.net/skyblock/bazaar").json()["products"][item]
    sell_price = "{:,}".format(round(bazaar_data["sell_summary"][0]["pricePerUnit"],3))
    buy_price = "{:,}".format(round(bazaar_data["buy_summary"][0]["pricePerUnit"],3))
    sold_per_week = "{:,}".format(bazaar_data["quick_status"]["sellMovingWeek"])
    buy_per_week = "{:,}".format(bazaar_data["quick_status"]["buyMovingWeek"])
    market_volume = "{:,}".format(bazaar_data["quick_status"]["sellVolume"])
    buy_orders = "{:,}".format(bazaar_data["quick_status"]["buyOrders"])
    sell_orders  = "{:,}".format(bazaar_data["quick_status"]["sellOrders"])

    message = f"**Market Volume: ** {market_volume}\n\n"
    message += f"**Buy Price: ** {buy_price}\n"
    message += f"**Sell Price: ** {sell_price}\n"
    message += f"\n**Buy Orders:** {buy_orders}\n"
    message += f"**Sell Orders: ** {sell_orders}\n"
    message += f"\n**Items Bought in Last 7 Days:** {buy_per_week}\n"
    message += f"**Items Sold in Last 7 Days:** {sold_per_week}"

    bazzar_embed = discord.Embed(title=title, description="Bazaar", color=0xdc6565)
    bazzar_embed.set_footer(text="Atlas from Stella Bot by Over#6203\nClick on the reactions to navigate menus.")
    bazzar_embed.set_thumbnail(url=thumbnail)
    bazzar_embed.add_field(name=name,value=message,inline=False)
    
    return bazzar_embed

class Atlas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="atlas",
        brief="Proof of Concept",
        help=(
            "**stella atlas [item]**\n"
            "Returns a menu a given item.\n"
            "Notes: \n "
            "• This is currently in an Alpha Stage.\n"
            "• To navigate the menu, click the reactions.\n"
            "• At this point only a few items are added (i.e. Cobblestone)"
        )  
    )
    async def search_atlas(self, ctx, item):
        # Receives a json object containing all embed info. This will be integrated with fuzzysearch with a table of contents.
        with open("data/atlas/index.json") as toc:
            index = json.load(toc)
        
        if item.lower() in index:
            with open(f"data/atlas/{index[item.lower()]}.json") as object_file:
                atlas_data = json.load(object_file)
        else:
            failure_embed = discord.Embed(title="Item Not Found", description="Atlas is still in beta. More items will be added in the future.", color=0xdc6565)
            failure_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            failure_embed.set_footer(text="Atlas from Stella Bot by Over#6203")
            await ctx.reply(embed=failure_embed)
            return
        # Initializes all embeds defined in json
        # TODO: Only load embed object on call for that object rather than on initialization
        # TODO: Integrate some form of dynamic auction prices
        embed_list = []
        for pages in atlas_data["pages"]:
            if "function" in pages:
                embed_list.append(eval(pages["function"],{"bazaar":bazaar}))
            else:
                item_tab = discord.Embed(title=pages["title"], description=pages["page_description"] if "page_description" in pages else atlas_data["summary_description"], color=0xdc6565)
                item_tab.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                item_tab.set_footer(text="Atlas from Stella Bot by Over#6203\nClick on the reactions to navigate menus.")
                if "thumbnail" in pages:
                    item_tab.set_thumbnail(url=pages["thumbnail"])
                if "image" in pages:
                    item_tab.set_image(url=pages["image"])
                if "fields" in pages:
                    for field in pages["fields"]:
                        item_tab.add_field(name=field["field_title"],value=field["field_description"],inline=False)
                embed_list.append(item_tab.copy())

        output = await ctx.reply(embed=embed_list[0])
        await output.add_reaction("⏮")
        await output.add_reaction("◀️")
        await output.add_reaction("▶️")
        await output.add_reaction("⏭")

        # Check for reaction menu
        def check(reaction, user):
            return user == ctx.author
        
        # Reaction menu
        tabs = len(atlas_data["pages"])
        current_tab = 1
        reaction = None
        while True:
            if str(reaction) == "⏮":
                current_tab = 1
                await output.edit(embed=embed_list[current_tab-1])
            
            elif str(reaction) == "▶️" and current_tab != tabs:
                current_tab += 1
                await output.edit(embed=embed_list[current_tab-1])

            elif str(reaction) == "◀️" and current_tab > 1:
                current_tab -= 1
                await output.edit(embed=embed_list[current_tab-1])
            
            elif str(reaction) == "⏭":
                current_tab = tabs
                await output.edit(embed=embed_list[current_tab-1])
     
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)
                await output.remove_reaction(reaction, user)
            except:
                break

        await output.clear_reactions()
def setup(bot):
    bot.add_cog(Atlas(bot))
