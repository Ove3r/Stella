import discord
from discord.ext import commands
from helpers import key
import traceback
import sys
from helpers.errors import *

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

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"This command is on cooldown for {ctx.author.display_name}. Try again later.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('MissingRequiredArgument Error. `stella help` for more info.')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown Command. `stella help` for a list of commands.")
    elif isinstance(error, commands.CommandInvokeError):
        if isinstance(error.original, discord.Forbidden):
            messages = {
                50003: "This cannot be done in a DM Channel.",
                50013: "Missing Permissions (Reactions or Message Related Permissions)."
            }

            error = error.original
            if error.code in messages:
                await ctx.send(messages[error.code])
            else:
                await ctx.send(f"CommandInvokeError {error.text}")  
        elif isinstance(error.original, APIResponseError):
            await ctx.reply(f"API Error. Web Code: `{error.original.code}`.")
        elif isinstance(error.original, NoProfileError):
            await ctx.reply(f"Player `{error.original.name}` has no Skyblock Profiles.")
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
    "atlas",
    "help",
    "minions"
]

for module in modules:
    bot.load_extension(f"cogs.{module}")

bot.run(key.TOKEN)
