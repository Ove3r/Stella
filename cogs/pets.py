import discord
from discord.ext import commands
import requests, json
from helpers import key
from helpers.utils import *
from constants.constants_pets import GET_PETS_CONSTANTS

class Pets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def pets_flip(self, PETS_CONSTANTS):
        with open("data/ah.json") as database:
            database = json.load(database)

        #Iterate through
        for entry in database["auctions"]:
            if "bin" in entry:
                for check in PETS_CONSTANTS:
                    if (check["extra"] in entry["extra"]) and (check["tier"] in entry["tier"]):
                        check["entire_list"].append(entry["starting_bid"])
                        if check["maxed"] in entry["extra"]:
                            check["maxed_list"].append(entry["starting_bid"])
                        break

        messages = {
            "farming" : "",
            "mining" : "",
            "combat" : "",
            "foraging" : "",
            "fishing" : "",
            "other" : ""
        }
        for entry in PETS_CONSTANTS:
            try:
                messages[entry["category"]] += f"**{entry['name']}** : {'{:,}'.format(min(entry['maxed_list'])-min(entry['entire_list']))}\n"
            except:
                pass
        return messages

    @commands.command(name="pets",
        brief="Pets Flipper",
        help=(
            "**stella pets**\n"
            "Returns a menu for profit/loss from leveling **LEGENDARY** pets.\n"
            "Notes: \n "
            "• Calculations take the cheapest BIN for the pet and compares it to the cheapest **[lvl 100]** for that pet.\n"
            "• To navigate the menu, click the reactions."
        )
    )
    async def pets_calculator(self,ctx):
        print(f"{ctx.author.name} sent pets command in {ctx.guild}")
        def check(reaction, member): #For Tab Menu
            return member == ctx.author

        def tabs_embed(message, category, thumbnail): #For creating new embeds for each category
            embed=discord.Embed(title=f"Pets Leveling", description=f"Profit from leveling **{rarity}** pets from cheapest BIN to lvl 100.", color=0xdc6565)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=thumbnail)
            embed.set_footer(text="Stella Bot by Over#6203\nClick on the reactions for other tabs.")
            embed.add_field(name=category,value=message)
            return embed

        constants = GET_PETS_CONSTANTS()
        messages = self.pets_flip(constants)
        rarity = "LEGENDARY"
        home_tab=discord.Embed(title=f"Pets Leveling", description=f"Profit from leveling **{rarity}** pets from cheapest BIN to lvl 100.", color=0xdc6565)
        home_tab.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        home_tab.set_footer(text="Stella Bot by Over#6203\nClick on the reactions for other tabs.")
        output = await ctx.reply(embed=home_tab)
        await output.add_reaction("<:golden_hoe:801205315806167050>")
        await output.add_reaction("<:stone_pickaxe:810604855726571545>")
        await output.add_reaction("<:stone_sword:810605120752058408>")
        await output.add_reaction("<:jungle_sapling:810605504934051892>")
        await output.add_reaction("<:fishing:801090235542929448>")
        await output.add_reaction("<:spawn_egg:810606172997812258>")

        #Tab Menu
        reaction = None
        while True:
            if str(reaction) == "<:golden_hoe:801205315806167050>":
                await output.edit(embed=tabs_embed(messages["farming"],"Farming","https://static.wikia.nocookie.net/hypixel-skyblock/images/a/af/Elephant_Pet.png/revision/latest?cb=20200506101231"))
            elif str(reaction) == "<:stone_pickaxe:810604855726571545>":
                await output.edit(embed=tabs_embed(messages["mining"],"Mining","https://static.wikia.nocookie.net/hypixel-skyblock/images/0/0c/Silverfish_Pet.png/revision/latest?cb=20200222204846"))
            elif str(reaction) == "<:stone_sword:810605120752058408>":
                await output.edit(embed=tabs_embed(messages["combat"],"Combat","https://static.wikia.nocookie.net/hypixel-skyblock/images/f/f2/Wolf_Pet.png/revision/latest?cb=20200222204848"))
            elif str(reaction) == "<:jungle_sapling:810605504934051892>":
                await output.edit(embed=tabs_embed(messages["foraging"],"Foraging","https://static.wikia.nocookie.net/hypixel-skyblock/images/e/e9/Ocelot_Pet.png/revision/latest?cb=20200222204840"))
            elif str(reaction) == "<:fishing:801090235542929448>":
                await output.edit(embed=tabs_embed(messages["fishing"],"Fishing","https://static.wikia.nocookie.net/hypixel-skyblock/images/e/ec/Flying_Fish_Pet.png/revision/latest?cb=20200222204853"))
            elif str(reaction) == "<:spawn_egg:810606172997812258>":
                await output.edit(embed=tabs_embed(messages["other"],"Enchanting/Alchemy","https://static.wikia.nocookie.net/hypixel-skyblock/images/4/47/Parrot_Pet.png/revision/latest?cb=20200222204854"))
            try: #Timeout
                reaction, member = await self.bot.wait_for("reaction_add", timeout=45.0, check=check)
                await output.remove_reaction(reaction, member)
            except:
                break
        await output.clear_reactions()
        await output.add_reaction("🛑")


def setup(bot):
    bot.add_cog(Pets(bot))
