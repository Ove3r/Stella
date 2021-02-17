import requests
from helpers.errors import *

def productName(name):
    name = name.lower()
    ###Items are separated into Categories
    #This will be eventually changed into a constant map. I know it's bad. Go look at the bad code elsewhere please.
    #Farming

    #Wheat
    if (name == "wheat"):
        return "WHEAT"
    if (name == "enchanted bread") or (name == "ebread") or (name == "bread"):
        return "ENCHANTED_BREAD"
    if (name == "hay bale") or (name == "haybale"):
        return "HAY_BLOCK"
    if (name == "enchanted hay bale") or (name == "ebale") or (name == "ehayblock"):
        return "ENCHANTED_HAY_BLOCK"
    if (name == "tightly-tied hay bale") or (name == "tightly tied hay bale"):
        return "TIGHTLY_TIED_HAY_BALE"

    #Carrot
    if (name == "carrot"):
        return "CARROT_ITEM"
    if (name == "enchanted carrot") or (name=="ecarrot"):
        return "ENCHANTED_CARROT"
    if (name == "ecarrot stick") or (name=="enchanted carrot on a stick") or (name == "estick"):
        return "ENCHANTED_CARROT_ON_A_STICK"
    if (name == "egolden carrot") or (name == "enchanted golden carrot"):
        return "ENCHANTED_GOLDEN_CARROT"

    #Potato
    if (name == "potato"):
        return "POTATO_ITEM"
    if (name == "enchanted potato") or (name =="epotato"):
        return "ENCHANTED_POTATO"
    if (name == "enchanted baked potato") or (name=="baked potato") or (name=="ebaked"):
        return "ENCHANTED_BAKED_POTATO"

    #Pumpkin
    if (name =="pumpkin"):
        return "PUMPKIN"
    if (name == "enchanted pumpkin") or (name == "epumpkin") or (name == "epump"):
        return "ENCHANTED_PUMPKIN"
    if (name =="polished pumpkin"):
        return "POLISHED_PUMPKIN"

    #Melon
    if (name =="melon"):
        return "MELON"
    if (name =="enchanted melon") or (name =="emelon"):
        return "ENCHANTED_MELON"
    if (name =="enchanted glistering melon") or (name =="eglistering"):
        return "ENCHANTED_GLISTERING_MELON"
    if (name =="enchanted melon block") or (name=="emelon block"):
        return "ENCHANTED_MELON_BLOCK"

    #Seeds
    if (name=="seeds"):
        return "SEEDS"
    if (name=="enchanted seeds") or (name=="eseeds"):
        return "ENCHANTED_SEEDS"

    #Red Mushrooms
    if (name=="red mushroom") or (name=="rmushroom") or (name=="rshroom"):
        return "RED_MUSHROOM"
    if (name=="enchanted red mushroom") or (name=="ered mushroom") or (name=="eredmushroom") or (name=="ershroom"):
        return "ENCHANTED_RED_MUSHROOM"
    if (name=="red mushroom block") or (name=="rmushroom block") or (name=="rshroom block"):
        return "HUGE_MUSHROOM_2"
    if (name=="enchanted red mushroom block") or (name=="ered mushroom block") or (name=="ershroom block"):
        return "ENCHANTED_HUGE_MUSHROOM_2"

    #Brown Mushrooms
    if (name=="brown mushroom") or (name=="bmushroom") or (name=="bshroom"):
        return "BROWN_MUSHROOM"
    if (name=="enchanted brown mushroom") or (name=="ebrown mushroom") or (name=="ebrownmushroom") or (name=="ebshroom"):
        return "ENCHANTED_BROWN_MUSHROOM"
    if (name=="brown mushroom block") or (name=="bmushroom block") or (name=="bshroom block"):
        return "HUGE_MUSHROOM_1"
    if (name=="enchanted brown mushroom block") or (name=="ebrown mushroom block") or (name=="ershroom block"):
        return "ENCHANTED_HUGE_MUSHROOM_1"

    #Cocoa Beans
    if (name=="cocoa beans") or (name=="cocoa") or (name=="beans") or (name=="bean"):
        return "INK_SACK:3"
    if (name=="enchanted cocoa beans") or (name=="ecocoa beans") or (name=="ecocoa") or (name=="ebean") or (name=="ebeans"):
        return "ENCHANTED_COCOA"
    if (name=="enchanted cookie") or (name=="ecookie"):
        return "ENCHANTED_COOKIE"

    #Cactus
    if (name=="cactus"):
        return "CACTUS"
    if (name=="enchanted cactus green") or (name=="cactus green") or (name=="ecactus green"):
        return "ENCHANTED_CACTUS_GREEN"
    if (name=="enchanted cactus") or (name=="enchanted cactus block") or (name =="ecactus"):
        return "ENCHANTED_CACTUS"

    #Sugar Cane
    if (name=="cane") or (name=="sugar cane"):
        return "SUGAR_CANE"
    if (name=="enchanted sugar") or (name=="esugar") or (name=="sugar"):
        return "ENCHANTED_SUGAR"
    if (name=="enchanted paper") or (name=="epaper") or (name=="paper"):
        return "ENCHANTED_PAPER"
    if (name=="enchanted sugar cane") or (name=="ecane"):
        return "ENCHANTED_SUGAR_CANE"

    #Feathers
    if (name=="feather") or (name=="feathers"):
        return "FEATHER"
    if (name=="enchanted feather") or (name=="efeather"):
        return "ENCHANTED_FEATHER"

    #leather&Beef
    if (name=="leather"):
        return "LEATHER"
    if (name=="enchanted leather") or (name=="eleather"):
        return "ENCHANTED_LEATHER"
    if (name=="raw beef") or (name=="beef"):
        return "RAW_BEEF"
    if (name=="enchanted raw beef") or (name=="ebeef"):
        return "ENCHANTED_RAW_BEEF"

    #Pork
    if (name=="pork"):
        return "PORK"
    if (name=="enchanted pork") or (name=="epork"):
        return "ENCHANTED_PORK"
    if (name=="enchanted grilled pork") or (name=="egrilled"):
        return "ENCHANTED_GRILLED_PORK"

    #Chicken&Eggs
    if (name=="raw chicken") or (name=="chicken"):
        return "RAW_CHICKEN"
    if (name=="enchanted raw chicken") or (name=="eraw chicken") or (name=="echicken"):
        return "ENCHANTED_RAW_CHICKEN"
    if (name=="enchanted egg") or (name=="eegg"):
        return "ENCHANTED_EGG"
    if (name=="enchanted cake") or (name=="ecake"):
        return "ENCHANTED_CAKE"
    if (name=="super enchanted egg") or (name=="seegg") or (name=="segg") or (name=="pet egg"):
        return "SUPER_EGG"

    #Mutton
    if (name=="raw mutton") or (name=="mutton"):
        return "MUTTON"
    if (name=="enchanted mutton") or (name=="emutton"):
        return "ENCHANTED_MUTTON"
    if (name=="enchanted cooked mutton") or (name=="egrilledmutton") or (name=="ecookedmutton"):
        return "ENCHANTED_COOKED_MUTTON"

    #Rabbit
    if (name=="raw rabbit") or (name=="rabbit"):
        return "RABBIT"
    if (name=="enchanted raw rabbit") or (name=="erabbit") or (name=="erawrabbit"):
        return "ENCHANTED_RABBIT"
    if (name=="rabbit's foot") or (name=="rabbits foot") or (name=="foot"):
        return "RABBIT_FOOT"
    if (name=="rabbit hide") or (name=="hide"):
        return "RABBIT_HIDE"
    if (name=="enchanted rabbit's foot") or (name=="enchanted rabbit foot") or (name=="efoot"):
        return "ENCHANTED_RABBIT_FOOT"
    if (name=="enchanted rabbit hide") or (name=="erabbithide") or(name=="ehide"):
        return "ENCHANTED_RABBIT_HIDE"

    #Netherwarts
    if (name=="nether wart") or (name=="wart") or (name=="warts"):
        return "NETHER_STALK"
    if (name=="enchanted nether wart") or (name=="ewart") or (name=="ewarts"):
        return "ENCHANTED_NETHER_STALK"
    if (name=="mutant nether wart") or (name=="mutant wart") or (name=="mutant"):
        return "MUTANT_NETHER_STALK"


    #mining

    #Cobble
    if (name=="cobblestone") or (name=="cobble"):
        return "COBBLESTONE"
    if (name=="enchanted cobblestone") or (name=="ecobble"):
        return "ENCHANTED_COBBLESTONE"

    #Coal
    if (name=="coal"):
        return "COAL"
    if (name=="enchanted coal") or (name=="ecoal"):
        return "ENCHANTED_COAL"
    if (name=="enchanted charcoal") or (name=="echarcoal") or (name=="charcoal"):
        return "ENCHANTED_CHARCOAL"
    if (name=="enchanted coal block") or (name=="coal block") or (name=="ecoal block") or (name=="ecoalblock"):
        return "ENCHANTED_COAL_BLOCK"

    #Iron
    if (name=="iron") or (name=="iron ingot"):
        return "IRON_INGOT"
    if (name=="enchanted iron") or (name=="eiron") or (name=="eiron ingot"):
        return "ENCHANTED_IRON"
    if (name=="enchanted iron block") or (name=="eiron block") or (name=="eironblock") or (name=="iron block"):
        return "ENCHANTED_IRON_BLOCK"

    #Gold
    if (name=="gold") or (name=="gold ingot"):
        return "GOLD_INGOT"
    if (name=="enchanted gold") or (name=="egold") or (name=="egold_ingot"):
        return "ENCHANTED_GOLD"
    if (name=="enchanted gold block") or (name=="egold block") or (name=="egoldblock") or (name=="gold block"):
        return "ENCHANTED_GOLD_BLOCK"

    #Diamond
    if (name=="diamond"):
        return "DIAMOND"
    if (name=="enchanted diamond") or (name=="egold"):
        return "ENCHANTED_DIAMOND"
    if (name=="enchanted diamond block") or (name=="ediamond block") or (name=="ediamondblock") or (name=="diamond block"):
        return "ENCHANTED_DIAMOND_BLOCK"

    #Lapis
    if (name=="lapis") or (name=="lapis_lazuli"):
        return "INK_SACK:4"
    if (name=="enchanted lapis lazuli") or (name=="elapis") or (name=="enchanted lapis"):
        return "ENCHANTED_LAPIS_LAZULI"
    if (name=="enchanted lapis block") or (name=="elapis block") or (name=="elapisblock") or (name=="lapis block") or (name=="lapisblock"):
        return "ENCHANTED_LAPIS_LAZULI_BLOCK"

    #Emerald
    if (name=="emerald"):
        return "EMERALD"
    if (name=="enchanted emerald") or (name=="eemerald"):
        return "ENCHANTED_EMERALD"
    if (name=="enchanted emerald block") or (name=="eemerald block") or (name=="eemeraldblock") or (name=="emerald block"):
        return "ENCHANTED_EMERALD_BLOCK"

    #Redstone
    if (name=="redstone") or (name=="red dust") or (name=="red"):
        return "REDSTONE"
    if (name=="enchanted redstone") or (name=="eredstone") or (name=="ered"):
        return "ENCHANTED_REDSTONE"
    if (name=="enchanted redstone block") or (name=="eredstone block") or (name=="ered block") or (name=="redblock"):
        return "ENCHANTED_REDSTONE_BLOCK"

    #Quartz
    if (name=="quartz"):
        return "QUARTZ"
    if (name=="enchanted quartz") or (name=="equartz"):
        return "ENCHANTED_QUARTZ"
    if (name=="enchanted quartz block") or (name=="equartz block") or (name=="equartzblock") or (name=="quartz block"):
        return "ENCHANTED_QUARTZ_BLOCK"

    #Obsidian
    if (name=="obsidian") or (name=="obi"):
        return "OBSIDIAN"
    if (name=="enchanted obsidian") or (name=="eobsidian") or (name=="eobi"):
        return "ENCHANTED_OBSIDIAN"

    #Glowstone
    if (name=="glowstone dust") or (name=="glow") or (name=="glowstone"):
        return "GLOWSTONE_DUST"
    if (name=="enchanted glowstone dust") or (name=="eglowdust"):
        return "ENCHANTED_GLOWSTONE_DUST"
    if (name=="enchanted glowstone") or (name=="glowstone block") or (name=="enchanted glowstone block") or (name=="eglowblock"):
        return "ENCHANTED_GLOWSTONE"
    if (name=="enchanted redstone lamp") or (name=="elamp"):
        return "ENCHANTED_REDSTONE_LAMP"

    #Gravel
    if (name=="gravel"):
        return "GRAVEL"

    #Flint
    if (name=="flint"):
        return "FLINT"
    if (name=="enchanted flint") or (name=="eflint"):
        return "ENCHANTED_FLINT"

    #Ice
    if (name=="ice"):
        return "ICE"
    if (name=="packed ice") or (name=="packed"):
        return "PACKED_ICE"
    if (name=="enchanted ice") or (name=="eice"):
        return "ENCHANTED_ICE"
    if (name=="enchanted packed ice") or (name=="epacked"):
        return "ENCHANTED_PACKED_ICE"

    #Netherrack
    if (name=="netherrack"):
        return "NETHERRACK"

    #Sand
    if (name=="sand"):
        return "SAND"
    if (name=="enchanted sand") or (name=="esand"):
        return "ENCHANTED_SAND"

    #Endstone
    if (name=="endstone"):
        return "ENDER_STONE"
    if (name=="enchanted endsstone") or (name=="eendstone"):
        return "ENCHANTED_ENDSTONE"

    #Snow
    if (name=="snowball") or (name=="snow ball"):
        return "SNOW_BALL"
    if (name=="snowblock") or (name=="snow") or (name=="snow block"):
        return "SNOW_BLOCK"
    if (name=="enchanted snow block") or (name=="esnow") or (name=="esnow block") or (name=="esnowblock"):
        return "ENCHANTED_SNOW_BLOCK"

    #Combat

    #Rotten Flesh
    if (name=="rotten flesh"):
        return "ROTTEN_FLESH"
    if (name=="enchanted rotten flesh") or (name=="eflesh") or (name=="erotten flesh"):
        return "ENCHANTED_ROTTEN_FLESH"

    #Bone
    if (name=="bone"):
        return "BONE"
    if (name=="enchanted bone") or (name=="ebone"):
        return "ENCHANTED_BONE"
    if (name=="enchanted bone block") or (name=="bone block") or (name=="ebone block"):
        return "ENCHANTED_BONE_BLOCK"

    #String
    if (name=="string"):
        return "STRING"
    if (name=="enchanted string") or (name=="estring"):
        return "ENCHANTED_STRING"

    #Spider eye
    if (name=="spider eye"):
        return "SPIDER_EYE"
    if (name=="enchanted spider eye") or (name=="espider"):
        return "ENCHANTED_SPIDER_EYE"
    if (name=="enchanted fermented spider eye") or (name=="efermented") or (name=="fermented"):
        return "ENCHANTED_FERMENTED_SPIDER_EYE"

    #Gunpowder
    if (name=="gunpowder"):
        return "SULPHUR"
    if (name=="enchanted gunpowder") or (name=="egunpoweder"):
        return "ENCHANTED_GUNPOWDER"
    if (name=="enchanted firework rocket") or (name=="firework") or (name=="efirework"):
        return "ENCHANTED_FIREWORK_ROCKET"

    #Enderpearl
    if (name=="ender pearl") or (name=="pearl"):
        return "ENDER_PEARL"
    if (name=="enchanted ender pearl") or (name=="epearl"):
        return "ENCHANTED_ENDER_PEARL"
    if (name=="enchanted eye of ender") or (name=="ender"):
        return "ENCHANTED_EYE_OF_ENDER"

    #Ghast Tear
    if (name=="ghast tear"):
        return "GHAST_TEAR"
    if (name=="enchanted ghast tear") or (name=="etear"):
        return "ENCHANTED_GHAST_TEAR"

    #Slime ball
    if (name=="slimeball"):
        return "SLIME_BALL"
    if (name=="enchanted slimeball") or (name=="eslimeball"):
        return "ENCHANTED_SLIME_BALL"
    if (name=="enchanted slime block") or (name=="eslimeblock") or (name=="eslime block"):
        return "ENCHANTED_SLIME_BLOCK"

    #Blaze
    if (name=="blazerod"):
        return "BLAZE_ROD"
    if (name=="enchanted blaze powder") or (name=="eblaze powder"):
        return "ENCHANTED_BLAZE_POWDER"
    if (name=="enchanted blaze rod") or (name=="eblaze rod"):
        return "ENCHANTED_BLAZE_ROD"

    #Magma Cream
    if (name=="magma cream"):
        return "MAGMA_CREAM"
    if (name=="enchanted magma cream") or (name=="emagma") or (name=="enchanted magma"):
        return "ENCHANTED_MAGMA_CREAM"

    #Mythological
    if (name=="griffin feather") or (name=="griffin"):
        return "GRIFFIN_FEATHER"
    if (name=="daedalus stick") or (name=="daedalus"):
        return "DAEDALUS_STICK"
    if (name=="ancient claw") or (name=="ancient") or (name=="claw"):
        return "ANCIENT_CLAW"
    if (name=="enchanted ancient claw") or (name=="eancient") or (name=="eclaw"):
        return "ENCHANTED_ANCIENT_CLAW"

    #Revenant flesh
    if (name=="revenant flesh") or (name=="revenant") or (name=="rev flesh") or (name=="rev"):
        return "REVENANT_FLESH"
    if (name=="revenant viscera") or (name=="viscera"):
        return "REVENANT_VISCERA"

    #Tarantula Web
    if (name=="tarantula web") or (name=="web") or (name=="tarantula"):
        return "TARANTULA_WEB"
    if (name=="tarantula silk") or (name=="silk"):
        return "TARANTULA_SILK"

    #Wolf Tooth
    if (name=="wolf tooth") or (name=="wolf") or (name=="tooth"):
        return "WOLF_TOOTH"
    if (name=="golden tooth") or (name=="golden teeth"):
        return "GOLDEN_TOOTH"

    #Woods&Fishes

    #Oak
    if (name=="oak log") or (name=="oak") or (name=="oak wood"):
        return "LOG"
    if (name=="enchanted oak log") or (name=="eoak") or (name=="eoak wood"):
        return "ENCHANTED_OAK_LOG"

    #Spruce
    if (name=="spruce log") or (name=="spruce") or (name=="spruce wood"):
        return "LOG:1"
    if (name=="enchanted spruce log") or (name=="espruce") or (name=="espruce wood"):
        return "ENCHANTED_SPRUCE_LOG"

    #Birch
    if (name=="birch log") or (name=="birch") or (name=="birch wood"):
        return "LOG:2"
    if (name=="enchanted birch log") or (name=="ebirch") or (name=="ebirch wood"):
        return "ENCHANTED_BIRCH_LOG"

    #Dark Oak
    if (name=="darkoak log") or (name=="darkoak") or (name=="darkoak wood") or (name=="doak log") or (name=="doak") or (name=="doak wood"):
        return "LOG_2:1"
    if (name=="enchanted darkoak log") or (name=="edarkoak") or (name=="edarkoak wood") or (name=="edoak log") or (name=="edoak") or (name=="edoak wood"):
        return "ENCHANTED_DARK_OAK_LOG"

    #Acacia
    if (name=="acacia log") or (name=="acacia") or (name=="acacia wood"):
        return "LOG_2"
    if (name=="enchanted acacia log") or (name=="eacacia") or (name=="eacacia wood"):
        return "ENCHANTED_ACACIA_LOG"

    #Jungle
    if (name=="jungle log") or (name=="jungle") or (name=="jungle wood"):
        return "LOG:3"
    if (name=="enchanted jungle log") or (name=="ejungle") or (name=="ejungle wood"):
        return "ENCHANTED_JUNGLE_LOG"

    #Raw Fish
    if (name=="raw fish") or (name=="fish"):
        return "RAW_FISH"
    if (name=="enchanted raw fish") or (name=="efish"):
        return "ENCHANTED_RAW_FISH"
    if (name=="enchanted cooked fish") or (name=="ecooked fish"):
        return "ENCHANTED_COOKED_FISH"

    #Salmon
    if (name=="salmon"):
        return "RAW_FISH:1"
    if (name=="enchanted salmon") or (name=="esalmon"):
        return "ENCHANTED_RAW_SALMON"
    if (name=="enchanted cooked salmon") or (name=="ecooked salmon"):
        return "ENCHANTED_COOKED_SALMON"

    #Clownfish
    if (name=="clownfish") or (name=="clown"):
        return "RAW_FISH:2"
    if (name=="enchanted clownfish") or (name=="eclownfish") or (name=="eclown"):
        return "ENCHANTED_CLOWNFISH"

    #Pufferfish
    if (name=="pufferfish") or (name=="puffer"):
        return "RAW_FISH:3"
    if (name=="enchanted pufferfish") or (name=="epufferfish") or (name=="epuffer"):
        return "ENCHANTED_PUFFERFISH"

    #Prismarine Shard
    if (name=="prismarine shard") or (name=="pris shard"):
        return "PRISMARINE_SHARD"
    if (name=="enchanted prismarine shard") or (name=="eprismarineshard") or (name=="eprismarine shard") or (name=="epris shard"):
        return "ENCHANTED_PRISMARINE_SHARD"

    #Prismarine Crystal
    if (name=="prismarine crystal") or (name=="pris crystal"):
        return "PRISMARINE_CRYSTALS"
    if (name=="enchanted prismarine shard") or (name=="eprismarineshard") or (name=="eprismarine shard") or (name=="epris shard"):
        return "ENCHANTED_PRISMARINE_CRYSTALS"

    #Clay
    if (name=="clay"):
        return "CLAY_BALL"
    if (name=="enchanted clay") or (name=="eclay"):
        return "ENCHANTED_CLAY_BALL"

    #Lily pad
    if (name=="lilypad") or (name=="lily"):
        return "WATER_LILY"
    if (name=="enchanted lilypad") or (name=="elilypad") or (name=="elily"):
        return "ENCHANTED_WATER_LILY"

    #INK
    if (name=="ink sack") or (name=="ink"):
        return "INK_SACK"
    if (name=="enchanted ink sack") or (name=="eink"):
        return "ENCHANTED_INK_SACK"

    #Sponge
    if (name=="sponge"):
        return "SPONGE"
    if (name=="enchanted sponge") or (name=="esponge"):
        return "ENCHANTED_SPONGE"
    if (name=="enchanted wet sponge") or (name=="ewet") or (name=="ewet sponge") or (name=="wet sponge"):
        return "ENCHANTED_WET_SPONGE"

    #Baits
    if (name=="carrot bait"):
        return "CARROT_BAIT"
    if (name=="minnow bait"):
        return "MINNOW_BAIT"
    if (name=="fish bait"):
        return "FISH_BAIT"
    if (name=="light bait"):
        return "LIGHT_BAIT"
    if (name=="dark bait"):
        return "DARK_BAIT"
    if (name=="spooky bait"):
        return "SPOOKY_BAIT"
    if (name=="spiked bait"):
        return "SPIKED_BAIT"
    if (name=="blessed bait"):
        return "BLESSED_BAIT"
    if (name=="ice bait"):
        return "ICE_BAIT"
    if (name=="whale bait"):
        return "WHALE_BAIT"
    if (name=="shark bait"):
        return "SHARK_BAIT"

    #Fishing Festival
    if (name=="nurse shark tooth") or (name=="nurse shark") or (name=="nurse"):
        return "NURSE_SHARK_TOOTH"
    if (name=="blue shark tooth") or (name=="blue shark") or (name=="blue"):
        return "BLUE_SHARK_TOOTH"
    if (name=="tiger shark tooth") or (name=="tiger shark") or (name=="tiger"):
        return "TIGER_SHARK_TOOTH"
    if (name=="great white shark tooth") or (name=="great white shark") or (name=="great white"):
        return "GREAT_WHITE_SHARK_TOOTH"
    if (name=="shark_fin") or (name=="fin"):
        return "SHARK_FIN"
    if (name=="enchanted shark fin") or (name=="efin"):
        return "ENCHANTED_SHARK_FIN"

    #Oddities

    #Booster Cookie

    if (name=="booster cookie") or (name=="booster") or (name=="bits"):
        return "BOOSTER_COOKIE"

    #Hot Potato Book
    if (name=="hot potato book") or (name=="hpb"):
        return "HOT_POTATO_BOOK"
    if (name=="fuming potato book") or (name=="fpb") or (name=="fuming"):
        return "FUMING_POTATO_BOOK"

    #Compactor
    if (name=="compactor"):
        return "COMPACTOR"
    if (name=="super compactor 3000") or (name=="super compactor"):
        return "SUPER_COMPACTOR_3000"

    #Summoning Eye:
    if (name=="summoning eye") or (name=="eye") or (name=="summoning eyes") or (name=="eyes"):
        return "SUMMONING_EYE"

    #Dragon Fragments
    if (name=="protector dragon fragment") or (name=="protector"):
        return "PROTECTOR_FRAGMENT"
    if (name=="old dragon fragment") or (name=="old"):
        return "OLD_FRAGMENT"
    if (name=="unstable dragon fragment") or (name=="unstable"):
        return "UNSTABLE_FRAGMENT"
    if (name=="strong dragon fragment") or (name=="strong"):
        return "STRONG_FRAGMENT"
    if (name=="young dragon fragment") or (name=="young"):
        return "YOUNG_FRAGMENT"
    if (name=="wise dragon fragment") or (name=="wise"):
        return "WISE_FRAGMENT"
    if (name=="superior dragon fragment") or (name=="superior"):
        return "SUPERIOR_FRAGMENT"
    if (name=="holy dragon fragment") or (name=="holy"):
        return "HOLY_FRAGMENT"

    #Fuels
    if (name=="enchanted lava bucket") or (name=="elava"):
        return "ENCHANTED_LAVA_BUCKET"
    if (name=="hamster wheel") or (name=="hamster") or (name=="wheel"):
        return "HAMSTER_WHEEL"
    if (name=="foul flesh") or (name=="foul"):
        return "FOUL_FLESH"
    if (name=="catalyst") or (name=="cata"):
        return "CATALYST"
    if (name=="hyper catalyst") or (name=="hyper") or (name=="hyper cata"):
        return "HYPER_CATALYST"

    #Sooky
    if (name=="green candy") or (name=="green"):
        return "GREEN_CANDY"
    if (name=="purple candy") or (name=="purple"):
        return "PURPLE_CANDY"
    if (name=="ectoplasm") or (name=="ecto"):
        return "ECTOPLASM"
    if (name=="pumpkin guts") or (name=="guts") or (name=="gut"):
        return "PUMPKIN_GUTS"
    if (name == "spooky shard") or (name=="spooky") or (name=="shard"):
        return "SPOOKY_SHARD"
    if (name=="werewolf skin") or (name=="werewolf") or (name=="skin"):
        return "WEREWOLF_SKIN"
    if (name=="soul fragment") or (name=="soul"):
        return "SOUL_FRAGMENT"

    #Gifts
    if (name=="white gift") or (name=="wgift"):
        return "WHITE_GIFT"
    if (name=="green gift") or (name=="ggift"):
        return "GREEN_GIFT"
    if (name=="red gift") or (name=="rgift"):
        return "RED_GIFT"

    #Refined Mineral
    if (name=="refined mineral") or (name=="refined") or (name=="mineral"):
        return "REFINED_MINERAL"

    #Recombobulator
    if (name=="recombobulator 3000") or (name=="recomb") or (name=="recombobulator") or (name=="bob"):
        return "RECOMBOBULATOR_3000"

    #Jacob's tickets
    if (name=="jacob's ticket") or (name=="ticket") or (name=="jacob"):
        return "JACOBS_TICKET"

    #EXP Bottles
    if (name=="experience bottle") or (name=="bottle") or (name=="xp bottle"):
        return "EXP_BOTTLE"
    if (name=="grand experience bottle") or (name=="grand"):
        return "GRAND_EXP_BOTTLE"
    if (name=="titanic experience bottle") or (name=="titanic"):
        return "TITANIC_EXP_BOTTLE"
    if (name=="colossal experience bottle") or (name=="colossal"):
        return "COLOSSAL_EXP_BOTTLE"

    #Stock of Stonks
    if (name=="stock of stonks") or (name=="stock") or (name=="stonks") or (name=="stonk"):
        return "STOCK_OF_STONKS"


    #Jerry Boxes
    if (name=="green jerry box") or (name=="green box") or (name=="green jerry"):
        return "JERRY_BOX_GREEN"
    if (name=="blue jerry box") or (name=="blue box") or (name=="blue jerry"):
        return "JERRY_BOX_BLUE"
    if (name=="purple jerry box") or (name=="purple box") or (name=="purple jerry"):
        return "JERRY_BOX_PURPLE"
    if (name=="golden jerry box") or (name=="gold jerry box") or (name=="gold box") or (name=="gold jerry") or (name=="golden jerry"):
        return "JERRY_BOX_GOLDEN"

    #Mining Update
    if (name=="mithril"):
        return "MITHRIL_ORE"
    if (name=="refined mithril"):
        return "REFINED_MITHRIL"
    if (name=="titanium"):
        return "TITANIUM_ORE"
    if (name=="refined titanium"):
        return "REFINED_TITANIUM"
    if (name=="starfall"):
        return "STARFALL"
    if (name=="etitanium") or (name=="enchanted titanium"):
        return "ENCHANTED_TITANIUM"
    if (name=="emithril") or (name=="enchanted mithril"):
        return "ENCHANTED_MITHRIL"

    else:
        raise ItemNotFound

def quickInfo(name):
    data = requests.get("https://api.hypixel.net/skyblock/bazaar").json()
    data = data["products"][name]

    sell_price = "{:,}".format(round(data["sell_summary"][0]["pricePerUnit"],3))
    buy_price = "{:,}".format(round(data["buy_summary"][0]["pricePerUnit"],3))

    sold_per_week = "{:,}".format(data["quick_status"]["sellMovingWeek"])
    buy_per_week = "{:,}".format(data["quick_status"]["buyMovingWeek"])
    market_volume = "{:,}".format(data["quick_status"]["sellVolume"])
    buy_orders = "{:,}".format(data["quick_status"]["buyOrders"])
    sell_orders  = "{:,}".format(data["quick_status"]["sellOrders"])


    message = f"**Market Volume: ** {market_volume}\n\n"
    message += f"**Buy Price: ** {buy_price}\n"
    message += f"**Sell Price: ** {sell_price}\n"
    message += f"\n**Buy Orders:** {buy_orders}\n"
    message += f"**Sell Orders: ** {sell_orders}\n"
    message += f"\n**Items Bought in Last 7 Days:** {buy_per_week}\n"
    message += f"**Items Sold in Last 7 Days:** {sold_per_week}"

    return message
