import discord
from discord.ext import tasks, commands
import requests, json
from helpers import key
from helpers.utils import *
from pymongo import MongoClient
import time

class Loops(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ahLoop.start()
        self.afkLoop.start()
        self.ah_track_loop.start()

    @tasks.loop(seconds=300)
    async def ahLoop(self):
        API_KEY = key.API_KEY
        index = requests.get(f"https://api.hypixel.net/skyblock/auctions?key={key.API_KEY}&page=0").json()["totalPages"]
        database = {"auctions":[]}
        await self.bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = " AH Database Refresh"))
        while index >= 0:
            data = requests.get(f"https://api.hypixel.net/skyblock/auctions?key={key.API_KEY}&page={index}").json().get("auctions",[])
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
        cluster = MongoClient(key.MONGODB_URL)
        db = cluster["stella"]
        collection = db["afk"]

        entries = collection.find({})
        print(entries.count(), "players being afk tracked.")
        for entry in entries:
            
            if get_player_status(entry["uuid"]) != entry["location"]:
                user = self.bot.get_user(int(entry["discord_id"]))
                embed=discord.Embed(title="AFK Tracker", description=f"`{entry['player']}` is no longer on `{entry['location']}`. \n\nTracking for `{entry['player']}` has been removed. \nUse **stella afk `{entry['player']}`** to track again.", color=0xdc6565)
                embed.add_field(name="Tracking Time", value=f"**{ms_to_standard(time.time() - entry['starting_time'])}**")
                embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{entry['uuid']}")
                embed.set_footer(text="Stella Bot by Over#6203")

                collection.delete_one(entry)
                await user.send(embed=embed)
                print(f"Debugging: {user} received an AFK notification.")

    @afkLoop.before_loop
    async def before_afk(self):
        await self.bot.wait_until_ready()
        return

    @tasks.loop(seconds=120)
    async def ah_track_loop(self):
        with open("data/ah_track.json") as ah_track:
            data = json.load(ah_track)
            update = data
            remove_auctions = []
            for entry in data["tracking"]:
                try:
                    data = requests.get(f"https://api.hypixel.net/skyblock/auction?key={key.API_KEY}&uuid={entry['uuid']}").json()["auctions"][0]
                    if (not data["claimed"]) and (data["highest_bid_amount"] != 0):
                        remove_auctions.append(entry)
                        user = self.bot.get_user(entry["discord_user"])
                        await user.send(f"`{getName(entry['auctioneer'])}`'s item: `{entry['item_name']}` sold to `{getName(data['bids'][0]['bidder'])}` for {'{:,}'.format(data['bids'][0]['amount'])}")
                        print(f"Debugging: {user} received an AH notification.")
                except:
                    remove_auctions.append(entry)

            for removal in remove_auctions:
                update["tracking"].remove(removal)
        with open("data/ah_track.json","w") as ah_track:
            ah_track.write(json.dumps(update))

    @ah_track_loop.before_loop
    async def before_track(self):
        await self.bot.wait_until_ready()
        return


def setup(bot):
    bot.add_cog(Loops(bot))
