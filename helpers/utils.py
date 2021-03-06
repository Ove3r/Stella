import requests, operator, math
from helpers import key
from helpers.errors import *
from constants import constants_ranks

def getName(uuid):
    data = requests.get(f"https://api.mojang.com/user/profiles/{uuid}/names").json()
    return data[-1]["name"]

def getUUID(name):
    try:
        data = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
        uuid = data["id"]
        return uuid
    except:
        raise PlayerNotFound

def getGuild(uuid):
    API_KEY = key.API_KEY
    guild_id = requests.get(f"https://api.hypixel.net/findGuild?key={API_KEY}&byUuid={uuid}").json()["guild"]
    if guild_id:
        guild_name = requests.get(f"https://api.hypixel.net/guild?key={API_KEY}&id={guild_id}").json()["guild"]["name"]
        return guild_name
    return guild_id

def get_player_status(uuid):
    API_KEY = key.API_KEY
    
    data = requests.get(f"https://api.hypixel.net/status?key={API_KEY}&uuid={uuid}")
    print(data.status_code, f"code for status check {uuid}")
    data = data.json()
    if not data["session"]["online"]:
        return False
    elif data["session"]["gameType"] != "SKYBLOCK":
        return "Other"
    else:
        return data["session"]["mode"]

def get_calendar_events():
    events = {}
    zoo = requests.get("https://hypixel-api.inventivetalent.org/api/skyblock/zoo/estimate").json()
    zoo = zoo["estimate"]
    events["<:oringo:798246581425930270> Traveling Zoo"] = zoo

    year = requests.get("https://hypixel-api.inventivetalent.org/api/skyblock/newyear/estimate").json()
    year = year["estimate"]
    events["<:newyearcake:798247179139547156> New Year Celebration"] = year

    events["<:snowball:798246888242937876> Season of Jerry"] = year - 6000000

    spooky = requests.get("https://hypixel-api.inventivetalent.org/api/skyblock/spookyFestival/estimate").json()
    spooky = spooky["estimate"]
    events["<:green_candy:798247092657193020> Spooky Festival"] = spooky

    darkAuction = requests.get("https://hypixel-api.inventivetalent.org/api/skyblock/darkauction/estimate").json()
    darkAuction = darkAuction["estimate"]
    events["<:sirius:798248398717059142> Dark Auction"] = darkAuction

    interest = requests.get("https://hypixel-api.inventivetalent.org/api/skyblock/bank/interest/estimate").json()
    interest = interest["estimate"]
    events["<:Enchanted_Gold_Block:798249009868570704> Bank Interest"] = interest

    events = sorted(events.items(),key=operator.itemgetter(1),reverse=False)
    return events

def changeCrops(cropID):
    cropsList = ["<:cactus:796098159863922719> Cactus", "<:carrot:796098312167096420> Carrot", "<:cocoa:796098455394975814> Cocoa Beans", "<:melon:796098570117185556> Melon", "<:mushroom:796098673310171256> Mushroom", "<:wart:796098753294630932> Nether Wart", "<:potato:796098824892448798> Potato", "<:pumpkin:796098901496823819> Pumpkin", "<:cane:796098970107117658> Sugar Cane", "<:wheat:796099047765049365> Wheat"]
    return cropsList[cropID]

def ms_to_standard(ms):
    minutes=math.floor((ms/(1000*60))%60)
    hours=math.floor((ms/(1000*60*60))%24)
    days=math.floor((ms/(1000*60*60*24)))
    timeago = ""
    if days !=0:
        timeago += f"{days} d. "
    if hours != 0:
        timeago += f"{hours} h. "
    if minutes != 0:
        timeago += f"{minutes} m. "
    if (minutes == 0) and (hours == 0):
        timeago += "0 m. "
    return timeago

def skill_xp_to_level(xp, max=50, xp_table="skills"):
    xp_tables = {
        "skills": [50,175,375,675,1175,1925,2925,4425,6425,9925,14925,22425,32425,47425,67425,97425,147425,222425,322425,522425,822425,1222425,1722425,2322425,3022425,3822425,4722425,5722425,6822425,8022425,9322425,10722425,12222425,13822425,15522425,17322425,19222425,21222425,23322425,25522425,27822425,30222425,32722425,35322425,38072425,40972425,44072425,47472425,51172425,55172425,59472425,64072425,68972425,74172425,79672425,85472425,91572425,97972425,104672425,111672425],
        "cata": [50,125,235,395,625,955,1425,2095,3045,4385,6275,8940,12700,17960,25340,35640,50040,70040,97640,135640,188140,259640,356640,488640,668640,911640,1239640,1684640,2284640,3084640,4149640,5559640,7459640,9959640,13259640,17559640,23159640,30359640,39559640,51559640,66559640,85559640,109559640,139559640,177559640,225559640,285559640,360559640,453559640,569809640],
        "zombie": [5,15,200,1000,5000,20000,100000,400000,1000000],
        "spider": [5,25,200,1000,5000,20000,100000,400000,1000000],
        "wolf": [10,30,250,1500,5000,20000,100000,400000,1000000],
        "enderman": [10,30,250,1500,5000,20000,100000,400000,1000000]
    }

    level = 0
    for i, requirement in enumerate(xp_tables[xp_table]):
    	if xp >= requirement:
    		level = i + 1
    	else:
    		break
    if level > max:
        level = max
    return level


def get_guild_members(guild):
    data = requests.get(f"https://api.hypixel.net/guild?name={guild}&key={key.API_KEY}").json()
    if not data["guild"]:
        raise GuildNotFound
    member_list = []
    for members in data["guild"]["members"]:
        member_list.append(members["uuid"])
        if members["rank"] == "Guild Master":
            guild_master = members["uuid"]
    guild_name = data["guild"]["name"]
    return member_list, guild_name, guild_master

def get_player_network_rank(uuid):
    data = requests.get(f"https://api.hypixel.net/player?key={key.API_KEY}&uuid={uuid}").json()["player"]
    ranks = constants_ranks.RANKS
    if "prefix" in data:
        return ranks[data["prefix"]]
    elif "rank" in data:
        return ranks[data["rank"]]
    elif "monthlyPackageRank" in data and data["monthlyPackageRank"] != "NONE":
        return ranks[data["monthlyPackageRank"]]
    elif "newPackageRank" in data:
        return ranks[data["newPackageRank"]]
    else:
        return "None"
