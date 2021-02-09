import discord
from discord.ext import tasks, commands
import requests, json
from helpers import key

class Loops(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ahLoop.start()

    @tasks.loop(seconds=300)
    async def ahLoop(self):
        API_KEY = key.API_KEY
        index = requests.get(f"https://api.hypixel.net/skyblock/auctions?key={API_KEY}&page=0").json()["totalPages"]
        database = {"auctions":[]}
        await self.bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = " AH Database Refresh"))
        while index >= 0:
            data = requests.get(f"https://api.hypixel.net/skyblock/auctions?key={API_KEY}&page={index}").json()["auctions"]
            database["auctions"][0:0] = data
            index -= 1
        with open("data/ah.json","w") as file:
            file.write(json.dumps(database))
            file.close()
        print(f"{len(database['auctions'])} auctions loaded into database.")
        await self.bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = f" {len(database['auctions'])} AH items."))
    @ahLoop.before_loop
    async def before_ah(self):
        print('Waiting for on_ready to begin loops.')
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(Loops(bot))
