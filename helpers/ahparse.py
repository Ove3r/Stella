import requests, json, time, operator
from helpers import key
from helpers.utils import *

def search_BIN(item):
    with open("data/ah.json") as database:
        data = json.load(database)
    sellers = []
    prices = []
    for entry in data["auctions"]:
        try:
            test = entry["bin"]
        except:
            test = False
        if test and entry["item_name"].lower() == item.lower():
            sellers.append(entry["auctioneer"])
            prices.append(entry["starting_bid"])

    return sellers, prices

def get_dark_auction():
    ender_artifact = []
    wither_artifact = []
    spirit_mask = []
    travel_scroll = []
    protection6 = []
    sharpness6 = []
    power6 = []
    giant_killer6 = []
    growth6 = []
    epic_parrot = []
    legendary_parrot = []
    epic_turtle = []
    legendary_turtle = []
    epic_jellyfish = []
    legendary_jellyfish = []
    sharpness7 = []
    protection7 = []
    growth7 = []
    power7 = []
    giant_killer7 = []
    counter_strike5 = []
    big_brain3 = []
    vicious3 = []
    hegemony_artifact = []
    plasma_nucleus = []
    with open("data/ah.json") as database:
        data = json.load(database)
    for entry in data["auctions"]:
        try:
            test = entry["bin"]
        except:
            test = False
        if test:
            #Serius
            if "Ender Artifact" in entry["extra"]:
                ender_artifact.append(entry["starting_bid"])
            elif "Wither Artifact" in entry["extra"]:
                wither_artifact.append(entry["starting_bid"])
            elif "Spirit Mask" in entry["extra"]:
                spirit_mask.append(entry["starting_bid"])
            elif "Travel Scroll to Dark Auction" in entry["extra"]:
                travel_scroll.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Protection VI\n§7Grants §a+18 §a❈ Defense§7.\n\n§7§7Apply Cost: §391 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                protection6.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Sharpness VI\n§7Increases melee damage dealt by\n§7§a30%§7\n\n§7§7Apply Cost: §391 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                sharpness6.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Power VI\n§7Increases bow damage by §a48%§7.\n\n§7§7Apply Cost: §391 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                power6.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Giant Killer VI\n§7Increases damage dealt by §a0.6%\n§a§7for each percent of extra\n§7health that your target has\n§7above you up to §a30%§7.\n\n§7§7Apply Cost: §391 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                giant_killer6.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Growth VI\n§7Grants §a+90 §c❤ Health§7.\n\n§7§7Apply Cost: §391 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                growth6.append(entry["starting_bid"])
            elif ("Parrot" in entry["extra"]) and (entry["tier"] == "EPIC"):
                epic_parrot.append(entry["starting_bid"])
            elif ("Parrot" in entry["extra"]) and (entry["tier"] == "LEGENDARY"):
                legendary_parrot.append(entry["starting_bid"])
            elif ("Turtle" in entry["extra"]) and (entry["tier"] == "EPIC"):
                epic_turtle.append(entry["starting_bid"])
            elif ("Turtle" in entry["extra"]) and (entry["tier"] == "LEGENDARY"):
                legendary_turtle.append(entry["starting_bid"])
            elif ("Jellyfish" in entry["extra"]) and (entry["tier"] == "EPIC"):
                epic_jellyfish.append(entry["starting_bid"])
            elif ("Jellyfish" in entry["extra"]) and (entry["tier"] == "LEGENDARY"):
                legendary_jellyfish.append(entry["starting_bid"])
            #Scorpius
            elif entry["item_lore"] == "§9Sharpness VII\n§7Increases melee damage dealt by\n§7§a35%§7\n\n§7§7Apply Cost: §3179 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§5§lEPIC":
                sharpness7.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Protection VII\n§7Grants §a+21 §a❈ Defense§7.\n\n§7§7Apply Cost: §3179 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§5§lEPIC":
                protection7.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Growth VII\n§7Grants §a+105 §c❤ Health§7.\n§9Protection VII\n§7Grants §a+21 §a❈ Defense§7.\n\n§7§7Apply Cost: §3236 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§5§lEPIC":
                growth7.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Power VII\n§7Increases bow damage by §a56%§7.\n\n§7§7Apply Cost: §3179 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§5§lEPIC":
                power7.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Giant Killer VII\n§7Increases damage dealt by §a0.7%\n§a§7for each percent of extra\n§7health that your target has\n§7above you up to §a35%§7.\n\n§7§7Apply Cost: §3179 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§5§lEPIC":
                giant_killer7.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Counter-Strike V\n§7Gain §a+10❈ Defense §7for §a7s\n§a§7on the first hit from an\n§7enemy.\n\n§7§7Apply Cost: §391 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§a§lUNCOMMON":
                counter_strike5.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Big Brain III\n§7Grants §b+15✎ Intelligence§7.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                big_brain3.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Vicious III\n§7Grants §c+3⫽ Ferocity§7.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                vicious3.append(entry["starting_bid"])
            elif "Hegemony Artifact" in entry["extra"]:
                hegemony_artifact.append(entry["starting_bid"])
            elif "Plasma Nucleus" in entry["extra"]:
                plasma_nucleus.append(entry["starting_bid"])

    dark_auction = ""
    try:
        dark_auction += f"`Protection 6` : `{'{:,}'.format(min(protection6))}`\n"
    except ValueError:
        pass
    try:
        dark_auction += f"`Growth 6` : `{'{:,}'.format(min(growth6))}`\n"
    except ValueError:
        pass
    try:
        dark_auction += f"`Sharpness 6` : `{'{:,}'.format(min(sharpness6))}`\n"
    except ValueError:
        pass
    try:
        dark_auction += f"`Power 6` : `{'{:,}'.format(min(power6))}`\n"
    except ValueError:
        pass
    try:
        dark_auction += f"`Giant Killer 6` : `{'{:,}'.format(min(giant_killer6))}`\n"
    except ValueError:
        pass
    dark_auction += "\n"
    try:
        dark_auction += f"`Ender Artifact` : `{'{:,}'.format(min(ender_artifact))}`\n"
    except ValueError:
        pass
    try:
        dark_auction += f"`Wither Artifact` : `{'{:,}'.format(min(wither_artifact))}`\n"
    except ValueError:
        pass
    try:
        dark_auction += f"`Travel Scroll to DA` : `{'{:,}'.format(min(travel_scroll))}`\n"
    except ValueError:
        pass
    dark_auction += "\n"
    try:
        dark_auction += f"`Parrot (Epic)` : `{'{:,}'.format(min(epic_parrot))}`\n"
    except ValueError:
        pass
    try:
        dark_auction += f"`Parrot (Legendary)` : `{'{:,}'.format(min(legendary_parrot))}`\n"
    except ValueError:
        pass
    try:
        dark_auction += f"`Turtle (Epic)` : `{'{:,}'.format(min(epic_turtle))}`\n"
    except ValueError:
        pass
    try:
        dark_auction += f"`Turtle (Legendary)` : `{'{:,}'.format(min(legendary_turtle))}`\n"
    except ValueError:
        pass
    try:
        dark_auction += f"`Jellyfish (Epic)` : `{'{:,}'.format(min(epic_jellyfish))}`\n"
    except ValueError:
        pass
    try:
        dark_auction += f"`Jellyfish (Legendary)` : `{'{:,}'.format(min(legendary_jellyfish))}`\n"
    except ValueError:
        pass

    darker_auction = ""
    try:
        darker_auction += f"`Protection 7` : `{'{:,}'.format(min(protection7))}`\n"
    except ValueError:
        pass
    try:
        darker_auction += f"`Growth 7` : `{'{:,}'.format(min(growth7))}`\n"
    except ValueError:
        pass
    try:
        darker_auction += f"`Sharpness 7` : `{'{:,}'.format(min(sharpness7))}`\n"
    except ValueError:
        pass
    try:
        darker_auction += f"`Power 7` : `{'{:,}'.format(min(power7))}`\n"
    except ValueError:
        pass
    try:
        darker_auction += f"`Giant Killer 7` : `{'{:,}'.format(min(giant_killer7))}`\n"
    except ValueError:
        pass
    try:
        darker_auction += f"`Counter-Strike 5` : `{'{:,}'.format(min(counter_strike5))}`\n"
    except ValueError:
        pass
    try:
        darker_auction += f"`Big Brain 3` : `{'{:,}'.format(min(big_brain3))}`\n"
    except ValueError:
        pass
    try:
        darker_auction += f"`Vicious 3` : `{'{:,}'.format(min(vicious3))}`\n"
    except ValueError:
        pass
    darker_auction += "\n"
    try:
        darker_auction += f"`Hegemony Artifact` : `{'{:,}'.format(min(hegemony_artifact))}`\n"
    except ValueError:
        pass
    try:
        darker_auction += f"`Plasma Nucleus` : `{'{:,}'.format(min(plasma_nucleus))}`\n"
    except ValueError:
        pass

    return dark_auction, darker_auction

def parse_player_ah(uuid):
    API_KEY = key.API_KEY
    data = requests.get(f"https://api.hypixel.net/skyblock/auction?key={API_KEY}&player={uuid}").json()

    total = 0
    value = 0
    message = ""
    totalmessage = ""
    #Determines BIN or not BIN
    for entry in data["auctions"]:
        try:
            bin = entry["bin"]
        except KeyError:
            bin = False
        #BIN AH
        if bin == True:
            #Bin and Sold
            if (entry["claimed"] == False and entry["highest_bid_amount"] != 0):
                message += entry["item_name"]
                message += " ~ BIN Sold: "
                message += "{:,}".format(entry["highest_bid_amount"])
                total += int(entry["highest_bid_amount"])
                message += "\n\n"
            #Bin and not Sold
            if (entry["claimed"] == False and entry["highest_bid_amount"] == 0):
                message += entry["item_name"]
                message += " ~ BIN Price: "
                message += "{:,}".format(entry["starting_bid"])
                value += int(entry["starting_bid"])
                message += "\n\n"

        #Not a BIN AH
        if bin == False:
            #Check Duration Expired
            currentTime = int(round(time.time() *  1000))
            if (entry["end"] <= currentTime):
                ended = True
            else:
                ended = False

            #Expired AH With Bids
            if (entry["claimed"] == False and entry["highest_bid_amount"] != 0 and ended == True):
                message += entry["item_name"]
                message += " ~ Ended Bid: "
                message += "{:,}".format(entry["highest_bid_amount"])
                total += int(entry["highest_bid_amount"])
                message += "\n\n"
            #Not Expired AH With Bids
            elif (entry["claimed"] == False and entry["highest_bid_amount"] != 0 and ended == False):
                message += entry["item_name"]
                message += " ~ Current Bid: "
                message += "{:,}".format(entry["highest_bid_amount"])
                total += int(entry["highest_bid_amount"])
                message += "\n\n"
            #Expired AH Without Bids
            elif (entry["claimed"] == False and entry["highest_bid_amount"] == 0 and ended == True):
                message += data["auctions"][x]["item_name"]
                message += " ~ Expired "
                message += "\n\n"
            #Not Expired AH Without Bids
            elif (entry["claimed"] == False and entry["highest_bid_amount"] != 0 and ended == False):
                message += entry["item_name"]
                message += " ~ Starting Bid: "
                message += "{:,}".format(entry["starting_bid"])
                total += int(entry["starting_bid"])
                message += "\n\n"
    if message == "":
        message = "No Items"
    if total > 0:
        totalmessage = "Total Sales: " + "{:,}".format(total) +'\n'
    if value > 0:
        totalmessage += "Unsold: " + "{:,}".format(value) +'\n'
    if total == 0 and value == 0:
        totalmessage = "No Totals"
    return message, totalmessage

def coins_per_bit():
    #God potion
    bits = {}
    godPotionPrices = []
    katFlowerPrices = []
    magmaBucketPrices = []
    plasmaPrices = []
    greatCarrotPrices = []
    ultimateCarrotPrices = []
    greaterPrices = []
    jumboPrices = []
    hologramPrices = []
    builderWandPrices = []
    bitsTalismanPrices = []
    compact = []
    expertise = []
    #Gets AH Data for the specific items
    with open("data/ah.json") as database:
        data = json.load(database)
    for entry in data["auctions"]:
        try:
            test = entry["bin"]
        except:
            test = False
        if test:
            if entry["item_name"].lower() == "god potion":
                godPotionPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "kat flower":
                katFlowerPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "magma bucket":
                magmaBucketPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "plasma bucket":
                plasmaPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "great carrot candy":
                greatCarrotPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "ultimate carrot candy":
                ultimateCarrotPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "greater backpack":
                greaterPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "jumbo backpack":
                jumboPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "hologram":
                hologramPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "builder's wand":
                builderWandPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "bits talisman":
                bitsTalismanPrices.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Compact I\n§7Gain §a1% §7extra Mining exp\n§7with §a0.2% §7chance to drop an\n§7enchanted item.\n§8100 blocks to tier up!\n\n§7§7Apply Cost: §323 Exp Levels\n\n§e▲ §7Compact cannot be combined!\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                compact.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Expertise I\n§7Gain §a2% §7extra Fishing exp\n§7and increases Sea Creatures\n§7spawn chance by §e1%§7.\n§850 kills to tier up!\n\n§7§7Apply Cost: §323 Exp Levels\n\n§e▲ §7Expertise cannot be combined!\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                expertise.append(entry["starting_bid"])

    bzData = requests.get("https://api.hypixel.net/skyblock/bazaar").json()
    #God potion
    try:
        godPotion = ((min(godPotionPrices))/2000)
        bits["God Potion"] = round(godPotion,3)
    except ValueError:
        pass
    #Kat Flower
    try:
        katFlower = ((min(katFlowerPrices))/500)
        bits["Kat Flower"] = round(katFlower,3)
    except ValueError:
        pass
    #Heat Core (Magma Bucket)
    try:
        buyLava = bzData["products"]["ENCHANTED_LAVA_BUCKET"]["quick_status"]["buyPrice"]
        magmaBucketDifference = (min(magmaBucketPrices))-(buyLava*2)
        magmaBucket = magmaBucketDifference/3000
        bits["Heat Core (Magma Bucket)"] = round(magmaBucket,3)
    except ValueError:
        pass
    #Heat Core (Plasma Bucket)
    try:
        plasmaBucket = ((min(plasmaPrices)) - (min(magmaBucketPrices)*2))/3000
        bits["Heat Core (Plasma Bucket)"] = round(plasmaBucket,3)
    except ValueError:
        pass
    #Hyper Catalyst Upgrade
    try:
        buyCata = bzData["products"]["CATALYST"]["quick_status"]["buyPrice"]
        sellHyper = bzData["products"]["HYPER_CATALYST"]["quick_status"]["sellPrice"]
        hyperCata = ((sellHyper*8) - (buyCata*8))/300
        bits["Hyper Catalyst"] = round(hyperCata,3)
    except ValueError:
        pass
    #Ultimate Carrot Candy
    try:
        greatCarrot = min(greatCarrotPrices)
        buyGolden = bzData["products"]["ENCHANTED_GOLDEN_CARROT"]["quick_status"]["buyPrice"]
        superb = (buyGolden*24) + (greatCarrot)
        ultimateCarrot = ((min(ultimateCarrotPrices)*10)-(superb*8))/8000
        bits["Ultimate Carrot Candy Upgrade"] = round(ultimateCarrot,3)
    except ValueError:
        pass
    #Colossal Experience Bottle
    try:
        buyTitantic = bzData["products"]["TITANIC_EXP_BOTTLE"]["quick_status"]["buyPrice"]
        sellColossal = bzData["products"]["COLOSSAL_EXP_BOTTLE"]["quick_status"]["sellPrice"]
        colossalExp = ((sellColossal) - (buyTitantic))/1200
        bits["Colossal Experience Bottle Upgrade"] = round(colossalExp,3)
    except ValueError:
        pass
    #Jumbo Backpack Upgrade
    try:
        jumboUpgrade = ((min(jumboPrices))-(min(greaterPrices)))/4000
        bits["Jumbo Backpack Upgrade"] = round(jumboUpgrade,3)
    except ValueError:
        pass
    #Hologram
    try:
        hologram = (min(hologramPrices))/2000
        bits["Hologram"] = round(hologram,3)
    except ValueError:
        pass
    #Builder's Wand
    try:
        buildersWand = (min(builderWandPrices))/12000
        bits["Builder's Wand"] = round(buildersWand,3)
    except ValueError:
        pass
    #Bits Talisman
    try:
        bitsTalisman = (min(bitsTalismanPrices))/15000
        bits["Bits Talisman"] = round(bitsTalisman,3)
    except ValueError:
        pass
    #Compact
    try:
        compactI = (min(compact))/4000
        bits["Compact I"] = round(compactI,3)
    except ValueError:
        pass
    #Expertise
    try:
        expertiseI = (min(expertise))/4000
        bits["Expertise I"] = round(expertiseI,3)
    except ValueError:
        pass

    sortedDict = sorted(bits.items(), key=operator.itemgetter(1), reverse=True)
    message = ""
    rank = 1
    for entry in sortedDict:
        message += f"{rank}.`{entry[0]}` at `{entry[1]}`\n"
        rank += 1
    return message

def get_forge():
    def costConvert(cost,time):
        #Time must be given in hours
        return round(cost/time)
    forge = {}
    tankPrices = []
    glacitePrices = []
    handlePrices = []
    platePrices = []
    treasurePrices = []
    enginePrices = []
    mithrilPlatePrices = []
    mithrilPickPrices = []
    beaconIPrices = []
    beaconIIPrices = []
    titaniumTalisPrices = []
    diamonitePrices = []
    powerPrices = []
    refinedPickPrices = []
    firstDrillPrices = []
    mithTankPrices = []
    mithEnginePrices = []
    beaconIIIPrices = []
    ringPrices = []
    purePrices = []
    rockPrices = []
    petrifiedPrices = []
    beaconIVPrices = []
    plasmaPrices = []
    secondDrillPrices = []
    omlettePrices = []
    eggPrices = []
    titaniumEnginePrices = []
    titaniumArtPrices = []
    thirdDrillPrices = []
    fourthDrillPrices = []
    fifthDrillPrices = []
    titaniumTankPrices = []
    beaconVPrices = []
    relicPrices = []
    with open("data/ah.json") as database:
        data = json.load(database)
    for entry in data["auctions"]:
        try:
            test = entry["bin"]
        except:
            test = False
        if test:
            if entry["item_name"].lower() == "fuel tank":
                tankPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "glacite jewel":
                glacitePrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "bejeweled handle":
                handlePrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "golden plate":
                platePrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "treasurite":
                treasurePrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "drill engine":
                enginePrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "mithril plate":
                mithrilPlatePrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "mithril pickaxe":
                mithrilPickPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "beacon i":
                beaconIPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "beacon ii":
                beaconIIPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "titanium talisman":
                titaniumTalisPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "diamonite":
                diamonitePrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "power crystal":
                powerPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "refined mithril pickaxe":
                refinedPickPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "Mithril Drill SX-R226".lower():
                firstDrillPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "Mithril-Infused Fuel Tank".lower():
                mithTankPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "Mithril-Plated Drill Engine".lower():
                mithEnginePrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "beacon III".lower():
                beaconIIIPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "titanium ring":
                ringPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "pure mithril":
                purePrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "rock gemstone":
                rockPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "petrified starfall":
                petrifiedPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "beacon iv":
                beaconIVPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "plasma":
                plasmaPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "Mithril Drill SX-R326".lower():
                secondDrillPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "goblin omelette":
                omlettePrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "goblin egg":
                eggPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "Titanium Plated Drill Engine".lower():
                titaniumEnginePrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "titanium artifact":
                titaniumArtPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "Titanium Drill DR-X355".lower():
                thirdDrillPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "Titanium Drill DR-X455".lower():
                fourthDrillPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "Titanium Drill DR-X555".lower():
                fifthDrillPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "Titanium-Infused Fuel Tank".lower():
                titaniumTankPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "beacon V".lower():
                beaconVPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "titanium relic".lower():
                relicPrices.append(entry["starting_bid"])

    bzData = requests.get("https://api.hypixel.net/skyblock/bazaar").json()
    #Refined Diamond
    try:
        diamondBlockBuy = round(bzData["products"]["ENCHANTED_DIAMOND_BLOCK"]["buy_summary"][0]["pricePerUnit"],3)
        refinedDiamondSell = round(bzData["products"]["REFINED_DIAMOND"]["sell_summary"][0]["pricePerUnit"],3)
        refinedDiamond = refinedDiamondSell - (2*diamondBlockBuy)
        refinedDiamond = costConvert(refinedDiamond,8)
        forge["Refined Diamond"] = refinedDiamond
    except:
        pass
    #Refined Mithril
    try:
        mithrilBuy = round(bzData["products"]["MITHRIL_ORE"]["buy_summary"][0]["pricePerUnit"],3)
        refinedMithSell = round(bzData["products"]["REFINED_MITHRIL"]["sell_summary"][0]["pricePerUnit"],3)
        refinedMithril = refinedMithSell - (25600*mithrilBuy)
        refinedMithril = costConvert(refinedMithril,6)
        forge["Refined Mithril"] = refinedMithril
    except:
        pass
    #Refined Titanium
    try:
        titaniumBuy = round(bzData["products"]["TITANIUM_ORE"]["buy_summary"][0]["pricePerUnit"],3)
        refinedTitaniumSell = round(bzData["products"]["REFINED_TITANIUM"]["sell_summary"][0]["pricePerUnit"],3)
        refinedTitanium = refinedTitaniumSell - (2560*titaniumBuy)
        refinedTitanium = costConvert(refinedTitanium,12)
        forge["Refined Titanium"] = refinedTitanium
    except:
        pass
    #Fuel Tank
    try:
        coalBlock = round(bzData["products"]["ENCHANTED_COAL_BLOCK"]["buy_summary"][0]["pricePerUnit"],3)
        tankPrices = min(tankPrices)
        fuelTank = tankPrices - (2*coalBlock)
        fuelTank = costConvert(fuelTank,10)
        forge["Fuel Tank"] = fuelTank
    except:
        pass
    #Bejewled Handle
    try:
        glacitePrices = min(glacitePrices)
        handlePrices = min(handlePrices)
        handle = handlePrices -(3*glacitePrices)
        handle = costConvert(handle,0.5)
        forge["Bejewled Handle"] = handle
    except:
        pass
    #Golden Plate
    try:
        goldBlock = round(bzData["products"]["ENCHANTED_GOLD_BLOCK"]["buy_summary"][0]["pricePerUnit"],3)
        refinedDiamondBuy = round(bzData["products"]["REFINED_DIAMOND"]["buy_summary"][0]["pricePerUnit"],3)
        platePrices = min(platePrices)
        goldenPlate =  platePrices -((2*goldBlock) + (5*glacitePrices) + (refinedDiamondBuy))
        goldenPlate = costConvert(goldenPlate,6)
        forge["Golden Plate"] = goldenPlate
    except:
        pass
    #Drill Engine
    try:
        ironBlock = round(bzData["products"]["ENCHANTED_IRON_BLOCK"]["buy_summary"][0]["pricePerUnit"],3)
        redstoneBlock = round(bzData["products"]["ENCHANTED_REDSTONE_BLOCK"]["buy_summary"][0]["pricePerUnit"],3)
        treasurePrices = min(treasurePrices)
        enginePrices = min(enginePrices)
        drillEngine = enginePrices - ((ironBlock) + (3*redstoneBlock) + (platePrices) + (10*treasurePrices) + (refinedDiamondBuy))
        drillEngine = costConvert(drillEngine,30)
        forge["Drill Engine"] = drillEngine
    except:
        pass
    #Mithril Plate
    try:
        refinedMithrilBuy = round(bzData["products"]["REFINED_MITHRIL"]["buy_summary"][0]["pricePerUnit"],3)
        refinedTitaniumBuy = round(bzData["products"]["REFINED_TITANIUM"]["buy_summary"][0]["pricePerUnit"],3)
        mithrilPlatePrices = min(mithrilPlatePrices)
        mithrilPlate = (mithrilPlatePrices) - ((5*refinedMithrilBuy) + (platePrices) + (ironBlock) + (refinedTitaniumBuy))
        mithrilPlate = costConvert(mithrilPlate,18)
        forge["Mithril Plate"] = mithrilPlate
    except:
        pass
    ###Casting
    casting = {}
    #Mithril Pickaxe
    try:
        enchantedMithril = mithrilBuy*160
        enchantedGoldBar = round(bzData["products"]["ENCHANTED_GOLD"]["buy_summary"][0]["pricePerUnit"],3)
        mithrilPickPrices = min(mithrilPickPrices)
        mithrilPick = (mithrilPickPrices) - ((30*enchantedMithril) + (handlePrices) + (10*enchantedGoldBar))
        mithrilPick = costConvert(mithrilPick,0.75)
        casting["Mithril Pickaxe"] = mithrilPick
    except:
        pass
    #Beacon II
    try:
        beaconIPrices = min(beaconIPrices)
        beaconIIPrices = min(beaconIIPrices)
        beaconII = (beaconIIPrices) - ((beaconIPrices) + (5*refinedMithrilBuy))
        beaconII = costConvert(beaconII,20)
        casting["Beacon II"] = beaconII
    except:
        pass
    #Titanium Talisman
    try:
        titaniumTalisPrices = min(titaniumTalisPrices)
        titaniumTalisman = (titaniumTalisPrices) - (2*refinedTitaniumBuy)
        titaniumTalisman = costConvert(titaniumTalisman,14)
        casting["Titanium Talisman"] = titaniumTalisman
    except:
        pass
    #Diamonite
    try:
        diamonitePrices = min(diamonitePrices)
        diamonite = (diamonitePrices) - (3*refinedDiamondBuy)
        diamonite = costConvert(diamonite,6)
        casting["Diamonite"] = diamonite
    except:
        pass
    #Power Crystal
    try:
        starfallBuy = round(bzData["products"]["STARFALL"]["buy_summary"][0]["pricePerUnit"],3)
        powerPrices = min(powerPrices)
        powerCrystal = (powerPrices) - (256*starfallBuy)
        powerCrystal = costConvert(powerCrystal,2)
        casting["Power Crystal"] = powerCrystal
    except:
        pass
    #Refined Mithril Pickaxe
    try:
        refinedPickPrices = min(refinedPickPrices)
        refinedMithrilPickaxe = refinedPickPrices - (3*refinedMithrilBuy) + (2*handlePrices) + (refinedDiamondBuy) + (30*enchantedGoldBar)
        refinedMithrilPickaxe = costConvert(refinedMithrilPickaxe,22)
        casting["Refined Mithril Pickaxe"] = refinedMithrilPickaxe
    except:
        pass
    #Mithril Drill SX-R226
    try:
        firstDrillPrices = min(firstDrillPrices)
        firstDrill = firstDrillPrices - ((enginePrices) + (3*refinedMithrilBuy) + (tankPrices))
        firstDrill = costConvert(firstDrill,4)
        casting["Mithril Drill SX-R226"] = firstDrill
    except:
        pass
    #Mithril-Infused Fuel Tank
    try:
        mithTankPrices = min(mithTankPrices)
        mithrilFuelTank = mithTankPrices - ((3*mithrilPlatePrices) + (5*tankPrices))
        mithrilFuelTank = costConvert(mithrilFuelTank,10)
        casting["Mithril-Infused Fuel Tank "] = mithrilFuelTank
    except:
        pass
    #Mithril-Plated Drill Engine
    try:
        mithEnginePrices = min(mithEnginePrices)
        mithrilEngine = mithEnginePrices - ((2*enginePrices) + (3*mithrilPlatePrices))
        mithrilEngine = costConvert(mithrilEngine,15)
        casting["Mithril-Plated Drill Engine"] = mithrilEngine
    except:
        pass
    #Beacon III
    try:
        beaconIIIPrices = min(beaconIIIPrices)
        beaconIII = beaconIIPrices - (beaconIIPrices + (10*refinedMithrilBuy))
        beaconIII = costConvert(beaconIII,30)
        casting["Beacon III"] = beaconIII
    except:
        pass
    #Titanium Ring (Special Case)
    try:
        ringPrices = min(ringPrices)
        titaniumRing = ringPrices - (8*refinedTitaniumBuy)
        titaniumRing = costConvert(titaniumRing,34)
        casting["Titanium Ring ◆"] = titaniumRing
    except:
        pass
    #Pure Mithril
    try:
        purePrices = min(purePrices)
        pureMithril = purePrices - (2*refinedMithrilBuy)
        pureMithril = costConvert(pureMithril,12)
        casting["Pure Mithril"] = pureMithril
    except:
        pass
    #Rock Gemstone
    try:
        rockPrices = min(rockPrices)
        enchantedCobbleBuy = round(bzData["products"]["ENCHANTED_COBBLESTONE"]["buy_summary"][0]["pricePerUnit"],3)
        rockGemstone = rockPrices - ((64*treasurePrices) + (128*enchantedCobbleBuy))
        rockGemstone = costConvert(rockGemstone,22)
        casting["Rock Gemstone"] = rockGemstone
    except:
        pass
    #Petrified Starfall
    try:
        petrifiedPrices = min(petrifiedPrices)
        petrifiedStarfall = petrifiedPrices - (512*starfallBuy)
        petrifiedStarfall = costConvert(petrifiedStarfall, 14)
        casting["Petrified Starfall"] = petrifiedStarfall
    except:
        pass
    #Beacon IV
    try:
        plasmaPrices = min(plasmaPrices)
        beaconIVPrices = min(beaconIVPrices)
        beaconIV = (beaconIVPrices -(beaconIIIPrices) + (20*refinedMithrilBuy) + (plasmaPrices))
        beaconIV = costConvert(beaconIV, 40)
        casting["Beacon IV"] = beaconIV
    except:
        pass
    #Mithril Drill SX-R326
    try:
        secondDrillPrices = min(secondDrillPrices)
        secondDrill = secondDrillPrices - ((firstDrillPrices) + (10*platePrices) + (2*mithrilPlatePrices))
        secondDrill = costConvert(secondDrill,30)
        casting["Mithril Drill SX-R326"] = secondDrill
    except:
        pass
    #Goblin Omlette
    try:
        omlettePrices = min(omlettePrices)
        eggPrices = min(eggPrices)
        goblinOmlette = omlettePrices - (99*eggPrices)
        goblinOmlette = costConvert(goblinOmlette,18)
        casting["Goblin Omelette"] = goblinOmlette
    except:
        pass
    #Titanium Plated Drill Engine
    try:
        titaniumEnginePrices = min(titaniumEnginePrices)
        titaniumEngine = titaniumEnginePrices - ((10*enginePrices) + (5*plasmaPrices) + (4*mithrilPlatePrices) + (5*refinedTitaniumBuy))
        titaniumEngine = costConvert(titaniumEngine,40)
        casting["Titanium Plated Drill Engine"] = titaniumEngine
    except ValueError:
        pass
    #Titanium Artifact
    try:
        titaniumArtPrices = min(titaniumArtPrices)
        artifact = titaniumArtPrices - (ringPrices + (12*refinedTitaniumBuy))
        artifact = costConvert(artifact,36)
        casting["Titanium Artifact"] = artifact
    except:
        pass
    #Titanium Drill DR-X355
    try:
        thirdDrillPrices = min(thirdDrillPrices)
        thirdDrill = thirdDrillPrices - ((enginePrices) + (tankPrices) + (6*platePrices) + (10*refinedTitaniumBuy) + (10*refinedMithrilBuy))
        thirdDrill = costConvert(thirdDrill,64)
        casting["Titanium Drill DR-X355"] = thirdDrill
    except:
        pass
    #Titanium Drill DR-X455
    try:
        fourthDrillPrices = min(fourthDrillPrices)
        fourthDrill = fourthDrillPrices - ((thirdDrillPrices) + (10*refinedDiamondBuy) + (16*refinedTitaniumBuy) + (6*mithrilPlatePrices))
        fourthDrill = costConvert(fourthDrill,1/120)
        casting["Titanium Drill DR-X455"] = fourthDrill
    except:
        pass
    #Titanium Drill DR-X555
    try:
        fifthDrillPrices = min(fifthDrillPrices)
        fifthDrill = fifthDrillPrices - ((fourthDrillPrices) + (20*refinedDiamondBuy) + (32*refinedTitaniumBuy) + (2*ironBlock) + (15*mithrilPlatePrices) + (20*plasmaPrices))
        fifthDrill = costConvert(fifthDrill,1/120)
        casting["Titanium Drill DR-X555"] = fifthDrill
    except:
        pass
    #Titanium-Infused Fuel Tank
    try:
        titaniumTankPrices = min(titaniumTankPrices)
        titaniumTank = titaniumTankPrices - ((10*refinedTitaniumBuy) + (10*refinedDiamondBuy) + (10*refinedMithrilBuy) + (10*tankPrices))
        titaniumTank = costConvert(titaniumTank,25)
        casting["Titanium-Infused Fuel Tank"] = titaniumTank
    except:
        pass
    #Beacon V
    try:
        beaconVPrices = min(beaconVPrices)
        beaconV = beaconVPrices - (beaconIVPrices + (40*refinedMithrilBuy) + (5*plasmaPrices))
        beaconV = costConvert(beaconV,50)
        casting["Beacon V"] = beaconV
    except:
        pass
    #Titanium Relic
    try:
        relicPrices = min(relicPrices)
        relic = relicPrices - (titaniumArtPrices + (20*refinedTitaniumBuy))
        relic = costConvert(relic,72)
        casting["Titanium Relic"] = relic
    except:
        pass

    sortedForge = sorted(forge.items(), key=operator.itemgetter(1), reverse=True)
    sortedCasting = sorted(casting.items(), key=operator.itemgetter(1), reverse=True)
    forgeMessage = ""
    castingMessage = ""
    forgeRank = 1
    castRank = 1
    for entry in sortedForge:
        forgeMessage += f"{forgeRank}.`{entry[0]}` at `{'{:,}'.format(entry[1])}`\n"
        forgeRank += 1
    for entry in sortedCasting:
        castingMessage += f"{castRank}.`{entry[0]}` at `{'{:,}'.format(entry[1])}`\n"
        castRank += 1

    return forgeMessage, castingMessage
