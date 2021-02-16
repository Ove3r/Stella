import discord
from discord.ext import tasks, commands
import requests, json
from helpers import key
from helpers.utils import *

class Loops(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #self.ahLoop.start()
        self.afkLoop.start()

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
        return

    @tasks.loop(seconds=60)
    async def afkLoop(self):
        print("Started AFK Check")
        with open("data/afk.json") as afk_track:
            data = json.load(afk_track)
        with open("data/afk.json","w") as afk_track:
            delete = []
            for entry in data["tracking"]:
                if get_player_status(entry["uuid"]) != "dynamic":
                    user = self.bot.get_user(int(entry["discord_id"]))
                    embed=discord.Embed(title="AFK Tracker", description=f"`{entry['player']}` is no longer on a personal island. \n\nTracking for `{entry['player']}` has been removed. \nUse **stella afk `{entry['player']}`** to track again.", color=0xdc6565)
                    embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{entry['uuid']}")
                    embed.set_footer(text="Stella Bot by Over#6203")
                    delete.append(entry)
                    await user.send(embed=embed)
                    print(f"Debugging: {user} received an AFK notification.")
            for entry in delete:
                data["tracking"].remove(entry)

            afk_track.write(json.dumps(data))
            print("Finished AFK Check")

    @afkLoop.before_loop
    async def before_afk(self):
        await self.bot.wait_until_ready()
        return
        
def setup(bot):
    bot.add_cog(Loops(bot))
