import discord
import json, time
from discord.ext import commands
from helpers.utils import *
from helpers.key import *
from helpers.player import Player

class Trackers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="status",aliases=["location"],
        brief="Returns the location of a player",
        help=(
        "**stella status [ign]**\n"
        "Returns the current skyblock location of a player.\n"
        "Notes: \n "
        "• If a player argument is not given, the user's discord display name will be used instead."
        )
    )
    async def check_player_location(self, ctx, *name):
        print(f"{ctx.author.name} sent status command in {ctx.guild}")
        if (not name):
            name = ctx.author.display_name
        else:
            name = name[0]
        try:
            uuid = getUUID(name)
        except PlayerNotFound:
            embed=discord.Embed(title="Error ◆ PlayerNotFound", description=f"Player `{name}` not found.", color=0xdc6565)
            embed.set_footer(text=f"Stella Bot by Over#6203 ")
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)
            return
        status = get_player_status(uuid)
        embed=discord.Embed(title=name, description="\u200b", color=0xdc6565)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Stella Bot by Over#6203")
        embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
        if not status:
            embed.add_field(name="**Current Location**",value="Not connected to mc.hypixel.net.")
        elif status == "dynamic":
            embed.add_field(name="**Current Location**",value="A Personal Skyblock Island.")
        else:
            embed.add_field(name="**Current Location**",value=status)
        await ctx.reply(embed=embed)

    @commands.command(name="afk",
        brief="Begins AFK Tracking",
        help=(
        "**stella afk [ign]**\n"
        "Adds a given player to a tracker that will notify you if the player leaves a personal island.\n"
        "Notes: \n "
        "• The tracker does a check once every minute.\n"
        "• If a player argument is not given, the user's discord display name will be used instead."
        )
    )
    async def add_afk(self, ctx, *name):
        print(f"{ctx.author.name} sent afk command in {ctx.guild}")
        if (not name):
            name = ctx.author.display_name
        else:
            name = name[0]
        try:
            uuid = getUUID(name)
        except PlayerNotFound:
            embed=discord.Embed(title="Error ◆ PlayerNotFound", description=f"Player `{name}` not found.", color=0xdc6565)
            embed.set_footer(text=f"Stella Bot by Over#6203 ")
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)
            return

        with open("data/afk.json") as afk_track:
            data = json.load(afk_track)
        with open("data/afk.json","w") as afk_track:
            entry = {
                "player": name,
                "uuid": uuid,
                "discord_id": ctx.author.id
            }
            data["tracking"].append(entry)
            afk_track.write(json.dumps(data))

        embed=discord.Embed(title="AFK Tracker", description=f"I will DM you if `{name}` is no longer on a personal island.", color=0xdc6565)
        embed.set_footer(text="Stella Bot by Over#6203 ◆ AFK Tracker refreshes every minute")
        embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
        await ctx.reply(embed=embed)

    @commands.command(name="ahtrack",
        brief="Tracks your BINs",
        help=(
        "**stella ahtrack [ign]**\n"
        "Starts tracking all BIN auctions for a given player.\n"
        "If an item that is tracked is sold, you will be notified of such.\n"
        "Notes: \n "
        "• The tracker does a check once 2 minutes.\n"
        "• If a player argument is not given, the user's discord display name will be used instead."
        )
    )
    async def ah_tracking(self,ctx, *name):
        print(f"{ctx.author.name} sent ahTrack command in {ctx.guild}")
        if (not name):
            name = ctx.author.display_name
        else:
            name = name[0]
        try:
            uuid = getUUID(name)
        except PlayerNotFound:
            await ctx.reply("PlayerNotFound Error")
            return

        data = requests.get(f"https://api.hypixel.net/skyblock/auction?key={key.API_KEY}&player={uuid}").json()
        addition = []
        items = []
        for entry in data["auctions"]:
            if ('bin' in entry) and (not entry["claimed"]) and (entry["highest_bid_amount"] == 0):
                player_record = {
                    "discord_user": ctx.author.id,
                }
                player_record.update(entry)
                items.append(entry["item_name"])
                addition.append(player_record)
        if len(addition) == 0:
            await ctx.reply("No BIN Auctions available for tracking.")
            return
        with open("data/ah_track.json") as tracking:
            database = json.load(tracking)
        with open("data/ah_track.json","w") as tracking:
            database["tracking"] += addition
            tracking.write(json.dumps(database))
        embed=discord.Embed(title="BIN Tracker", description="Started Tracking These Items", color=0xdc6565)
        embed.set_footer(text="Stella Bot by Over#6203")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        message = ""
        for item in items:
            message += item + "\n"
        embed.add_field(name="Items",value=message)
        await ctx.reply(embed=embed)

    @commands.command(name="track",
        brief="Player Tracking",
        help=(
        "To start and restart tracking type **stella track [ign] [profile]**\n."
        "To see changes type **stella track**\n"
        "Notes: \n "
        "• You can only track one player at a time per discord account.\n"
        )
    )
    async def player_track(self, ctx, *args):
        print(f"{ctx.author.name} sent track command in {ctx.guild}")
        if (not args):
            try:
                with open(f"data/player_track/{ctx.author.id}.json","r") as player_file:
                    saved_data = json.load(player_file)
            except FileNotFoundError:
                await ctx.reply("You're not currently tracking a player. Type `stella help track` for more info. \nIf you were tracking a player before the rewrite of Stella and you would like your data to be migrated, contact Over#6203.")
            uuid = list(saved_data.keys())[0]

            user = Player(getName(uuid),profile=saved_data[uuid]["profile"])
            if not user.api_enabled:
                await ctx.reply("Skill APIs are Disabled")
                return

            saved_data = saved_data[uuid]
            user.get_player_summary()

            skillsMessage = ""
            if round(user.xp_farming - saved_data['skills']['xp_farming']) > 0:
                skillsMessage += f"**Farming:** + {'{:,}'.format(round(user.xp_farming - saved_data['skills']['xp_farming']))} \n"
            if round(user.xp_mining - saved_data['skills']['xp_mining']) > 0:
                skillsMessage += f"**Mining:** + {'{:,}'.format(round(user.xp_mining - saved_data['skills']['xp_mining']))} \n"
            if round(user.xp_combat - saved_data['skills']['xp_combat']) > 0:
                skillsMessage += f"**Combat:** + {'{:,}'.format(round(user.xp_combat - saved_data['skills']['xp_combat']))} \n"
            if round(user.xp_foraging - saved_data['skills']['xp_foraging']) > 0:
                skillsMessage += f"**Foraging:** + {'{:,}'.format(round(user.xp_foraging - saved_data['skills']['xp_foraging']))} \n"
            if round(user.xp_fishing - saved_data['skills']['xp_fishing']) > 0:
                skillsMessage += f"**Fishing:** + {'{:,}'.format(round(user.xp_fishing - saved_data['skills']['xp_fishing']))} \n"
            if round(user.xp_enchanting - saved_data['skills']['xp_enchanting']) > 0:
                skillsMessage += f"**Enchanting:** + {'{:,}'.format(round(user.xp_enchanting - saved_data['skills']['xp_enchanting']))} \n"
            if round(user.xp_alchemy - saved_data['skills']['xp_alchemy']) > 0:
                skillsMessage += f"**Alchemy:** + {'{:,}'.format(round(user.xp_alchemy - saved_data['skills']['xp_alchemy']))} \n"
            if round(user.xp_taming - saved_data['skills']['xp_taming']) > 0:
                skillsMessage += f"**Taming:** + {'{:,}'.format(round(user.xp_taming - saved_data['skills']['xp_taming']))} \n"
            else:
                skillsMessage += "No Skill Changes"

            slayersMessage = ""
            if round(user.xp_zombie - saved_data['slayers']['xp_zombie']) > 0:
                slayersMessage += f"**Revenant:** + {'{:,}'.format(round(user.xp_zombie - saved_data['slayers']['xp_zombie']))} \n"
            if round(user.xp_spider - saved_data['slayers']['xp_spider']) > 0:
                slayersMessage += f"**Tarantula:** + {'{:,}'.format(round(user.xp_spider - saved_data['slayers']['xp_spider']))} \n"
            if round(user.xp_wolf - saved_data['slayers']['xp_wolf']) > 0:
                slayersMessage += f"**Revenants:** + {'{:,}'.format(round(user.xp_wolf - saved_data['slayers']['xp_wolf']))} \n"
            else:
                slayersMessage += "No Slayer Changes"

            dungeonsMessage = ""
            if round(user.xp_cata - saved_data['dungeons']['xp_cata']) > 0:
                dungeonsMessage += f"**Catacombs:** + {'{:,}'.format(round(user.xp_cata - saved_data['dungeons']['xp_cata']))} \n"
            if round(user.xp_healer - saved_data['dungeons']['xp_healer']) > 0:
                dungeonsMessage += f"**Healer:** + {'{:,}'.format(round(user.xp_healer - saved_data['dungeons']['xp_healer']))} \n"
            if round(user.xp_mage - saved_data['dungeons']['xp_mage']) > 0:
                dungeonsMessage += f"**Mage:** + {'{:,}'.format(round(user.xp_mage - saved_data['dungeons']['xp_mage']))} \n"
            if round(user.xp_berserk - saved_data['dungeons']['xp_berserk']) > 0:
                dungeonsMessage += f"**Berserk:** + {'{:,}'.format(round(user.xp_berserk - saved_data['dungeons']['xp_berserk']))} \n"
            if round(user.xp_archer - saved_data['dungeons']['xp_archer']) > 0:
                dungeonsMessage += f"**Archer:** + {'{:,}'.format(round(user.xp_archer - saved_data['dungeons']['xp_archer']))} \n"
            if round(user.xp_tank - saved_data['dungeons']['xp_tank']) > 0:
                dungeonsMessage += f"**Tank:** + {'{:,}'.format(round(user.xp_tank - saved_data['dungeons']['xp_tank']))} \n"
            else:
                dungeonsMessage += "No Dungeon Changes"

            embed=discord.Embed(title=f"Skills Tracking for {user.name}", description=f"Started Tracking {ms_to_standard((time.time()*1000) - saved_data['time'])} ago for profile: {user.fruit}", color=0xdc6565)
            embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{user.uuid}")
            embed.set_footer(text="Stella Bot by Over#6203 ")
            embed.add_field(name="Skills", value=skillsMessage,inline=False)
            embed.add_field(name="Slayers", value=slayersMessage,inline=False)
            embed.add_field(name="Dungeons", value=dungeonsMessage,inline=False)
            await ctx.reply(embed=embed)

        else:
            try:
                user = Player(args[0],profile=args[1])
            except ProfileNotFound:
                await ctx.reply("ProfileNotFound Error")
                return
            except PlayerNotFound:
                await ctx.reply("PlayerNotFound Error")
                return
            except IndexError:
                await ctx.reply("Improper Usage. Type `stella help track` for more info.")
                return
            if not user.api_enabled:
                await ctx.reply("Skill APIs are Disabled")
                return
            user.get_player_summary()
            data = {
                user.uuid:{
                    "skills":{
                        "xp_farming" : user.xp_farming,
                        "xp_mining" : user.xp_mining,
                        "xp_combat" : user.xp_combat,
                        "xp_foraging" : user.xp_foraging,
                        "xp_fishing" : user.xp_fishing,
                        "xp_enchanting" : user.xp_enchanting,
                        "xp_alchemy" : user.xp_alchemy,
                        "xp_taming" : user.xp_taming
                    },
                    "slayers":{
                        "xp_zombie" : user.xp_zombie,
                        "xp_spider" : user.xp_spider,
                        "xp_wolf" : user.xp_wolf,
                    },
                    "dungeons":{
                        "xp_cata" : user.xp_cata,
                        "xp_healer" : user.xp_healer,
                        "xp_mage" : user.xp_mage,
                        "xp_berserk" : user.xp_berserk,
                        "xp_archer" : user.xp_archer,
                        "xp_tank" : user.xp_tank
                    },
                    "time": round(time.time()*1000),
                    "profile" : user.fruit
                }
            }
            with open(f"data/player_track/{ctx.author.id}.json","w") as player_file:
                player_file.write(json.dumps(data))
            embed=discord.Embed(title=f"Skills Tracking for {user.name}", description=f"Started Tracking skills and slayer xp", color=0xdc6565)
            embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{user.uuid}")
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            embed.set_footer(text="Stella Bot by Over#6203 ")
            embed.add_field(name="\u200b",value=f"To check your changes, type \n> `stella track` \nTo change your starting point for tracking, type \n> `stella track {user.name} {user.fruit}`")
            await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Trackers(bot))
