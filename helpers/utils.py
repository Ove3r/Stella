import requests
import helpers.key
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
