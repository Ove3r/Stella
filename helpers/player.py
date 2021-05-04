import requests, time
from helpers import key
from helpers.errors import *
from helpers.utils import *
import matplotlib.pyplot as plt
import numpy as np
from constants import constants_fishing
from constants.constants_minions import *
#Player Attributes: name, uuid, fruit, profile_id, player_data
class Player:
    def __init__(self,name,profile=None):
        self.API_KEY = key.API_KEY
        self.uuid = getUUID(name)
        self.name = getName(self.uuid)
        self.profile_list = []
        self.guild = getGuild(self.uuid)

        # Network Rank
        try:
            self.rank = get_player_network_rank(self.uuid)
        except:
            self.rank = "None"

        # If a profile argument is given.
        data = requests.get(f"https://api.hypixel.net/skyblock/profiles?key={self.API_KEY}&uuid={self.uuid}")
        if data.status_code != 200:
            raise APIResponseError(code=data.status_code)

        data = data.json()
        if not data["profiles"]:
            raise NoProfileError(self.name)

        for entry in data["profiles"]:
            self.profile_list.append(entry["cute_name"])

        if profile:
            for entry in data["profiles"]:
                if profile.lower() == entry.get("cute_name").lower():
                    self.fruit = entry["cute_name"]
                    self.profile_id = entry["profile_id"]
                    self.player_data = entry["members"][self.uuid]
                    break
            if not hasattr(self, "fruit"):
               raise ProfileNotFound

        # If no profile argument is given, fetches most recent profile.
        else:
            if len(data) > 1:
                initial = data["profiles"][0]["members"][self.uuid].get("last_save", 0)
                for entry in data["profiles"]:
                    if entry["members"][self.uuid].get("last_save", 0) >= initial:
                        initial = entry["members"][self.uuid].get("last_save", 0)
                        self.fruit = entry["cute_name"]
                        self.profile_id = entry["profile_id"]
                        self.player_data = entry["members"][self.uuid]
            else:
                self.fruit = data["profiles"][0]["cute_name"]
                self.profile_id = data["profiles"][0]["members"]["profile_id"]
                self.player_data = data["profiles"][0]["members"][self.uuid]

        # API Check
        set1 = set(self.player_data)
        set2 = set(["experience_skill_combat","experience_skill_mining","experience_skill_alchemy","experience_skill_farming","experience_skill_enchanting","experience_skill_fishing","experience_skill_foraging"])
        if set1.intersection(set2):
            self.api_enabled = True
        else:
            self.api_enabled = False

        # Gets the minions related data for a player
        self.get_minions()

    def get_player_summary(self):
        # Slayers
        slayer_data = self.player_data.get("slayer_bosses")
        self.xp_zombie = slayer_data.get("zombie").get("xp", 0)
        self.lvl_zombie = skill_xp_to_level(self.xp_zombie, xp_table="zombie")
        self.xp_spider = slayer_data.get("spider").get("xp", 0)
        self.lvl_spider = skill_xp_to_level(self.xp_spider, xp_table="spider")
        self.xp_wolf = slayer_data.get("wolf").get("xp", 0)
        self.lvl_wolf = skill_xp_to_level(self.xp_wolf, xp_table="wolf")

        # Cata
        dungeons_data = self.player_data.get("dungeons")

        self.xp_cata = round(dungeons_data.get("dungeon_types").get("catacombs").get("experience", 0))
        self.lvl_cata = skill_xp_to_level(self.xp_cata, xp_table="cata")

        # Dungeons Classes
        dungeons_data = dungeons_data.get("player_classes")

        self.xp_healer = round(dungeons_data.get("healer").get("experience", 0))
        self.lvl_healer = skill_xp_to_level(self.xp_healer, xp_table="cata")
        self.xp_mage = round(dungeons_data.get("mage").get("experience", 0))
        self.lvl_mage = skill_xp_to_level(self.xp_mage, xp_table="cata")
        self.xp_berserk = round(dungeons_data.get("berserk").get("experience", 0))
        self.lvl_berserk = skill_xp_to_level(self.xp_berserk, xp_table="cata")
        self.xp_archer = round(dungeons_data.get("archer").get("experience", 0))
        self.lvl_archer = skill_xp_to_level(self.xp_archer, xp_table="cata")
        self.xp_tank = round(dungeons_data.get("tank").get("experience", 0))
        self.lvl_tank = skill_xp_to_level(self.xp_tank, xp_table="cata")
        
        # Skills
        if self.api_enabled:
            self.xp_farming = round(self.player_data.get("experience_skill_farming",0))
            self.lvl_farming = skill_xp_to_level(self.xp_farming, 60)
            self.xp_mining = round(self.player_data.get("experience_skill_mining",0))
            self.lvl_mining = skill_xp_to_level(self.xp_mining, 60)
            self.xp_combat = round(self.player_data.get("experience_skill_combat",0))
            self.lvl_combat = skill_xp_to_level(self.xp_combat,60)
            self.xp_foraging = round(self.player_data.get("experience_skill_foraging",0))
            self.lvl_foraging = skill_xp_to_level(self.xp_foraging)
            self.xp_fishing = round(self.player_data.get("experience_skill_fishing",0))
            self.lvl_fishing = skill_xp_to_level(self.xp_fishing)   
            self.xp_enchanting = round(self.player_data.get("experience_skill_enchanting",0))
            self.lvl_enchanting = skill_xp_to_level(self.xp_enchanting, 60) 
            self.xp_alchemy = round(self.player_data.get("experience_skill_alchemy",0))
            self.lvl_alchemy = skill_xp_to_level(self.xp_alchemy)         
            self.xp_taming = round(self.player_data.get("experience_skill_taming",0))
            self.lvl_taming = skill_xp_to_level(self.xp_taming)

            self.skill_xp_list = [self.xp_farming, self.xp_mining, self.xp_combat, self.xp_foraging, self.xp_fishing, self.xp_enchanting, self.xp_alchemy, self.xp_taming]
            self.total_xp = sum(self.skill_xp_list)

        else:
            data = requests.get(f"https://api.hypixel.net/player?key={self.API_KEY}&uuid={self.uuid}").json()["player"]["achievements"]
            self.lvl_farming = min(data.get("skyblock_harvester",0),60)
            self.lvl_mining = min(data.get("skyblock_excavator",0),60)
            self.lvl_combat = min(data.get("skyblock_combat",0),60)      
            self.lvl_foraging = min(data.get("skyblock_gatherer",0),50)       
            self.lvl_fishing = min(data.get("skyblock_angler",0),50)  
            self.lvl_enchanting = min(data.get("skyblock_augmentation",0),60) 
            self.lvl_alchemy = min(data.get("skyblock_concoctor",0),50)
            self.lvl_taming = min(data.get("skyblock_domesticator",0),50)

        self.skill_lvl_list = [self.lvl_farming, self.lvl_mining, self.lvl_combat, self.lvl_foraging, self.lvl_fishing, self.lvl_enchanting, self.lvl_alchemy, self.lvl_taming]
        self.skill_average = sum(self.skill_lvl_list)/len(self.skill_lvl_list)

    def get_player_xp_pie(self):
        if self.api_enabled:
            skill_labels = ["Farming","Mining","Combat","Foraging","Fishing","Enchanting","Alchemy","Taming"]
            skill_colors = ["#7CFC00","#708090","#ff4c4c","#228B22","#00FFFF","#EE82EE","#FFFF00","#F9DED7"]

            explode = np.zeros(len(self.skill_xp_list))
            explode[np.array(self.skill_xp_list).argmax()] = 0.1
            plt.pie(self.skill_xp_list, labels=skill_labels, colors=skill_colors, explode = explode, autopct='%1.1f%%', shadow=True, startangle=45)
            plt.axis('equal')
            plt.title(f"Skill Experience Distribution for {self.name}\n")
            plt.figtext(0.95, 0.05, f"Total Experience: {'{:,}'.format(self.total_xp)}", horizontalalignment='right')
            plt.figtext(0.05, 0.05, "Stella Bot by Over#6203", horizontalalignment='left')
            plt.savefig(f"data/pie/{self.name}.png")
            plt.close()
            return f"data/pie/{self.name}.png"
        else:
            raise DisabledAPI

    def get_skills_message(self):
        if self.api_enabled:
            self.skills_message = (
            f"<:golden_hoe:801205315806167050>**Farming:** {self.lvl_farming} ⮕ ({'{:,}'.format(self.xp_farming)})\n"
            f"<:stone_pickaxe:810604855726571545>**Mining:** {self.lvl_mining} ⮕ ({'{:,}'.format(self.xp_mining)})\n"
            f"<:stone_sword:810605120752058408>**Combat: ** {self.lvl_combat} ⮕ ({'{:,}'.format(self.xp_combat)})\n"
            f"<:jungle_sapling:810605504934051892>**Foraging: ** {self.lvl_foraging} ⮕ ({'{:,}'.format(self.xp_foraging)})\n"
            f"<:fishing:801090235542929448>**Fishing: ** {self.lvl_fishing} ⮕ ({'{:,}'.format(self.xp_fishing)})\n"
            f"<:enchanting_table:810605765982683166>**Enchanting: ** {self.lvl_enchanting} ⮕ ({'{:,}'.format(self.xp_enchanting)})\n"
            f"<:brewing_stand:810605985336000512>**Alchemy: ** {self.lvl_alchemy} ⮕ ({'{:,}'.format(self.xp_alchemy)})\n"
            f"<:spawn_egg:810606172997812258>**Taming: ** {self.lvl_taming} ⮕ ({'{:,}'.format(self.xp_taming)})\n"
            )
        else:
            self.skills_message = (
            f"<:golden_hoe:801205315806167050>**Farming:** {self.lvl_farming}\n"
            f"<:stone_pickaxe:810604855726571545>**Mining:** {self.lvl_mining}\n"
            f"<:stone_sword:810605120752058408>**Combat: ** {self.lvl_combat}\n"
            f"<:jungle_sapling:810605504934051892>**Foraging: ** {self.lvl_foraging}\n"
            f"<:fishing:801090235542929448>**Fishing: ** {self.lvl_fishing}\n"
            f"<:enchanting_table:810605765982683166>**Enchanting: ** {self.lvl_enchanting}\n"
            f"<:brewing_stand:810605985336000512>**Alchemy: ** {self.lvl_alchemy}\n"
            f"<:spawn_egg:810606172997812258>**Taming: ** {self.lvl_taming}\n"
            )

        return self.skills_message

    def get_slayer_dungeon_message(self):
        self.slayer_message = (
        f"<:revenant:810606609095983114>**Revenant:** {self.lvl_zombie} ⮕ ({'{:,}'.format(self.xp_zombie)})\n"
        f"<:tarantula:810606741023621151>**Tarantula:** {self.lvl_spider} ⮕ ({'{:,}'.format(self.xp_spider)})\n"
        f"<:sven:810606857378201630>**Sven:** {self.lvl_wolf} ⮕ ({'{:,}'.format(self.xp_wolf)})\n"
        )

        self.dungeon_message = (
        f"<:wither_skull:810607234568552459>**Catacombs:** {self.lvl_cata} ⮕ ({'{:,}'.format(self.xp_cata)})\n"
        f"<:splash_heal:810607537488396308>**Healer:** {self.lvl_healer} ⮕ ({'{:,}'.format(self.xp_healer)})\n"
        f"<:blaze_rod:810607718527926272>**Mage:** {self.lvl_mage} ⮕ ({'{:,}'.format(self.xp_mage)})\n"
        f"<:iron_sword:810607869656432690>**Berserker:** {self.lvl_berserk} ⮕ ({'{:,}'.format(self.xp_berserk)})\n"
        f"<:bow:810607983507406939>**Archer:** {self.lvl_archer} ⮕ ({'{:,}'.format(self.xp_archer)})\n"
        f"<:leather_chestplate:810608291083190352>**Tank:** {self.lvl_tank} ⮕ ({'{:,}'.format(self.xp_tank)})\n"
        )

        return self.slayer_message, self.dungeon_message

    def get_jacob_summary(self):
        recent_contests = ""
        recorded = 0
        for contest in reversed(self.player_data["jacob2"]["contests"]):
            if recorded >= 3:
                break
            else:
                try:
                    if self.player_data["jacob2"]["contests"][contest]["claimed_rewards"]:
                        recent_contests += (
                        f"**{contest}**\n"
                        f"Collected: {self.player_data['jacob2']['contests'][contest]['collected']}\n"
                        f"Contest Position: {self.player_data['jacob2']['contests'][contest]['claimed_position'] + 1}\n"
                        f"Contest Participants: {self.player_data['jacob2']['contests'][contest]['claimed_participants']}\n"
                        "\n"
                        )
                    recorded += 1
                except:
                    pass
        self.jacob_summary = recent_contests
        if self.jacob_summary == "":
            self.jacob_summary = "No Contests"

        perks = "**Medal Inventory**\n"
        medals = ["Bronze","Silver","Gold"]
        for tier in medals:
            try:
                perks += f"{tier}: {self.player_data['jacob2']['medals_inv'][tier.lower()]}\n"
            except:
                pass
        try:
            perks += f"\n\n**Anita Perk Bonus: ** {self.player_data['jacob2']['perks']['double_drops'] * 2}%\n"
        except:
            perks += "**Anita Perk Bonus: ** 0%\n"
        try:
            perks += f"**Contests Participated: ** {len(self.player_data['jacob2']['contests'])}\n"
        except:
            perks += "**Contests Participated: ** 0\n"
        self.jacob_perks = perks
        
        return self.jacob_summary

    def get_fishing_stats(self):
        self.fishing_stats = constants_fishing.FISHING_STATS()
        for entry in self.fishing_stats:
            for names in entry["api_name"]:
                try:
                    entry["count"] += self.player_data["stats"][names]
                except:
                    pass
        self.fishing_messages = {
            "Standard Sea Creatures" : "",
            "Spooky Sea Creatures" : "",
            "Winter Sea Creatures" : "",
            "Marina Sharks" : ""
        }

        for entry in self.fishing_stats:
            if entry["count"] != 0:
                if entry["category"] == "Standard":
                    self.fishing_messages["Standard Sea Creatures"] += f"{entry['common_name']} : {'{:,}'.format(round(entry['count']))}\n"
                elif entry["category"] == "Spooky":
                    self.fishing_messages["Spooky Sea Creatures"] += f"{entry['common_name']} : {'{:,}'.format(round(entry['count']))}\n"
                elif entry["category"] == "Winter":
                    self.fishing_messages["Winter Sea Creatures"] += f"{entry['common_name']} : {'{:,}'.format(round(entry['count']))}\n"
                elif entry["category"] == "Marina":
                    self.fishing_messages["Marina Sharks"] += f"{entry['common_name']} : {'{:,}'.format(round(entry['count']))}\n"

    # -----
    # Head Function for Player Minions (Initalization for minions related actions)
    # -----
    def get_minions(self):
        self.all_minions = []
        self.members_list = []

        self.profile_data = requests.get(f"https://api.hypixel.net/skyblock/profile?key={key.API_KEY}&profile={self.profile_id}").json()

        community_upgrades = self.profile_data["profile"].get("community_upgrades", {})
        minion_community_upgrades = community_upgrades.get("upgrade_states", {})

        # Profile Upgrades
        self.minion_community_upgrades = 0
        for entry in minion_community_upgrades: 
            if entry["upgrade"] == "minion_slots":
                self.minion_community_upgrades += 1

        # For Unique crafts on the profile
        self.profile_data = self.profile_data["profile"]["members"]
        for member in self.profile_data: 
            self.members_list.append(member)
            minions = self.profile_data[member].get("crafted_generators", [])
            self.all_minions = self.all_minions + list(set(minions) - set(self.all_minions))

        self.unique_minion_count = len(self.all_minions)
        self.__minion_list()
        self.constants = GET_PLAYER_MINION()  # Varies with the player
        self.tiers = GET_MINION_CONSTANTS()  # Constants for calculations
        for entry in self.all_minions:
            last_char_index = entry.rfind("_")
            listing = entry[:last_char_index] + " " + entry[last_char_index + 1:]
            name = listing.split(" ")
            if name[0] in self.constants:
                self.constants[name[0]]["list"].append(int(name[1]))

        for entry in self.constants:
            if len(self.constants[entry]["list"]) == 0:
                self.constants[entry]["list"].append(1)
        self.__get_minion_upgrade_cost()

    # Determines the total unlocked minion slots for a profile
    def __minion_list(self):
        minion_table = [0, 5, 15, 30, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600]
        self.unlocks = 0
        for i, requirement in enumerate(minion_table):
            if self.unique_minion_count >= requirement:
                self.unlocks = i + 5
                index = i
            else:
                break

        self.unlocks += self.minion_community_upgrades

    # Determines all tier up costs for minions
    def __get_minion_upgrade_cost(self):
        self.upgrade_costs = {}
        bazaar_data = requests.get("https://api.hypixel.net/skyblock/bazaar").json()["products"]
        for minion in self.tiers:
            # Gets the tier of minion that the player has
        
            tier = str(max(self.constants[minion]["list"]))
              
            
            cost = 0
            for material in self.tiers[minion]["tiers"][tier]["upgrade"]:
                if material == "COINS":
                    cost += self.tiers[minion]["tiers"][tier]["upgrade"][material]
                # For each item it takes to upgrade the minion to the next tier
                elif len(bazaar_data[material]["buy_summary"]) > 0:
                    cost += (bazaar_data[material]["buy_summary"][0]["pricePerUnit"]) * \
                            self.tiers[minion]["tiers"][tier]["upgrade"][material]
                
                self.upgrade_costs[minion] = round(cost,1)
        
        # Sorts the dictionary
        self.upgrade_costs = sorted(self.upgrade_costs.items(), key=operator.itemgetter(1), reverse=False)
    
    # Function for adding an item to the yeild of minions (Diamond Spreading)
    def modify_tiers_for_an_upgrade(self, item, rate):
        for minion in self.tiers:
            if item in self.tiers[minion]["yield"]:
                self.tiers[minion]["yield"][item] += rate
            else:
                self.tiers[minion]["yield"][item] = rate
    
    # Function for items that modify the quantity of a yield
    def modify_tiers_for_yield_changes(self, rate=1):
        for minion in self.tiers:
            for item in self.tiers[minion]["yield"]:
                self.tiers[minion]["yield"][item] *= rate

    # Per hour profits for all minions
    def get_yield_per_hour(self, modifier=0):
        bazaar_data = requests.get("https://api.hypixel.net/skyblock/bazaar").json()["products"]
        self.minion_profits = {}
        for minion in self.tiers:
            profit = 0
            tier = max(self.constants[minion]["list"])
            speed = self.tiers[minion]["tiers"][str(tier)]["speed"]
            for item in self.tiers[minion]["yield"]:
                if len(bazaar_data[item]["sell_summary"]) > 0:
                    profit += bazaar_data[item]["sell_summary"][0]["pricePerUnit"] * self.tiers[minion]["yield"][item]

            self.minion_profits[minion] = (3600 / (2 * (speed / 1 + modifier))) * profit
        # Sorts the dictionary
        self.minion_profits = sorted(self.minion_profits.items(), key=operator.itemgetter(1), reverse=True)
    
    # Per hour profits for a specific minion
    def get_yield_per_hour_minion(self, minion, modifier=0):
        message = ""
        tier = max(self.constants[minion]["list"])
        speed = self.tiers[minion]["tiers"][str(tier)]["speed"]

        # (3600 / (2 * (speed / 1 + modifier))) * profit
        for item in self.tiers[minion]["yield"]:
            message += f"**{item}** : {round((3600 / (2 * (speed / 1 + modifier))) * self.tiers[minion]['yield'][item])}\n"
        
        return message
        



        
class Guild:
    def __init__(self,guild):
        self.API_KEY = key.API_KEY
        try:
            self.guild_members, self.guild_name, self.guild_master = get_guild_members(guild)
        except GuildNotFound:
            raise GuildNotFound
        self.average_farming = 0
        self.average_mining = 0
        self.average_combat = 0
        self.average_foraging = 0
        self.average_fishing = 0
        self.average_enchanting = 0
        self.average_alchemy = 0
        self.average_taming = 0

    def get_guild_skill_summary(self):
        for member in self.guild_members:
            self.get_member_achievement_average(member)
            if len(self.guild_members) > 70:
                time.sleep(0.15)
        self.average_farming = round(self.average_farming/len(self.guild_members),3)
        self.average_mining = round(self.average_mining/len(self.guild_members),3)
        self.average_combat = round(self.average_combat/len(self.guild_members),3)
        self.average_foraging = round(self.average_foraging/len(self.guild_members),3)
        self.average_fishing = round(self.average_fishing/len(self.guild_members),3)
        self.average_enchanting = round(self.average_enchanting/len(self.guild_members),3)
        self.average_alchemy = round(self.average_alchemy/len(self.guild_members),3)
        self.average_taming = round(self.average_taming/len(self.guild_members),3)
        self.average_list = [self.average_farming,self.average_mining,self.average_combat,self.average_foraging,self.average_fishing,self.average_enchanting,self.average_alchemy,self.average_taming]
        self.average = round(sum(self.average_list)/len(self.average_list),3)

    def get_member_achievement_average(self,uuid):
        while True: #Accounts for Key Throttle
            try:
                data = requests.get(f"https://api.hypixel.net/player?key={self.API_KEY}&uuid={uuid}").json()["player"]["achievements"]
            except:
                time.sleep(1)
                continue
            break
        try:
            self.average_farming += min(data["skyblock_harvester"],60)
        except KeyError:
            self.average_farming += 0
        try:
            self.average_mining += min(data["skyblock_excavator"],60)
        except KeyError:
            self.average_mining += 0
        try:
            self.average_combat += min(data["skyblock_combat"],60)
        except KeyError:
            self.average_combat += 0
        try:
            self.average_foraging += min(data["skyblock_gatherer"],50)
        except KeyError:
            self.average_foraging += 0
        try:
            self.average_fishing += min(data["skyblock_angler"],50)
        except KeyError:
            self.average_fishing += 0
        try:
            self.average_enchanting += min(data["skyblock_augmentation"],60)
        except KeyError:
            self.average_enchanting += 0
        try:
            self.average_alchemy += min(data["skyblock_concoctor"],50)
        except KeyError:
            self.average_alchemy += 0
        try:
            self.average_taming += min(data["skyblock_domesticator"],50)
        except KeyError:
            self.average_taming += 0

    def get_guild_summary_message(self):
        self.get_guild_skill_summary()
        average = f"**Average: ** {self.average}"
        skills = (
        f"**Farming: ** {self.average_farming}\n"
        f"**Mining: ** {self.average_mining}\n"
        f"**Combat: ** {self.average_combat}\n"
        f"**Foraging: ** {self.average_foraging}\n"
        f"**Fishing: ** {self.average_fishing}\n"
        f"**Enchanting: ** {self.average_enchanting}\n"
        f"**Alchemy: ** {self.average_alchemy}\n"
        f"**Taming: ** {self.average_taming}\n"
        )
        return average, skills
