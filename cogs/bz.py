import discord
from discord.ext import commands
from helpers.bazaar import *


class Bazaar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bz")
    async def get_bz_item(self, ctx, *, item):
        try:
            name = productName(item)
        except ItemNotFound:
            embed=discord.Embed(title="Error ◆ ItemNotFound", description=f"Item `{item}` not found.", color=0xdc6565)
            embed.set_footer(text=f"Stella Bot by Over#6203 ")
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)
            return
        message = quickInfo(name)
        if (name=="INK_SACK:3"):
            name = "COCOA_BEANS"
        if (name=="INK_SACK:4"):
            name = "LAPIS_LAZULI"
        if (name=="LOG"):
            name = "OAK_LOG"
        if (name=="LOG:1"):
            name = "SPRUCE_LOG"
        if (name=="LOG:2"):
            name = "BIRCH_LOG"
        if (name=="LOG_2:1"):
            name = "DARK_OAK_LOG"
        if (name=="LOG_2"):
            name = "ACACIA_LOG"
        if (name=="LOG:3"):
            name = "JUNGLE_LOG"
        if (name=="RAW_FISH:1"):
            name ="SALMON"
        if (name=="RAW_FISH:2"):
            name = "CLOWNFISH"
        if (name=="RAW_FISH:3"):
            name = "PUFFERFISH"

        embed=discord.Embed(title="Bazaar", description=item, color=0xdc6565)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Stella Bot by Over#6203")
        embed.add_field(name="Quick Info", value=message, inline=False)
        try:
            file = discord.File(f"data/bzimages/{name}.png", filename="image.png")
            embed.set_thumbnail(url="attachment://image.png")
            await ctx.reply(embed=embed,file=file)
        except:
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/hypixel-skyblock/images/c/c8/Bazaar.png/revision/latest?cb=20200729000145")
            await ctx.reply(embed=embed)




def setup(bot):
    bot.add_cog(Bazaar(bot))
