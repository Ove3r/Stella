import discord
from discord.ext import commands
from helpers import key
def get_prefix(bot,message):
    prefixes = ['stella ','/sb ','/Sb ', 'Stella ','rw ']
    return commands.when_mentioned_or(*prefixes)(bot, message)

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=get_prefix, intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user} in {len(bot.guilds)} servers.")
    member_count = 0
    for server in bot.guilds:
        print(f"{server} ({'{:,}'.format(len(server.members))}) owned by {server.owner}")
        member_count += len(server.members)
    print(f"Total Member Count: {'{:,}'.format(member_count)}")
    await bot.change_presence(activity=discord.Game(name=" Stella Bot Rewrite"))

@bot.command(name="help",
    brief="Returns this menu",
    help=(
    "**stella help**\n"
    "Recursion."
    )
)
async def help(ctx,args=None):
    help_embed=discord.Embed(title="Help", description="Report Bugs [Here](https://github.com/Ove3r/Stella/issues)", color=0xdc6565)
    help_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    help_embed.set_footer(text="Stella Bot by Over#6203")

    command_list = [x for x in bot.commands if not x.hidden]
    def sortCommands(value):
        return value.name
    command_list.sort(key=sortCommands)
    command_names_list = [x.name for x in command_list]
    if not args:
        help_embed.add_field(name="Command Prefixes",value="`stella` `sb` `/sb`",inline=False)
        help_embed.add_field(name="Commands List:",value="```"+"\n".join(['{:>2}. {:<16}{}'.format(str(i+1),x.name,x.brief) for i,x in enumerate(command_list)])+"```",inline=False)
        help_embed.add_field(name="Details",value="Type `stella help <command name>` for more details about each command.",inline=False)
        help_embed.add_field(name="Latest Update",value="Latest Update: [1.0](https://github.com/Ove3r/Stella/blob/main/Documentation/Updates/1.0.md).\nSource Code: [GitHub](https://github.com/Ove3r/Stella)\n[Invite Link](https://tinyurl.com/stellabot)",inline=False)
        await ctx.reply("A list of all commands has been sent to you!")
    elif args in command_names_list:
        help_embed.add_field(name="\u200b",value=bot.get_command(args).help)
    else:
        help_embed.add_field(name="Unknown Command",value="For a list of commands type `stella help`")
    await ctx.author.send(embed=help_embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
        await ctx.send(f"This command is on cooldown for {ctx.author.display_name}. Try again later.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('MissingRequiredArgument Error. `stella help` for more info.')
    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("Unknown Command. `stella help` for a list of commands.")
    else:
        await ctx.send("An error is being ignored. If you believe this is a bug contact Over#6203.")

modules = [
    "loops",
    "player",
    "auctions",
    "trackers",
    "bz",
    "events",
    "guilds",
    "skyborn",
    "pets"
]

for module in modules:
    bot.load_extension(f"cogs.{module}")

bot.run(key.TOKEN)
