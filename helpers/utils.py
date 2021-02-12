import requests, operator, math
from helpers import key
from helpers.errors import *

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

def get_player_status(uuid):
    API_KEY = key.API_KEY
    data = requests.get(f"https://api.hypixel.net/status?key={API_KEY}&uuid={uuid}").json()
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

def skill_xp_to_level(xp, max=50):
    xp_table = [50,175,375,675,1175,1925,2925,4425,6425,9925,14925,22425,32425,47425,67425,97425,147425,222425,322425,522425,822425,1222425,1722425,2322425,3022425,3822425,4722425,5722425,6822425,8022425,9322425,10722425,12222425,13822425,15522425,17322425,19222425,21222425,23322425,25522425,27822425,30222425,32722425,35322425,38072425,40972425,44072425,47472425,51172425,55172425,59472425,64072425,68972425,74172425,79672425,85472425,91572425,97972425,104672425,111672425]
    for i, requirement in enumerate(xp_table):
    	if xp >= requirement:
    		level = i + 1
    	else:
    		break
    if level > max:
        level = max
    return level

def highest_lvl(skill, highest):
    if skill > highest:
        return highest
    else:
        return skill
