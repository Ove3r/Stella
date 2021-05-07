import json

def GET_MINION_CONSTANTS():
    with open("data/minions.json") as json_file:
        data = json.load(json_file)

    return data

def GET_PLAYER_MINION():
    constant = {
        "WHEAT":{
            "list":[],
            "category": "farming"
        },
        "CARROT":{
            "list":[],
            "category": "farming"
        },
        "POTATO":{
            "list":[],
            "category": "farming"
        },
        "PUMPKIN":{
            "list":[],
            "category": "farming"
        },
        "MELON":{
            "list":[],
            "category": "farming"
        },
        "MUSHROOM":{
            "list":[],
            "category": "farming"
        },
        "COCOA":{
            "list":[],
            "category": "farming"
        },
        "CACTUS":{
            "list":[],
            "category": "farming"
        },
        "SUGAR_CANE":{
            "list":[],
            "category": "farming"
        },
        "COW":{
            "list":[],
            "category": "farming"
        },
        "PIG":{
            "list":[],
            "category": "farming"
        },
        "CHICKEN":{
            "list":[],
            "category": "farming"
        },
        "SHEEP":{
            "list":[],
            "category": "farming"
        },
        "RABBIT":{
            "list":[],
            "category": "farming"
        },
        "NETHER_WARTS":{
            "list":[],
            "category": "farming"
        },
        "COBBLESTONE":{
            "list":[],
            "category": "mining"
        },
        "COAL":{
            "list":[],
            "category": "mining"
        },
        "IRON":{
            "list":[],
            "category": "mining"
        },
        "GOLD":{
            "list":[],
            "category": "mining"
        },
        "DIAMOND":{
            "list":[],
            "category": "mining"
        },
        "LAPIS":{
            "list":[],
            "category": "mining"
        },
        "EMERALD":{
            "list":[],
            "category": "mining"
        },
        "REDSTONE":{
            "list":[],
            "category": "mining"
        },
        "QUARTZ":{
            "list":[],
            "category": "mining"
        },
        "OBSIDIAN":{
            "list":[],
            "category": "mining"
        },
        "GLOWSTONE":{
            "list":[],
            "category": "mining"
        },
        "GRAVEL":{
            "list":[],
            "category": "mining"
        },
        "ICE":{
            "list":[],
            "category": "mining"
        },
        "SAND":{
            "list":[],
            "category": "mining"
        },
        "ENDER_STONE":{
            "list":[],
            "category": "mining"
        },
        "CLAY":{
            "list":[],
            "category": "mining"
        },
        "MITHRIL":{
            "list":[],
            "category": "mining"
        },
        "ZOMBIE":{
            "list":[],
            "category": "combat"
        },
        "SKELETON":{
            "list":[],
            "category": "combat"
        },
        "SPIDER":{
            "list":[],
            "category": "combat"
        },
        "CAVESPIDER":{
            "list":[],
            "category": "combat"
        },
        "CREEPER":{
            "list":[],
            "category": "combat"
        },
        "ENDERMAN":{
            "list":[],
            "category": "combat"
        },
        "GHAST":{
            "list":[],
            "category": "combat"
        },
        "SLIME":{
            "list":[],
            "category": "combat"
        },
        "BLAZE":{
            "list":[],
            "category": "combat"
        },
        "MAGMA_CUBE":{
            "list":[],
            "category": "combat"
        },
        "REVENANT":{
            "list":[],
            "category": "combat"
        },
        "TARANTULA":{
            "list":[],
            "category": "combat"
        },
        "OAK":{
            "list":[],
            "category": "foraging"
        },
        "SPRUCE":{
            "list":[],
            "category": "foraging"
        },
        "BIRCH":{
            "list":[],
            "category": "foraging"
        },
        "DARK_OAK":{
            "list":[],
            "category": "foraging"
        },
        "ACACIA":{
            "list":[],
            "category": "foraging"
        },
        "JUNGLE":{
            "list":[],
            "category": "foraging"
        },
        "FISHING":{
            "list":[],
            "category": "fishing"
        },
        "FLOWER":{
            "list":[],
            "category": "foraging"
        },
        "SNOW":{
            "list":[],
            "category": "mining"
        }
    }
    
    return constant
