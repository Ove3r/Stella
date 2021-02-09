import helpers.key
import requests

def getName(uuid):
    data = requests.get(f"https://api.mojang.com/user/profiles/{uuid}/names").json()
    return data[-1]["name"]
