import discord
from discord.ext import commands
from helpers import key
import traceback
import sys

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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name= f" {len(bot.commands)} commands from {'{:,}'.format(member_count)} users in {len(bot.guilds)} servers."))

@bot.event
async def on_message(message):
    if "stella" in message.content.lower() and "cute" in message.content.lower():
        print(f"{message.author.display_name} sent a cute message")
        await message.reply(f"{message.author.display_name}'s cuter.")
    await bot.process_commands(message)

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
        help_embed.add_field(name="Latest Update",value="Latest Update: [1.1](https://github.com/Ove3r/Stella/blob/main/Documentation/Updates/1.1.md).\nSource Code: [GitHub](https://github.com/Ove3r/Stella)\n[Invite Link](https://tinyurl.com/stellabot)",inline=False)
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
        with open("error.txt","w") as file:
            traceback.print_exception(type(error), error, error.__traceback__, file=file)
            file.write(f"\nContext Object: {ctx.message}")
            file.write(f"\nCommand Message: {ctx.message.content}")
        
        channel = bot.get_channel(823008000796786689)
       

        await channel.send(f"Command Error Traceback Invoked By: {ctx.author} <@222116366872739843>", file=discord.File("error.txt"))
        await ctx.reply("An error is being ignored and has been logged (also shown below). Over#6203 will get to this eventually!",file=discord.File("error.txt"))
        

modules = [
    "loops",
    "player",
    "auctions",
    "trackers",
    "bz",
    "events",
    "guilds",
    "skyborn",
    "pets",
    "atlas"
]

for module in modules:
    bot.load_extension(f"cogs.{module}")

bot.run(key.TOKEN)
