import requests
import json
import helpers.key

def search_BIN(item):
    data = json.load(open("data/ah.json"))
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
    data = json.load(open("data/ah.json"))
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
