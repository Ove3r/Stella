import requests
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
