import discord
from discord.ext.commands import Bot
from discord.ext.commands import cooldown
from discord.ext import commands, tasks
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands import MemberConverter
import requests
import time
import math
import json
from helpers import key

def get_prefix(bot,message):
    prefixes = ['rw ','test ']
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix=get_prefix)

bot.remove_command('help')

#Bot Status
@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}, SUCCESS!')
    await bot.change_presence(activity=discord.Game(name=" Stella Bot Rewrite"))

bot.load_extension("cogs.test")

bot.run(key.TOKEN)
