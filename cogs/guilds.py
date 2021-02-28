import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from helpers.utils import *
from helpers.player import Guild

class Guild_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="guild", aliases=["guilds"],
        brief="Returns Guild Averages",
        help=(
        "**stella guild [guild name]**\n"
        "Returns a summary of a guild's SkyBlock statistics.\n"
        "Notes: \n "
        "• Guild member averages are calculated from the achievements API."
        )
    )
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def get_guild_summary(self, ctx, *, guild):
        print(f"{ctx.author.name} sent guild command in {ctx.guild}")
        try:
            guild = Guild(guild)
        except GuildNotFound:
            await ctx.reply("GuildNotFound Error")
            return

        loading_embed=discord.Embed(title=f"Loading {guild.guild_name} Guild Averages", description="This may take some time. Other commands may be delayed while this command is running.", color=0xdc6565)
        if len(guild.guild_members) > 70:
            loading_embed.add_field(name="Large Guild Warning", value="This guild has more than 70 members, this command may take a longer time to load.")
        loading_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        loading_embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{guild.guild_master}")
        loading_embed.set_footer(text="Stella Bot by Over#6203")
        loading = await ctx.reply(embed=loading_embed)

        average, skills = guild.get_guild_summary_message()

        embed=discord.Embed(title=guild.guild_name, description="Averages are taken from achievements API.", color=0xdc6565)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{guild.guild_master}")
        embed.add_field(name=f"Members: {len(guild.guild_members)}\n**Guild Master: ** `{getName(guild.guild_master)}`",value=average,inline=False)
        embed.add_field(name="\u200b",value=skills,inline=False)
        embed.set_footer(text="Stella Bot by Over#6203")
        await loading.edit(embed=embed)

def setup(bot):
    bot.add_cog(Guild_Commands(bot))
