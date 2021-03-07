import discord
from discord.ext import commands
import json


class Atlas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="atlas")
    async def search_atlas(self, ctx, item):
        with open("data/atlas/collections/cobblestone/cobblestone.json") as object_file:
            atlas_data = json.load(object_file)

        embed_list = []
        for pages in atlas_data["pages"]:
            item_tab = discord.Embed(title=pages["title"], description=atlas_data["summary_description"], color=0xdc6565)
            item_tab.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            item_tab.set_thumbnail(url=pages["thumbnail"])
            item_tab.set_footer(text="Atlas from Stella Bot by Over#6203\nClick on the reactions to navigate menus.")
            for field in pages["fields"]:
                item_tab.add_field(name=field["field_title"],value=field["field_description"],inline=False)
            embed_list.append(item_tab.copy())

        output = await ctx.reply(embed=embed_list[0])
        await output.add_reaction("◀️")
        await output.add_reaction("▶️")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        tabs = atlas_data["tabs"]
        current_tab = 1

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)

                if str(reaction) == "▶️" and current_tab != tabs:
                    current_tab += 1
                    await output.edit(embed=embed_list[current_tab-1])

                elif str(reaction) == "◀️" and current_tab > 1:
                    current_tab -= 1
                    await output.edit(embed=embed_list[current_tab-1])
                    
                await output.remove_reaction(reaction, user)
            except Exception as e:
                print(e)
                await output.clear_reactions()
                break
def setup(bot):
    bot.add_cog(Atlas(bot))