import discord
from discord.ext import commands
from helpers import key
def get_prefix(bot,message):
    prefixes = ['rw ','test ']
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix=get_prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}.')
    await bot.change_presence(activity=discord.Game(name=" Stella Bot Rewrite"))

modules = [
    "loops",
    "player",
    "auctions",
    "trackers",
    "bz",
    "events",
]

for module in modules:
    bot.load_extension(f"cogs.{module}")


bot.run(key.TOKEN)
