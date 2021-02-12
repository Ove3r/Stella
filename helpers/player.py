import requests
from helpers import key
from helpers.errors import *
from helpers.utils import *
import matplotlib.pyplot as plt
import numpy as np

#Player Attributes: name, uuid, fruit, profile_id, player_data
class Player:
    def __init__(self,name,profile=None):
        API_KEY = key.API_KEY
        self.name = name
        self.uuid = getUUID(name)
        ##If a profile argument is given.
        data = requests.get(f"https://api.hypixel.net/skyblock/profiles?key={API_KEY}&uuid={self.uuid}").json()
        if profile:
            for entry in data["profiles"]:
                if profile.lower() == entry["cute_name"].lower():
                    self.fruit = entry["cute_name"]
                    self.profile_id = entry["profile_id"]
                    self.player_data = entry["members"][self.uuid]
                    break
            if not hasattr(self, "fruit"):
               raise ProfileNotFound

        ##If no profile argument is given, fetches most recent profile.
        else:
            if len(data) > 1:
                initial = data["profiles"][0]["members"][self.uuid]["last_save"]
                for entry in data["profiles"]:
                    if entry["members"][self.uuid]["last_save"] >= initial:
                        initial = entry["members"][self.uuid]["last_save"]
                        self.fruit = entry["cute_name"]
                        self.profile_id = entry["profile_id"]
                        self.player_data = entry["members"][self.uuid]

            else:
                self.fruit = data["profiles"][0]["cute_name"]
                self.profile_id = data["profiles"][0]["members"]["profile_id"]
                self.player_data = data["profiles"][0]["members"][self.uuid]

    def check_skills_API(self):
        set1 = set(self.player_data)
        set2 = set(["experience_skill_combat","experience_skill_mining","experience_skill_alchemy","experience_skill_farming","experience_skill_enchanting","experience_skill_fishing","experience_skill_foraging"])
        if set1.intersection(set2):
            return True
        else:
            return False

    def get_player_summary(self):
        if self.check_skills_API():
            try:
                self.xp_farming = round(self.player_data["experience_skill_farming"])
                self.lvl_farming = skill_xp_to_level(self.xp_farming, 60)
            except KeyError:
                self.xp_farming = 0
                self.lvl_farming = 0
            try:
                self.xp_mining = round(self.player_data["experience_skill_mining"])
                self.lvl_mining = skill_xp_to_level(self.xp_mining, 60)
            except KeyError:
                self.xp_mining = 0
                self.lvl_mining = 0
            try:
                self.xp_combat = round(self.player_data["experience_skill_combat"])
                self.lvl_combat = skill_xp_to_level(self.xp_combat, 50)
            except KeyError:
                self.xp_combat = 0
                self.lvl_combat = 0
            try:
                self.xp_foraging = round(self.player_data["experience_skill_foraging"])
                self.lvl_foraging = skill_xp_to_level(self.xp_foraging, 50)
            except KeyError:
                self.xp_foraging = 0
                self.lvl_foraging = 0
            try:
                self.xp_fishing = round(self.player_data["experience_skill_fishing"])
                self.lvl_fishing = skill_xp_to_level(self.xp_fishing, 50)
            except KeyError:
                self.xp_fishing = 0
            try:
                self.xp_enchanting = round(self.player_data["experience_skill_enchanting"])
                self.lvl_enchanting = skill_xp_to_level(self.xp_enchanting, 60)
            except KeyError:
                self.xp_enchanting = 0
            try:
                self.xp_alchemy = round(self.player_data["experience_skill_alchemy"])
                self.lvl_alchemy = skill_xp_to_level(self.xp_alchemy, 50)
            except KeyError:
                self.xp_alchemy = 0
                self.lvl_alchemy = 0
            try:
                self.xp_taming = round(self.player_data["experience_skill_alchemy"])
                self.lvl_taming = skill_xp_to_level(self.xp_taming, 50)
            except KeyError:
                self.xp_taming = 0
                self.lvl_taming = 0
            self.skill_lvl_list = [self.lvl_farming, self.lvl_mining, self.lvl_combat, self.lvl_foraging, self.lvl_fishing, self.lvl_enchanting, self.lvl_alchemy, self.lvl_taming]
            self.skill_xp_list = [self.xp_farming, self.xp_mining, self.xp_combat, self.xp_foraging, self.xp_fishing, self.xp_enchanting, self.xp_alchemy, self.xp_taming]
            self.skill_average = sum(self.skill_lvl_list)/len(self.skill_lvl_list)

    def get_player_xp_pie(self):
        skill_labels = ["Farming","Mining","Combat","Foraging","Fishing","Enchanting","Alchemy","Taming"]
        skill_colors = ["#7CFC00","#708090","#ff4c4c","#228B22","#00FFFF","#EE82EE","#FFFF00","#F9DED7"]

        explode = np.zeros(len(self.skill_xp_list))
        explode[np.array(self.skill_xp_list).argmax()] = 0.1
        figure, ax = plt.subplots()
        ax.pie(self.skill_xp_list, labels=skill_labels, colors=skill_colors, explode = explode, autopct='%1.1f%%', shadow=True, startangle=45)
        ax.axis('equal')
        plt.title(f"Skill Experience Distribution for {self.name}")
        plt.savefig(f"data/pie/{self.name}.png")
        return f"data/pie/{self.name}.png"


#try:
#    user = Player("Over_",profile="Banana")
#except ProfileNotFound:
#    print("ProfileNotFound Error")
#except PlayerNotFound:
#    print("PlayerNotFound Error")

#user.get_player_summary()
#path = user.get_player_xp_pie()
#print(path)
