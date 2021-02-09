import discord
from discord.ext import tasks, commands
import requests, json
from helpers import key

class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




def setup(bot):
    bot.add_cog(Player(bot))
