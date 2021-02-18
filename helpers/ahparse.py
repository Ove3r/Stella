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
    raw = {}
    crafted = {}
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
    heatCorePrices = []
    hyperCataItem = []
    ultimateCarrotItem = []
    colossalPrices = []
    jumboItemPrices = []
    cultivating = []
    blockZapper = []
    kismetFlowerPrices = []
    autoPetPrices = []
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
            elif entry["item_name"].lower() == "heat core":
                heatCorePrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "hyper catalyst upgrade":
                hyperCataItem.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "ultimate carrot candy upgrade":
                ultimateCarrotItem.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "colossal experience bottle upgrade":
                colossalPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "jumbo backpack upgrade":
                jumboItemPrices.append(entry["starting_bid"])
            elif entry["item_lore"] == "§9Cultivating I\n§7Gain §a1% §7extra Farming exp\n§7and §6+1☘ Farming Fortune§7.\n§81k crops to tier up!\n\n§e▲ §7Cultivating cannot be combined!\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                cultivating.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "block zapper":
                blockZapper.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "kismet feather":
                kismetFlowerPrices.append(entry["starting_bid"])
            elif entry["item_name"].lower() == "autopet rules 2-pack":
                autoPetPrices.append(entry["starting_bid"])

    bzData = requests.get("https://api.hypixel.net/skyblock/bazaar").json()
    #God potion
    try:
        godPotion = ((min(godPotionPrices))/2000)
        raw["God Potion"] = round(godPotion,3)
    except ValueError:
        pass
    #Kat Flower
    try:
        katFlower = ((min(katFlowerPrices))/500)
        raw["Kat Flower"] = round(katFlower,3)
    except ValueError:
        pass
    #Heat Core (Raw Item)
    try:
        heatCore = min(heatCorePrices)/3000
        raw["Heat Core"] = round(heatCore,3)
    except ValueError:
        pass
    #Heat Core (Magma Bucket)
    try:
        buyLava = bzData["products"]["ENCHANTED_LAVA_BUCKET"]["buy_summary"][0]["pricePerUnit"]
        magmaBucketDifference = (min(magmaBucketPrices))-(buyLava*2)
        magmaBucket = magmaBucketDifference/3000
        crafted["Heat Core (Magma Bucket)"] = round(magmaBucket,3)
    except ValueError:
        pass
    #Heat Core (Plasma Bucket)
    try:
        plasmaBucket = ((min(plasmaPrices)) - (min(magmaBucketPrices)*2))/3000
        crafted["Heat Core (Plasma Bucket)"] = round(plasmaBucket,3)
    except ValueError:
        pass
    #Hyper Catalyst (Raw Item)
    try:
        hyperCataUpgrade = min(hyperCataItem)/300
        raw["Hyper Catalyst Upgrade"] = round(hyperCataUpgrade,3)
    except ValueError:
        pass
    #Hyper Catalyst Upgrade
    try:
        buyCata = bzData["products"]["CATALYST"]["buy_summary"][0]["pricePerUnit"]
        sellHyper = bzData["products"]["HYPER_CATALYST"]["sell_summary"][0]["pricePerUnit"]
        hyperCata = ((sellHyper*8) - (buyCata*8))/300
        crafted["Hyper Catalysts"] = round(hyperCata,3)
    except ValueError:
        pass
    #Ultimate Carrot Candy (Raw Item)
    try:
        carrotCandyItem = min(ultimateCarrotItem)/8000
        raw["Ultimate Carrot Candy Upgrade"] = round(carrotCandyItem,3)
    except ValueError:
        pass
    #Ultimate Carrot Candy
    try:
        greatCarrot = min(greatCarrotPrices)
        buyGolden = bzData["products"]["ENCHANTED_GOLDEN_CARROT"]["buy_summary"][0]["pricePerUnit"]
        superb = (buyGolden*24) + (greatCarrot)
        ultimateCarrot = ((min(ultimateCarrotPrices)*10)-(superb*8))/8000
        crafted["Ultimate Carrot Candy"] = round(ultimateCarrot,3)
    except ValueError:
        pass
    #Colossal Item
    try:
        colossalItem = min(colossalPrices)/1200
        raw["Colossal Bottle Upgrade"] = round(colossalItem,3)
    except ValueError:
        pass
    #Colossal Experience Bottle
    try:
        buyTitantic = bzData["products"]["TITANIC_EXP_BOTTLE"]["buy_summary"][0]["pricePerUnit"]
        sellColossal = bzData["products"]["COLOSSAL_EXP_BOTTLE"]["sell_summary"][0]["pricePerUnit"]
        colossalExp = ((sellColossal) - (buyTitantic))/1200
        crafted["Colossal Experience Bottles"] = round(colossalExp,3)
    except ValueError:
        pass
    #Jumbo Backpack Item
    try:
        jumboItem = min(jumboItemPrices)/4000
        raw["Jumbo Backpack Upgrade"] = round(jumboItem,3)
    except ValueError:
        pass
    #Jumbo Backpack Upgrade
    try:
        jumboUpgrade = ((min(jumboPrices))-(min(greaterPrices)))/4000
        crafted["Jumbo Backpacks"] = round(jumboUpgrade,3)
    except ValueError:
        pass
    #Hologram
    try:
        hologram = (min(hologramPrices))/2000
        raw["Hologram"] = round(hologram,3)
    except ValueError:
        pass
    #Builder's Wand
    try:
        buildersWand = (min(builderWandPrices))/12000
        raw["Builder's Wand"] = round(buildersWand,3)
    except ValueError:
        pass
    #Bits Talisman
    try:
        bitsTalisman = (min(bitsTalismanPrices))/15000
        raw["Bits Talisman"] = round(bitsTalisman,3)
    except ValueError:
        pass
    #Compact
    try:
        compactI = (min(compact))/4000
        raw["Compact I"] = round(compactI,3)
    except ValueError:
        pass
    #Expertise
    try:
        expertiseI = (min(expertise))/4000
        raw["Expertise I"] = round(expertiseI,3)
    except ValueError:
        pass
    #Cultivating
    try:
        cultivatingI = min(cultivating)/4000
        raw["Cultivating I"] = round(cultivatingI,3)
    except ValueError:
        pass
    #Block Zapper
    try:
        zapper = min(blockZapper)/5000
        raw["Block Zapper"] = round(zapper,3)
    except ValueError:
        pass
    #Kismet flower
    try:
        kismet = min(kismetFlowerPrices)/1350
        raw["Kismet Feather"] = round(kismet,3)
    except ValueError:
        pass
    #Auto Pet
    try:
        autoPet = min(autoPetPrices)/21000
        raw["Autopet Rules"] = round(autoPet,3)
    except ValueError:
        pass
    sorted_crafted = sorted(crafted.items(), key=operator.itemgetter(1), reverse=True)
    sorted_raw = sorted(raw.items(), key=operator.itemgetter(1), reverse=True)
    crafted_message = ""
    raw_message = ""
    rank = 1
    for entry in sorted_crafted:
        crafted_message += f"{rank}.`{entry[0]}` at `{entry[1]}`\n"
        rank += 1
    rank = 1
    for entry in sorted_raw:
        raw_message += f"{rank}.`{entry[0]}` at `{entry[1]}`\n"
        rank += 1
    return crafted_message, raw_message

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

def get_dungeon(floor):
    if int(floor) == 1:
        rejuvenateI = []
        rejuvenateII = []
        featherVI = []
        quiverVI = []
        comboI = []
        jerryI = []
        mask = []
        staff = []
        nose = []
        brooch = []
        with open("data/ah.json") as json_file:
            data = json.load(json_file)
            for entry in data["auctions"]:
                if "bin" in entry:
                    if entry["item_lore"] == "§9Rejuvenate I\n§7Increases your natural\n§7regeneration by §a+2%§7.\n\n§7§7Apply Cost: §39 Exp Levels\n\n§7§cRequires Enchanting 10 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Rejuvenate II\n§7Increases your natural\n§7regeneration by §a+4%§7.\n\n§7§7Apply Cost: §318 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Feather Falling VI\n§7Increases how high you can fall\n§7before taking fall damage by\n§7§a6§7 and reduces fall damage by\n§7§a30%§7.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        featherVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Infinite Quiver VI\n§7Saves arrows §a60%§7 of the time\n§7when you fire your bow.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        quiverVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lCombo I\n§7Every mob kill within §e3§7\n§7seconds grants §c+2❁ Strength\n§c§7and §9+1☠ Crit Damage§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        comboI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Jerry I\n§7Increases the base damage of\n§7§fAspect of the Jerry§7 by\n§7§a1000%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        jerryI.append(entry["starting_bid"])
                    elif "Bonzo's Mask" in entry["item_name"]:
                        mask.append(entry["starting_bid"])
                    elif "Bonzo's Staff" in entry["item_name"]:
                        staff.append(entry["starting_bid"])
                    elif "Red Nose" in entry["item_name"]:
                        nose.append(entry["starting_bid"])
                    elif "Necromancer's Brooch" in entry["item_name"]:
                        brooch.append(entry["starting_bid"])

        armor = ""
        try:
            armor += f"`Bonzo's Mask` : `{'{:,}'.format(min(mask))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Bonzo's Staff` : `{'{:,}'.format(min(staff))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Red Nose` : `{'{:,}'.format(min(nose))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Necromancer's Brooch` : `{'{:,}'.format(min(brooch))}`\n"
        except ValueError:
            pass
        bazaar = requests.get("https://api.hypixel.net/skyblock/bazaar").json()["products"]
        armor += f"\n`Recombobulator` : `{'{:,}'.format(round(bazaar['RECOMBOBULATOR_3000']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Hot Potato Book` : `{'{:,}'.format(round(bazaar['HOT_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Fuming Potato Book` : `{'{:,}'.format(round(bazaar['FUMING_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"
        books = ""
        try:
            books += f"`Rejuvenate I` : `{'{:,}'.format(min(rejuvenateI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rejuvenate II` : `{'{:,}'.format(min(rejuvenateII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Feather Falling VI` : `{'{:,}'.format(min(featherVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Infinite Quiver VI` : `{'{:,}'.format(min(quiverVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Combo I` : `{'{:,}'.format(min(comboI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Jerry I` : `{'{:,}'.format(min(jerryI))}`\n"
        except ValueError:
            pass
    elif int(floor) == 2:
        rejuvenateI = []
        rejuvenateII = []
        rejuvenateIII = []
        featherVI = []
        quiverVI = []
        ultiWiseI = []
        wisdomI = []
        comboI = []
        jerryI = []
        adaptiveBlade = []
        studies = []
        brooch = []
        redScarf = []
        with open("data/ah.json") as json_file:
            data = json.load(json_file)
            for entry in data["auctions"]:
                if "bin" in entry:
                    if entry["item_lore"] == "§9Rejuvenate I\n§7Increases your natural\n§7regeneration by §a+2%§7.\n\n§7§7Apply Cost: §39 Exp Levels\n\n§7§cRequires Enchanting 10 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Rejuvenate II\n§7Increases your natural\n§7regeneration by §a+4%§7.\n\n§7§7Apply Cost: §318 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Rejuvenate III\n§7Increases your natural\n§7regeneration by §a+6%§7.\n\n§7§7Apply Cost: §327 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateIII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Feather Falling VI\n§7Increases how high you can fall\n§7before taking fall damage by\n§7§a6§7 and reduces fall damage by\n§7§a30%§7.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        featherVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Infinite Quiver VI\n§7Saves arrows §a60%§7 of the time\n§7when you fire your bow.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        quiverVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Wise I\n§7Reduces the ability mana cost of\n§7this item by §a10%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        ultiWiseI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lWisdom I\n§7Gain §b1 §7Intelligence for\n§7every §b5 §7levels of exp you\n§7have on you. Capped at §b20\n§b§7Intelligence.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        wisdomI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lCombo I\n§7Every mob kill within §e3§7\n§7seconds grants §c+2❁ Strength\n§c§7and §9+1☠ Crit Damage§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        comboI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Jerry I\n§7Increases the base damage of\n§7§fAspect of the Jerry§7 by\n§7§a1000%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        jerryI.append(entry["starting_bid"])
                    elif "Adaptive Blade" in entry["item_name"]:
                        adaptiveBlade.append(entry["starting_bid"])
                    elif "Scarf's Studies" in entry["item_name"]:
                        studies.append(entry["starting_bid"])
                    elif "Necromancer's Brooch" in entry["item_name"]:
                        brooch.append(entry["starting_bid"])
                    elif "Red Scarf" in entry["item_name"]:
                        redScarf.append(entry["item_name"])
        armor = ""
        try:
            armor += f"`Adaptive Blade` : `{'{:,}'.format(min(adaptiveBlade))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Scarf's Studies` : `{'{:,}'.format(min(studies))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Red Scarf` : `{'{:,}'.format(min(redScarf))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Necromancer's Brooch` : `{'{:,}'.format(min(brooch))}`\n"
        except ValueError:
            pass
        bazaar = requests.get("https://api.hypixel.net/skyblock/bazaar").json()["products"]
        armor += f"\n`Recombobulator` : `{'{:,}'.format(round(bazaar['RECOMBOBULATOR_3000']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Hot Potato Book` : `{'{:,}'.format(round(bazaar['HOT_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Fuming Potato Book` : `{'{:,}'.format(round(bazaar['FUMING_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"
        books = ""
        try:
            books += f"`Rejuvenate I` : `{'{:,}'.format(min(rejuvenateI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rejuvenate II` : `{'{:,}'.format(min(rejuvenateII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rejuvenate III` : `{'{:,}'.format(min(rejuvenateIII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Feather Falling VI` : `{'{:,}'.format(min(featherVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Infinite Quiver VI` : `{'{:,}'.format(min(quiverVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Wise I` : `{'{:,}'.format(min(ultiWiseI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Wisdom I` : `{'{:,}'.format(min(wisdomI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Combo I` : `{'{:,}'.format(min(comboI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Jerry I` : `{'{:,}'.format(min(jerryI))}`\n"
        except ValueError:
            pass
    elif int(floor) == 3:
        rejuvenateI = []
        rejuvenateII = []
        rejuvenateIII = []
        featherVI = []
        quiverVI = []
        ultiWiseI = []
        wisdomI = []
        lastStandI = []
        comboI = []
        jerryI = []
        adaptiveHelm = []
        adaptiveChest = []
        adaptiveLegs = []
        adaptiveBoots = []
        brooch = []
        vial = []
        with open("data/ah.json") as json_file:
            data = json.load(json_file)
            for entry in data["auctions"]:
                if "bin" in entry:
                    if entry["item_lore"] == "§9Rejuvenate I\n§7Increases your natural\n§7regeneration by §a+2%§7.\n\n§7§7Apply Cost: §39 Exp Levels\n\n§7§cRequires Enchanting 10 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Rejuvenate II\n§7Increases your natural\n§7regeneration by §a+4%§7.\n\n§7§7Apply Cost: §318 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Rejuvenate III\n§7Increases your natural\n§7regeneration by §a+6%§7.\n\n§7§7Apply Cost: §327 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateIII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Feather Falling VI\n§7Increases how high you can fall\n§7before taking fall damage by\n§7§a6§7 and reduces fall damage by\n§7§a30%§7.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        featherVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Infinite Quiver VI\n§7Saves arrows §a60%§7 of the time\n§7when you fire your bow.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        quiverVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Wise I\n§7Reduces the ability mana cost of\n§7this item by §a10%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        ultiWiseI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lWisdom I\n§7Gain §b1 §7Intelligence for\n§7every §b5 §7levels of exp you\n§7have on you. Capped at §b20\n§b§7Intelligence.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        wisdomI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lLast Stand I\n§7Increases your defense by §a5%\n§a§7when you are below §a40%\n§a§7Health\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7§cRequires Enchanting 30 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        lastStandI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lCombo I\n§7Every mob kill within §e3§7\n§7seconds grants §c+2❁ Strength\n§c§7and §9+1☠ Crit Damage§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        comboI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Jerry I\n§7Increases the base damage of\n§7§fAspect of the Jerry§7 by\n§7§a1000%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        jerryI.append(entry["starting_bid"])
                    elif "Adaptive Helm" in entry["item_name"]:
                        adaptiveHelm.append(entry["starting_bid"])
                    elif "Adaptive Chestplate" in entry["item_name"]:
                        adaptiveChest.append(entry["starting_bid"])
                    elif "Adaptive Leggings" in entry["item_name"]:
                        adaptiveLegs.append(entry["starting_bid"])
                    elif "Adaptive Boots" in entry["item_name"]:
                        adaptiveBoots.append(entry["starting_bid"])
                    elif "Necromancer's Brooch" in entry["item_name"]:
                        brooch.append(entry["starting_bid"])
                    elif "Suspicious Vial" in entry["item_name"]:
                        vial.append(entry["starting_bid"])
        armor = ""
        try:
            armor += f"`Adaptive Helm` : `{'{:,}'.format(min(adaptiveHelm))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Adaptive Chestplate` : `{'{:,}'.format(min(adaptiveChest))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Adaptive Leggings` : `{'{:,}'.format(min(adaptiveLegs))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Adaptive Boots` : `{'{:,}'.format(min(adaptiveBoots))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Necromancer's Brooch` : `{'{:,}'.format(min(brooch))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Suspicious Vial` : `{'{:,}'.format(min(vial))}`\n"
        except ValueError:
            pass
        bazaar = requests.get("https://api.hypixel.net/skyblock/bazaar").json()["products"]
        armor += f"\n`Recombobulator` : `{'{:,}'.format(round(bazaar['RECOMBOBULATOR_3000']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Hot Potato Book` : `{'{:,}'.format(round(bazaar['HOT_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Fuming Potato Book` : `{'{:,}'.format(round(bazaar['FUMING_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"

        books = ""
        try:
            books += f"`Rejuvenate I` : `{'{:,}'.format(min(rejuvenateI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rejuvenate II` : `{'{:,}'.format(min(rejuvenateII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rejuvenate III` : `{'{:,}'.format(min(rejuvenateIII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Feather Falling VI` : `{'{:,}'.format(min(featherVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Infinite Quiver VI` : `{'{:,}'.format(min(quiverVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Wise I` : `{'{:,}'.format(min(ultiWiseI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Wisdom I` : `{'{:,}'.format(min(wisdomI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Last Stand I` : `{'{:,}'.format(min(lastStandI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Combo I` : `{'{:,}'.format(min(comboI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Jerry I` : `{'{:,}'.format(min(jerryI))}`\n"
        except ValueError:
            pass
    elif int(floor) == 4:
        rejuvenateI = []
        rejuvenateII = []
        rejuvenateIII = []
        featherVI = []
        quiverVI = []
        ultiWiseI = []
        wisdomI = []
        lastStandI = []
        comboI = []
        rendI = []
        jerryI = []
        spiritSword = []
        spiritBow = []
        spiritStone = []
        spiritBoots = []
        spiritBone = []
        spiritWing = []
        epicSpirit = []
        legendarySpirit = []
        brooch = []
        with open("data/ah.json") as json_file:
            data = json.load(json_file)
            for entry in data["auctions"]:
                if "bin" in entry:
                    if entry["item_lore"] == "§9Rejuvenate I\n§7Increases your natural\n§7regeneration by §a+2%§7.\n\n§7§7Apply Cost: §39 Exp Levels\n\n§7§cRequires Enchanting 10 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Rejuvenate II\n§7Increases your natural\n§7regeneration by §a+4%§7.\n\n§7§7Apply Cost: §318 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Rejuvenate III\n§7Increases your natural\n§7regeneration by §a+6%§7.\n\n§7§7Apply Cost: §327 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateIII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Feather Falling VI\n§7Increases how high you can fall\n§7before taking fall damage by\n§7§a6§7 and reduces fall damage by\n§7§a30%§7.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        featherVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Infinite Quiver VI\n§7Saves arrows §a60%§7 of the time\n§7when you fire your bow.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        quiverVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Wise I\n§7Reduces the ability mana cost of\n§7this item by §a10%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        ultiWiseI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lWisdom I\n§7Gain §b1 §7Intelligence for\n§7every §b5 §7levels of exp you\n§7have on you. Capped at §b20\n§b§7Intelligence.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        wisdomI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lLast Stand I\n§7Increases your defense by §a5%\n§a§7when you are below §a40%\n§a§7Health\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7§cRequires Enchanting 30 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        lastStandI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lCombo I\n§7Every mob kill within §e3§7\n§7seconds grants §c+2❁ Strength\n§c§7and §9+1☠ Crit Damage§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        comboI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lRend I\n§7Grants your bow a Left Click\n§7ability that rips out the arrows\n§7from nearby enemies and deals\n§7§c5% §7of your last critical hit\n§7for every arrow in the target.\n§7§a2s §7Cooldown.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7§cRequires Enchanting 32 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rendI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Jerry I\n§7Increases the base damage of\n§7§fAspect of the Jerry§7 by\n§7§a1000%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        jerryI.append(entry["starting_bid"])
                    elif "Spirit Sword" in entry["item_name"]:
                        spiritSword.append(entry["starting_bid"])
                    elif "Spirit Bow" in entry["item_name"]:
                        spiritBow.append(entry["starting_bid"])
                    elif "Spirit Stone" in entry["item_name"]:
                        spiritStone.append(entry["starting_bid"])
                    elif "Spirit Boots" in entry["item_name"]:
                        spiritBoots.append(entry["starting_bid"])
                    elif "Spirit Bone" in entry["item_name"]:
                        spiritBone.append(entry["starting_bid"])
                    elif "Spirit Wing" in entry["item_name"]:
                        spiritWing.append(entry["starting_bid"])
                    elif "Spirit Skull Item" in entry["extra"] and entry["tier"] == "EPIC":
                        epicSpirit.append(entry["starting_bid"])
                    elif "Spirit Skull Item" in entry["extra"] and entry["tier"] == "LEGENDARY":
                        legendarySpirit.append(entry["starting_bid"])
                    elif "Necromancer's Brooch" in entry["item_name"]:
                        brooch.append(entry["starting_bid"])

        armor = ""
        try:
            armor += f"`Spirit Sword` : `{'{:,}'.format(min(spiritSword))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Spirit Bow` : `{'{:,}'.format(min(spiritBow))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Spirit Boots` : `{'{:,}'.format(min(spiritBoots))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Spirit Stone` : `{'{:,}'.format(min(spiritStone))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Spirit Bone` : `{'{:,}'.format(min(spiritBone))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Spirit Wing` : `{'{:,}'.format(min(spiritWing))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Spirit Pet (Epic)` : `{'{:,}'.format(min(epicSpirit))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Spirit Pet (Legendary)` : `{'{:,}'.format(min(legendarySpirit))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Necromancer's Brooch` : `{'{:,}'.format(min(brooch))}`\n"
        except ValueError:
            pass

        bazaar = requests.get("https://api.hypixel.net/skyblock/bazaar").json()["products"]
        armor += f"\n`Recombobulator` : `{'{:,}'.format(round(bazaar['RECOMBOBULATOR_3000']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Hot Potato Book` : `{'{:,}'.format(round(bazaar['HOT_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Fuming Potato Book` : `{'{:,}'.format(round(bazaar['FUMING_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"

        books = ""
        try:
            books += f"`Rejuvenate I` : `{'{:,}'.format(min(rejuvenateI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rejuvenate II` : `{'{:,}'.format(min(rejuvenateII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rejuvenate III` : `{'{:,}'.format(min(rejuvenateIII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Feather Falling VI` : `{'{:,}'.format(min(featherVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Infinite Quiver VI` : `{'{:,}'.format(min(quiverVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Wise I` : `{'{:,}'.format(min(ultiWiseI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Wisdom I` : `{'{:,}'.format(min(wisdomI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Last Stand I` : `{'{:,}'.format(min(lastStandI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Combo I` : `{'{:,}'.format(min(comboI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rend I` : `{'{:,}'.format(min(rendI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Jerry I` : `{'{:,}'.format(min(jerryI))}`\n"
        except ValueError:
            pass
    elif int(floor) == 5:
        rejuvenateI = []
        rejuvenateII = []
        rejuvenateIII = []
        featherVI = []
        quiverVI = []
        ultiWiseI = []
        wisdomI = []
        lastStandI = []
        comboI = []
        legionI = []
        overloadI = []
        lethalityVI = []
        jerryI = []
        jerryII = []
        jerryIII = []
        shadowHelm = []
        shadowChest = []
        shadowLegs = []
        shadowBoots = []
        lividDag = []
        shadowFury = []
        warpedStone = []
        darkOrb = []
        lastBreath = []
        with open("data/ah.json") as json_file:
            data = json.load(json_file)
            for entry in data["auctions"]:
                if "bin" in entry:
                    if entry["item_lore"] == "§9Rejuvenate I\n§7Increases your natural\n§7regeneration by §a+2%§7.\n\n§7§7Apply Cost: §39 Exp Levels\n\n§7§cRequires Enchanting 10 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Rejuvenate II\n§7Increases your natural\n§7regeneration by §a+4%§7.\n\n§7§7Apply Cost: §318 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Rejuvenate III\n§7Increases your natural\n§7regeneration by §a+6%§7.\n\n§7§7Apply Cost: §327 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateIII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Feather Falling VI\n§7Increases how high you can fall\n§7before taking fall damage by\n§7§a6§7 and reduces fall damage by\n§7§a30%§7.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        featherVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Infinite Quiver VI\n§7Saves arrows §a60%§7 of the time\n§7when you fire your bow.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        quiverVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Wise I\n§7Reduces the ability mana cost of\n§7this item by §a10%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        ultiWiseI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lWisdom I\n§7Gain §b1 §7Intelligence for\n§7every §b5 §7levels of exp you\n§7have on you. Capped at §b20\n§b§7Intelligence.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        wisdomI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lLast Stand I\n§7Increases your defense by §a5%\n§a§7when you are below §a40%\n§a§7Health\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7§cRequires Enchanting 30 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        lastStandI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lCombo I\n§7Every mob kill within §e3§7\n§7seconds grants §c+2❁ Strength\n§c§7and §9+1☠ Crit Damage§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        comboI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lLegion I\n§7Increases most of your player\n§7stats by §e0.07% §7per player\n§7within §b30 §7blocks of you, up\n§7to §c20 §7players.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        legionI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Overload I\n§7Increases §9☠ Crit Damage §7by\n§7§a1%§7 and §9☣ Crit Chance §7by\n§7§a1%§7. Having a Critical chance\n§7above §9100% §7grants a chance\n§7to perform a Mega Critical Hit\n§7dealing §910% §7extra damage.\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7§cRequires Enchanting 33 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        overloadI.append(entry["starting_bid"])
                    elif entry["item_lore"] ==  "§9Lethality VI\n§7Reduces the armor of your target\n§7by §a18% §7for §68 §7seconds\n§7each time you hit them with\n§7melee. Stacks up to §a5 §7times.\n\n§7§7Apply Cost: §3179 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        lethalityVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Jerry I\n§7Increases the base damage of\n§7§fAspect of the Jerry§7 by\n§7§a1000%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        jerryI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Jerry II\n§7Increases the base damage of\n§7§fAspect of the Jerry§7 by\n§7§a2000%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §391 Exp Levels\n\n§7§cRequires Enchanting 18 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        jerryII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Jerry III\n§7Increases the base damage of\n§7§fAspect of the Jerry§7 by\n§7§a3000%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §3136 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        jerryIII.append(entry["starting_bid"])
                    elif "Shadow Assassin Helmet" in entry["item_name"]:
                        shadowHelm.append(entry["starting_bid"])
                    elif "Shadow Assassin Chestplate" in entry["item_name"]:
                        shadowChest.append(entry["starting_bid"])
                    elif "Shadow Assassin Leggings" in entry["item_name"]:
                        shadowLegs.append(entry["starting_bid"])
                    elif "Shadow Assassin Boots" in entry["item_name"]:
                        shadowBoots.append(entry["starting_bid"])
                    elif "Livid Dagger" in entry["item_name"]:
                        lividDag.append(entry["starting_bid"])
                    elif "Shadow Fury" in entry["item_name"]:
                        shadowFury.append(entry["starting_bid"])
                    elif "Livid Dagger" in entry["item_name"]:
                        lividDag.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§8Reforge Stone\n\n§7Can be used in a Reforge Anvil\n§7or with the Dungeon Blacksmith\n§7to apply the §9Warped §7reforge\n§7to a melee weapon.\n\n§7§8§oIf you look deep inside, you\n§8§orisk finding yourself somewhere\n§8§oelse.\n\n§7Requires §aMining Skill Level\n§aXXVI§7!\n\n§9§lRARE REFORGE STONE":
                        warpedStone.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§8Reforge Stone\n\n§7Can be used in a Reforge Anvil\n§7or with the Dungeon Blacksmith\n§7to apply the §9Shaded §7reforge\n§7to accessories.\n\n§7§8§oAssassins use it,\n§8§oapparently.\n\n§9§lRARE REFORGE STONE":
                        darkOrb.append(entry["starting_bid"])
                    elif "Last Breath" in entry["item_name"]:
                        lastBreath.append(entry["starting_bid"])
        armor = ""
        try:
            armor += f"`Shadow Assassin Helmet` : `{'{:,}'.format(min(shadowHelm))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Shadow Assassin Chestplate` : `{'{:,}'.format(min(shadowChest))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Shadow Assassin Leggings` : `{'{:,}'.format(min(shadowLegs))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Shadow Assassin Boots` : `{'{:,}'.format(min(shadowBoots))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Shadow Fury` : `{'{:,}'.format(min(shadowFury))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Livid Dagger` : `{'{:,}'.format(min(lividDag))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Last Breath` : `{'{:,}'.format(min(lastBreath))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Warped Stone` : `{'{:,}'.format(min(warpedStone))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Dark Orb` : `{'{:,}'.format(min(darkOrb))}`\n"
        except ValueError:
            pass

        bazaar = requests.get("https://api.hypixel.net/skyblock/bazaar").json()["products"]
        armor += f"\n`Recombobulator` : `{'{:,}'.format(round(bazaar['RECOMBOBULATOR_3000']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Hot Potato Book` : `{'{:,}'.format(round(bazaar['HOT_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Fuming Potato Book` : `{'{:,}'.format(round(bazaar['FUMING_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"

        books = ""
        try:
            books += f"`Rejuvenate I` : `{'{:,}'.format(min(rejuvenateI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rejuvenate II` : `{'{:,}'.format(min(rejuvenateII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rejuvenate III` : `{'{:,}'.format(min(rejuvenateIII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Feather Falling VI` : `{'{:,}'.format(min(featherVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Infinite Quiver VI` : `{'{:,}'.format(min(quiverVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Lethality VI` : `{'{:,}'.format(min(lethalityVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Wise I` : `{'{:,}'.format(min(ultiWiseI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Wisdom I` : `{'{:,}'.format(min(wisdomI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Last Stand I` : `{'{:,}'.format(min(lastStandI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Combo I` : `{'{:,}'.format(min(comboI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Legion I` : `{'{:,}'.format(min(legionI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Overload I` : `{'{:,}'.format(min(overloadI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Jerry I` : `{'{:,}'.format(min(jerryI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Jerry II` : `{'{:,}'.format(min(jerryII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Jerry III` : `{'{:,}'.format(min(jerryIII))}`\n"
        except ValueError:
            pass
    elif int(floor) == 6:
        rejuvenateI = []
        rejuvenateII = []
        rejuvenateIII = []
        featherVI = []
        quiverVI = []
        ultiWiseI = []
        wisdomI = []
        lastStandI = []
        comboI = []
        swarmI = []
        jerryI = []
        jerryII = []
        jerryIII = []
        necroHelmet = []
        necroChest = []
        necroLegs = []
        necroBoots = []
        necroSword = []
        giantTooth = []
        summoningRing = []
        sadans = []
        giantSword = []
        precursor = []
        rose = []
        with open("data/ah.json") as json_file:
            data = json.load(json_file)
            for entry in data["auctions"]:
                if "bin" in entry:
                    if entry["item_lore"] == "§9Rejuvenate I\n§7Increases your natural\n§7regeneration by §a+2%§7.\n\n§7§7Apply Cost: §39 Exp Levels\n\n§7§cRequires Enchanting 10 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Rejuvenate II\n§7Increases your natural\n§7regeneration by §a+4%§7.\n\n§7§7Apply Cost: §318 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Rejuvenate III\n§7Increases your natural\n§7regeneration by §a+6%§7.\n\n§7§7Apply Cost: §327 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateIII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Feather Falling VI\n§7Increases how high you can fall\n§7before taking fall damage by\n§7§a6§7 and reduces fall damage by\n§7§a30%§7.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        featherVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Infinite Quiver VI\n§7Saves arrows §a60%§7 of the time\n§7when you fire your bow.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        quiverVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Wise I\n§7Reduces the ability mana cost of\n§7this item by §a10%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        ultiWiseI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lWisdom I\n§7Gain §b1 §7Intelligence for\n§7every §b5 §7levels of exp you\n§7have on you. Capped at §b20\n§b§7Intelligence.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        wisdomI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lLast Stand I\n§7Increases your defense by §a5%\n§a§7when you are below §a40%\n§a§7Health\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7§cRequires Enchanting 30 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        lastStandI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lCombo I\n§7Every mob kill within §e3§7\n§7seconds grants §c+2❁ Strength\n§c§7and §9+1☠ Crit Damage§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        comboI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lSwarm I\n§7Increases your damage by §c1.25%\n§c§7for each enemy within §e10\n§e§7blocks. Maximum of §c16\n§c§7enemies.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        swarmI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Jerry I\n§7Increases the base damage of\n§7§fAspect of the Jerry§7 by\n§7§a1000%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        jerryI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Jerry II\n§7Increases the base damage of\n§7§fAspect of the Jerry§7 by\n§7§a2000%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §391 Exp Levels\n\n§7§cRequires Enchanting 18 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        jerryII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Jerry III\n§7Increases the base damage of\n§7§fAspect of the Jerry§7 by\n§7§a3000%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §3136 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        jerryIII.append(entry["starting_bid"])
                    elif "Necromancer Lord Helmet" in entry["item_name"]:
                        necroHelmet.append(entry["starting_bid"])
                    elif "Necromancer Lord Chestplate" in entry["item_name"]:
                        necroChest.append(entry["starting_bid"])
                    elif "Necromancer Lord Leggings" in entry["item_name"]:
                        necroLegs.append(entry["starting_bid"])
                    elif "Necromancer Lord Boots" in entry["item_name"]:
                        necroBoots.append(entry["starting_bid"])
                    elif "Necromancer Sword" in entry["item_name"]:
                        necroSword.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§8Reforge Stone\n\n§7Can be used in a Reforge Anvil\n§7or with the Dungeon Blacksmith\n§7to apply the §9Giant §7reforge\n§7to armor.\n\n§7§8§oSuper clean, great hygiene.\n\n§7Requires §aMining Skill Level\n§aXXV§7!\n\n§5§lEPIC REFORGE STONE":
                        giantTooth.append(entry["starting_bid"])
                    elif "Summoning Ring" in entry["item_name"]:
                        summoningRing.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§8Reforge Stone\n\n§7Can be used in a Reforge Anvil\n§7or with the Dungeon Blacksmith\n§7to apply the §9Empowered\n§9§7reforge to armor.\n\n§7§8§oVery original...\n\n§7Requires §aMining Skill Level\n§aXXV§7!\n\n§5§lEPIC REFORGE STONE":
                        sadans.append(entry["starting_bid"])
                    elif "Giant's Sword" in entry["item_name"]:
                        giantSword.append(entry["starting_bid"])
                    elif "Precursor Eye" in entry["item_name"]:
                        precursor.append(entry["starting_bid"])
                    elif "Ancient Rose" in entry["item_name"]:
                        rose.append(entry["starting_bid"])

        armor = ""
        try:
            armor += f"`Necromancer Lord Helmet` : `{'{:,}'.format(min(necroHelmet))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Necromancer Lord Chestplate` : `{'{:,}'.format(min(necroChest))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Necromancer Lord Leggings` : `{'{:,}'.format(min(necroLegs))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Necromancer Lord Boots` : `{'{:,}'.format(min(necroBoots))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Necromancer Sword` : `{'{:,}'.format(min(necroSword))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Giant's Sword` : `{'{:,}'.format(min(giantSword))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Giant Tooth` : `{'{:,}'.format(min(giantTooth))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Sadan's Brooch` : `{'{:,}'.format(min(sadans))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Summoning Ring` : `{'{:,}'.format(min(summoningRing))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Precursor Eye` : `{'{:,}'.format(min(precursor))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Ancient Rose` : `{'{:,}'.format(min(rose))}`\n"
        except ValueError:
            pass

        bazaar = requests.get("https://api.hypixel.net/skyblock/bazaar").json()["products"]
        armor += f"\n`Recombobulator` : `{'{:,}'.format(round(bazaar['RECOMBOBULATOR_3000']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Hot Potato Book` : `{'{:,}'.format(round(bazaar['HOT_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Fuming Potato Book` : `{'{:,}'.format(round(bazaar['FUMING_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"

        books = ""
        try:
            books += f"`Rejuvenate I` : `{'{:,}'.format(min(rejuvenateI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rejuvenate II` : `{'{:,}'.format(min(rejuvenateII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rejuvenate III` : `{'{:,}'.format(min(rejuvenateIII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Feather Falling VI` : `{'{:,}'.format(min(featherVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Infinite Quiver VI` : `{'{:,}'.format(min(quiverVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Wise I` : `{'{:,}'.format(min(ultiWiseI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Wisdom I` : `{'{:,}'.format(min(wisdomI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Last Stand I` : `{'{:,}'.format(min(lastStandI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Combo I` : `{'{:,}'.format(min(comboI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Swarm I` : `{'{:,}'.format(min(swarmI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Jerry I` : `{'{:,}'.format(min(jerryI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Jerry II` : `{'{:,}'.format(min(jerryII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Jerry III` : `{'{:,}'.format(min(jerryIII))}`\n"
        except ValueError:
            pass
    elif int(floor) == 7:
        rejuvenateI = []
        rejuvenateII = []
        rejuvenateIII = []
        featherVI = []
        featherVII = []
        quiverVI = []
        quiverVII = []
        ultiWiseI = []
        wisdomI = []
        lastStandI = []
        soulI = []
        ofaI = []
        jerryI = []
        jerryII = []
        jerryIII = []
        noPainI = []
        bankI = []
        bankII = []
        bankIII = []
        witherBoots = []
        witherLegs = []
        witherChest = []
        witherHelm = []
        witherCata = []
        witherBlood = []
        witherCloak = []
        precursor = []
        handle = []
        implosion = []
        shadowWarp = []
        witherShield = []
        autoRecomb = []
        diamante = []
        pinkRock = []
        bigfoot = []
        eye = []
        with open("data/ah.json") as json_file:
            data = json.load(json_file)
            for entry in data["auctions"]:
                if "bin" in entry:
                    if entry["item_lore"] == "§9Rejuvenate I\n§7Increases your natural\n§7regeneration by §a+2%§7.\n\n§7§7Apply Cost: §39 Exp Levels\n\n§7§cRequires Enchanting 10 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Rejuvenate II\n§7Increases your natural\n§7regeneration by §a+4%§7.\n\n§7§7Apply Cost: §318 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Rejuvenate III\n§7Increases your natural\n§7regeneration by §a+6%§7.\n\n§7§7Apply Cost: §327 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        rejuvenateIII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Feather Falling VI\n§7Increases how high you can fall\n§7before taking fall damage by\n§7§a6§7 and reduces fall damage by\n§7§a30%§7.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        featherVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Feather Falling VII\n§7Increases how high you can fall\n§7before taking fall damage by\n§7§a7§7 and reduces fall damage by\n§7§a35%§7.\n\n§7§7Apply Cost: §373 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§5§lEPIC":
                        featherVII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Infinite Quiver VI\n§7Saves arrows §a60%§7 of the time\n§7when you fire your bow.\n\n§7§7Apply Cost: §355 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§9§lRARE":
                        quiverVI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9Infinite Quiver VII\n§7Saves arrows §a70%§7 of the time\n§7when you fire your bow.\n\n§7§7Apply Cost: §373 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§5§lEPIC":
                        quiverVII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Wise I\n§7Reduces the ability mana cost of\n§7this item by §a10%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        ultiWiseI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lWisdom I\n§7Gain §b1 §7Intelligence for\n§7every §b5 §7levels of exp you\n§7have on you. Capped at §b20\n§b§7Intelligence.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        wisdomI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lLast Stand I\n§7Increases your defense by §a5%\n§a§7when you are below §a40%\n§a§7Health\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7§cRequires Enchanting 30 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        lastStandI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lSoul Eater I\n§7Your weapon gains §c2§7x the\n§7Strength of the latest monster\n§7killed and applies it on your\n§7next hit.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        soulI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lOne For All I\n§7Removes all other enchants but\n§7increases your weapon damage by\n§7§a210%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§e▲ §7§d§lOne For All cannot be combined!\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        ofaI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Jerry I\n§7Increases the base damage of\n§7§fAspect of the Jerry§7 by\n§7§a1000%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        jerryI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Jerry II\n§7Increases the base damage of\n§7§fAspect of the Jerry§7 by\n§7§a2000%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §391 Exp Levels\n\n§7§cRequires Enchanting 18 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        jerryII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lUltimate Jerry III\n§7Increases the base damage of\n§7§fAspect of the Jerry§7 by\n§7§a3000%§7.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §3136 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        jerryIII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lNo Pain No Gain I\n§7You have §e20% §7chance to gain\n§7§b10 §7experience orbs every\n§7time you take hits from mobs.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7§cRequires Enchanting 29 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        noPainI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lBank I\n§7Saves §610.0§7% of your coins on\n§7death.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §345 Exp Levels\n\n§7§cRequires Enchanting 16 to\n§capply\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        bankI.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lBank II\n§7Saves §620.0§7% of your coins on\n§7death.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §391 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        bankII.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§9§d§lBank III\n§7Saves §630.0§7% of your coins on\n§7death.\n\n§7§cYou can only have 1 Ultimate\n§cEnchantment on an item!\n\n§7§7Apply Cost: §3136 Exp Levels\n\n§7Use this on an item in an Anvil\n§7to apply it!\n\n§f§lCOMMON":
                        bankIII.append(entry["starting_bid"])
                    elif "Wither Boots" in entry["item_name"]:
                        witherBoots.append(entry["starting_bid"])
                    elif "Wither Leggings" in entry["item_name"]:
                        witherLegs.append(entry["starting_bid"])
                    elif "Wither Chestplate" in entry["item_name"]:
                        witherChest.append(entry["starting_bid"])
                    elif "Wither Helmet" in entry["item_name"]:
                        witherHelm.append(entry["starting_bid"])
                    elif "Wither Catalyst" in entry["item_name"]:
                        witherCata.append(entry["starting_bid"])
                    elif "Wither Cloak Sword" in entry["item_name"]:
                        witherCloak.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§8Reforge Stone\n\n§7Can be used in a Reforge Anvil\n§7or with the Dungeon Blacksmith\n§7to apply the §9Withered\n§9§7reforge to a melee weapon.\n\n§7Requires §aMining Skill Level\n§aXXX§7!\n\n§5§lEPIC REFORGE STONE":
                        witherBlood.append(entry["starting_bid"])
                    elif entry["item_lore"] == "§8Reforge Stone\n\n§7Can be used in a Reforge Anvil\n§7or with the Dungeon Blacksmith\n§7to apply the §9Ancient §7reforge\n§7to armor.\n\n§7Requires §aMining Skill Level\n§aXXX§7!\n\n§5§lEPIC REFORGE STONE":
                        precursor.append(entry["starting_bid"])
                    elif "Necron's Handle" in entry["item_name"]:
                        handle.append(entry["starting_bid"])
                    elif "Implosion" in entry["item_name"]:
                        implosion.append(entry["starting_bid"])
                    elif "Shadow Warp" in entry["item_name"]:
                        shadowWarp.append(entry["starting_bid"])
                    elif "Wither Shield" in entry["item_name"]:
                        witherShield.append(entry["starting_bid"])
                    elif "Auto Recombobulator" in entry["item_name"]:
                        autoRecomb.append(entry["starting_bid"])
                    elif "Diamante's Handle" in entry["item_name"]:
                        diamante.append(entry["starting_bid"])
                    elif "Jolly Pink Rock" in entry["item_name"]:
                        pinkRock.append(entry["starting_bid"])
                    elif "Bigfoot's Lasso" in entry["item_name"]:
                        bigfoot.append(entry["starting_bid"])
                    elif "L.A.S.R.'s Eye" in entry["item_name"]:
                        eye.append(entry["starting_bid"])



        armor = ""
        try:
            armor += f"`Wither Boots` : `{'{:,}'.format(min(witherBoots))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Wither Leggings` : `{'{:,}'.format(min(witherLegs))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Wither Chestplate` : `{'{:,}'.format(min(witherChest))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Wither Helmet` : `{'{:,}'.format(min(witherHelm))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Wither Catalyst` : `{'{:,}'.format(min(witherCata))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Wither Blood` : `{'{:,}'.format(min(witherBlood))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Wither Cloak Sword` : `{'{:,}'.format(min(witherCloak))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Precursor Gear` : `{'{:,}'.format(min(precursor))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Necron's Handle` : `{'{:,}'.format(min(handle))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Implosion` : `{'{:,}'.format(min(implosion))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Shadow Warp` : `{'{:,}'.format(min(shadowWarp))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Wither Shield` : `{'{:,}'.format(min(witherShield))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Diamante's Handle` : `{'{:,}'.format(min(diamante))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Jolly Pink Rock` : `{'{:,}'.format(min(pinkRock))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`Bigfoot's Lasso` : `{'{:,}'.format(min(bigfoot))}`\n"
        except ValueError:
            pass
        try:
            armor += f"`L.A.S.R.'s Eye` : `{'{:,}'.format(min(eye))}`\n"
        except ValueError:
            pass
        try:
            armor += f"\n`Auto Recombobulator` : `{'{:,}'.format(min(autoRecomb))}`\n"
        except ValueError:
            pass

        bazaar = requests.get("https://api.hypixel.net/skyblock/bazaar").json()["products"]
        armor += f"\n`Recombobulator` : `{'{:,}'.format(round(bazaar['RECOMBOBULATOR_3000']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Hot Potato Book` : `{'{:,}'.format(round(bazaar['HOT_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"
        armor += f"`Fuming Potato Book` : `{'{:,}'.format(round(bazaar['FUMING_POTATO_BOOK']['sell_summary'][0]['pricePerUnit']))}`\n"

        books = ""
        try:
            books += f"`Rejuvenate I` : `{'{:,}'.format(min(rejuvenateI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rejuvenate II` : `{'{:,}'.format(min(rejuvenateII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Rejuvenate III` : `{'{:,}'.format(min(rejuvenateIII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Feather Falling VI` : `{'{:,}'.format(min(featherVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Feather Falling VII` : `{'{:,}'.format(min(featherVII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Infinite Quiver VI` : `{'{:,}'.format(min(quiverVI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Infinite Quiver VII` : `{'{:,}'.format(min(quiverVII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Wise I` : `{'{:,}'.format(min(ultiWiseI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Wisdom I` : `{'{:,}'.format(min(wisdomI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Last Stand I` : `{'{:,}'.format(min(lastStandI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Soul Eater I` : `{'{:,}'.format(min(soulI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`One for All I` : `{'{:,}'.format(min(ofaI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Jerry I` : `{'{:,}'.format(min(jerryI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Jerry II` : `{'{:,}'.format(min(jerryII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Ultimate Jerry III` : `{'{:,}'.format(min(jerryIII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`No Pain No Gain I` : `{'{:,}'.format(min(noPainI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Bank I` : `{'{:,}'.format(min(bankI))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Bank II` : `{'{:,}'.format(min(bankII))}`\n"
        except ValueError:
            pass
        try:
            books += f"`Bank III` : `{'{:,}'.format(min(bankIII))}`\n"
        except ValueError:
            pass

    return books, armor
