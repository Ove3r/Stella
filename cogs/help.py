import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help",
    brief="Returns this menu",
    help=(
    "**stella help**\n"
    "Recursion."
    )
)
    async def get_help(self, ctx, args=None):
        command_list = [x for x in self.bot.commands if not x.hidden]
        def sortCommands(value):
            return value.name
        command_list.sort(key=sortCommands)
        command_names_list = [x.name for x in command_list]
        types = ["profile", "tracking", "prices", "other"]
        available_commands = {
            "profile": {
                "ah": "Returns a player's posted auctions.",
                "guild": "Returns guild averages for a guild.",
                "player": "Returns various stats for a player.",
                "status": "Returns the current location of a player.",
                
                "uuid": "Returns the uuid for a player."
            },
            "tracking": {
                "afk": "Begins AFK Tracking for a player.",
                "ahtrack": "Notifies you when one of your auctions sell.",
                "track": "Skills tracking for a player.",
            },
            "prices": {
                "bits": "Gold/Bit for bit shop items.",
                "bz": "Returns stats for a bazaar item.",
                "da": "Prices for Dark Auction items.",
                "floor": "End of dungeon floor loot values.",
                "forge": "Gold/Hour for items that can be forged.",
                "mythos": "Diana related prices.",
                "pets": "Upgrade profits for leveling 1 to 100 pets.",
                "price": "Return auction prices for an item [exact spelling]."         
            },
            "other": {
                "events": "Approximate Event Timers",
                "jacob": "Jacob timers and event crops",
                "reqs": "Skyborn join requirements"
            }
        }

        help_embed=discord.Embed(title="Help", description="Report Bugs [Here](https://github.com/Ove3r/Stella/issues)", color=0xdc6565)
        help_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        help_embed.set_footer(text="Stella Bot by Over#6203")
        if args in available_commands:
            for entry in available_commands[args]:
                help_embed.add_field(name=entry, value=available_commands[args][entry],inline=False)
        elif args in command_names_list:
            help_embed.add_field(name="\u200b",value=self.bot.get_command(args).help)
        else:
            help_embed.add_field(name="profile", value=f"{len(available_commands['profile'])} commands",inline=False)
            help_embed.add_field(name="tracking", value=f"{len(available_commands['tracking'])} commands",inline=False)
            help_embed.add_field(name="prices", value=f"{len(available_commands['prices'])} commands",inline=False)
            help_embed.add_field(name="other", value=f"{len(available_commands['other'])} commands",inline=False)
            help_embed.add_field(name="For list of commands in a category:", value="stella help [category]",inline=False)
        if not isinstance(ctx.channel, discord.DMChannel):
        
            await ctx.reply("A Help Menu menu has been DM'd to you.")
        await ctx.author.send(embed=help_embed)

def setup(bot):
    bot.add_cog(Help(bot))