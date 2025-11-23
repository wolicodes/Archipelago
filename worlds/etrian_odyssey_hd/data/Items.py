
from enum import Enum
from BaseClasses import Item, ItemClassification

class Items(str, Enum):
    KNIFE = "Knife"
    SCRAMASAX = "Scramasax"
    DAGGER = "Dagger"
    SHORTSWORD = "Shortsword"
    BOAR_SPEAR = "Boar Spear"
    BROADSWORD = "Broadsword"
    RAPIER = "Rapier"
    VIKING = "Viking"
    SHAMSHIR = "Shamshir"
    CLAYMORE = "Claymore"
    EXECUTOR = "Executor"
    KATZBALGER = "Katzbalger"
    STEELSWORD = "Steelsword"
    EPEE = "Epee"
    LAST_ESTOC = "Last Estoc"
    PATTISA = "Pattisa"
    FLAMBERGE = "Flamberge"
    DUERGAR = "Duergar"
    DRAGONBANE = "Dragonbane"
    BONE_AXE = "Bone Axe"
    HAND_AXE = "Hand Axe"
    CELTIS = "Celtis"
    BROADAXE = "Broadaxe"
    BATTLE_AXE = "Battle Axe"
    BILIOMG = "Biliomg"
    TABAR = "Tabar"
    GREAT_AXE = "Great Axe"
    BARDICHE = "Bardiche"
    HALBERD = "Halberd"
    WAND = "Wand"
    BREAKER = "Breaker"
    LABYRIS = "Labyris"
    FRANCISCA = "Francisca"
    BHUJ = "Bhuj"
    FASCES_AXE = "Fasces Axe"
    FLAME_AXE = "Flame Axe"
    METEOR_AXE = "Meteor Axe"
    HATCHET = "Hatchet"
    STAFF = "Staff"
    BONE_STAFF = "Bone Staff"
    BONE_MACE = "Bone Mace"
    DOWN_STAFF = "Down Staff"
    BONE_FLAIL = "Bone Flail"
    GEM_STAFF = "Gem Staff"
    WAR_MACE = "War Mace"
    LUCK_STAFF = "Luck Staff"
    GODENDAG = "Godendag"
    MYSTIC_ROD = "Mystic Rod"
    WARHAMMER = "Warhammer"
    ARCANA_ROD = "Arcana Rod"
    SAGE_WAND = "Sage Wand"
    WAKIZASHI = "Wakizashi"
    UCHIGATANA = "Uchigatana"
    OHDACHI = "Ohdachi"
    KOGARASU = "Kogarasu"
    SHIDA = "Shida"
    ZANMATOU = "Zanmatou"
    KUZUNOSADA = "Kuzunosada"
    HACHI = "Hachi"
    HISAMEMARU = "Hisamemaru"
    MASAMUNE = "Masamune"
    WOOD_BOW = "Wood Bow"
    ENAMEL_BOW = "Enamel Bow"
    SHORT_BOW = "Short Bow"
    BEAST_BOW = "Beast Bow"
    HARD_SLING = "Hard Sling"
    LONG_BOW = "Long Bow"
    HINDI = "Hindi"
    SELF_BOW = "Self Bow"
    HUNTER_BOW = "Hunter Bow"
    FIN_BOW = "Fin Bow"
    VINE_BOW = "Vine Bow"
    HEAVEN_BOW = "Heaven Bow"
    SHIDGEDOU = "Shidgedou"
    WAR_BOW = "War Bow"
    ARBALEST = "Arbalest"
    FAILNAUGHT = "Failnaught"
    ZAMIEL_BOW = "Zamiel Bow"
    ARC_DRAWER = "Arc Drawer"
    LIGHT_WHIP = "Light Whip"
    FANG_WHIP = "Fang Whip"
    BULLWHIP = "Bullwhip"
    VINE_WHIP = "Vine Whip"
    NAIL_WHIP = "Nail Whip"
    EDGE_WHIP = "Edge Whip"
    TOXIC_WHIP = "Toxic Whip"
    GUM_WHIP = "Gum Whip"
    WIND_WHIP = "Wind Whip"
    SHRED_WHIP = "Shred Whip"
    STING_WHIP = "Sting Whip"
    BLADE_WHIP = "Blade Whip"
    NINE_TAILS = "Nine Tails"
    KNOUT = "Knout"
    DEAD_WHIP = "Dead Whip"
    TORMENTOR = "Tormentor"
    DOMINATOR = "Dominator"
    VOLT_WHIP = "Volt Whip"
    THORN_WHIP = "Thorn Whip"
    TWEED = "Tweed"
    JERKIN = "Jerkin"
    LEAF_COAT = "Leaf Coat"
    HIDE_VEST = "Hide Vest"
    HIDE_ARMOR = "Hide Armor"
    PLATE = "Plate"
    DOUBLET = "Doublet"
    BUFFCOAT = "Buffcoat"
    BRIAULT = "Briault"
    CHAIN_MAIL = "Chain Mail"
    PETAL_COAT = "Petal Coat"
    LEAF_TUNIC = "Leaf Tunic"
    IRON_PLATE = "Iron Plate"
    RING_MAIL = "Ring Mail"
    OAK_JACKET = "Oak Jacket"
    WING_COAT = "Wing Coat"
    HAUBERK = "Hauberk"
    STUD_VEST = "Stud Vest"
    FANCY_COAT = "Fancy Coat"
    COTARDIE = "Cotardie"
    FULL_ARMOR = "Full Armor"
    PLATE_MAIL = "Plate Mail"
    SEVEN_DOUBLET = "7 Doublet"
    SURCOAT = "Surcoat"
    TIGER_COAT = "Tiger Coat"
    FAIRY_ROBE = "Fairy Robe"
    DARK_TUNIC = "Dark Tunic"
    BRIGANDINE = "Brigandine"
    EBON_PLATE = "Ebon Plate"
    LYCORIS = "Lycoris"
    WYVERNMAIL = "Wyvernmail"
    JAZERAINT = "Jazeraint"
    DEMON_COAT = "Demon Coat"
    RUNE_TWEED = "Rune Tweed"
    RUNE_TUNIC = "Rune Tunic"
    BLOOD_MAIL = "Blood Mail"
    COMPOSITE = "Composite"
    AZURE_COAT = "Azure Coat"
    BLOOD_COAT = "Blood Coat"
    DINO_PLATE = "Dino Plate"
    DEMON_MAIL = "Demon Mail"
    SYLPHEED = "Sylpheed"
    HOLY_ARMOR = "Holy Armor"
    GHOST_VEST = "Ghost Vest"
    MOBIUS_ALB = "Mobius Alb"
    ANGEL_ROBE = "Angel Robe"
    FAIRY_MAIL = "Fairy Mail"
    RUBY_MAIL = "Ruby Mail"
    HEX_MANTLE = "Hex Mantle"
    MOSS_COAT = "Moss Coat"
    FLAME_COAT = "Flame Coat"
    FROST_COAT = "Frost Coat"
    VOLT_COAT = "Volt Coat"
    HAIRPIN = "Hairpin"
    HIDE_HAT = "Hide Hat"
    PLUMED_HAT = "Plumed Hat"
    CHAIN_HELM = "Chain Helm"
    GUM_HELM = "Gum Helm"
    SCALE_HELM = "Scale Helm"
    SCALE_CAP = "Scale Cap"
    SANDY_PIN = "Sandy Pin"
    TIGER_CAP = "Tiger Cap"
    CIRCLET = "Circlet"
    BLOOD_HELM = "Blood Helm"
    ANGEL_HELM = "Angel Helm"
    KNIT_GLOVE = "Knit Glove"
    HIDE_GLOVE = "Hide Glove"
    DOWN_GLOVE = "Down Glove"
    IRON_GLOVE = "Iron Glove"
    BEAR_GLOVE = "Bear Glove"
    GUM_GLOVE = "Gum Glove"
    FANG_GLOVE = "Fang Glove"
    SAND_GLOVE = "Sand Glove"
    TIGER_HAND = "Tiger Hand"
    RUNE_GLOVE = "Rune Glove"
    BLOOD_GAGE = "Blood Gage"
    BRAVE_GAGE = "Brave Gage"
    EBON_GLOVE = "Ebon Glove"
    ATHANOR = "Athanor"
    RUBY_GAGE = "Ruby Gage"
    TOXIC_GAGE = "Toxic Gage"
    TARGE = "Targe"
    HIDE_ASPIS = "Hide Aspis"
    ASPIS = "Aspis"
    OVAL_ASPIS = "Oval Aspis"
    HEAT_ASPIS = "Heat Aspis"
    GUM_ASPIS = "Gum Aspis"
    BODY_ASPIS = "Body Aspis"
    EBON_ASPIS = "Ebon Aspis"
    MOON_ASPIS = "Moon Aspis"
    KING_ASPIS = "King Aspis"
    HALO_ASPIS = "Halo Aspis"
    HOLY_ASPIS = "Holy Aspis"
    PAIN_ASPIS = "Pain Aspis"
    LEAF_BOOT = "Leaf Boot"
    HIDE_BOOT = "Hide Boot"
    PLUME_BOOT = "Plume Boot"
    CHAIN_BOOT = "Chain Boot"
    MOCCASINS = "Moccasins"
    SCALE_BOOT = "Scale Boot"
    FAIRY_BOOT = "Fairy Boot"
    TIGER_BOOT = "Tiger Boot"
    FLAME_BOOT = "Flame Boot"
    FUR_BOOT = "Fur Boot"
    DYED_BOOT = "Dyed Boot"
    SPEED_BOOT = "Speed Boot"
    HIDE_BELT = "Hide Belt"
    HIDE_RING = "Hide Ring"
    RED_CHARM = "Red Charm"
    PETAL_RING = "Petal Ring"
    CUT_CHARM = "Cut Charm"
    GEM_RING = "Gem Ring"
    LEAF_CAPE = "Leaf Cape"
    FIRE_RING = "Fire Ring"
    STAR_CHARM = "Star Charm"
    TUSK_CHARM = "Tusk Charm"
    OLD_CHOKER = "Old Choker"
    HIDE_CAPE = "Hide Cape"
    AMBER_RING = "Amber Ring"
    SEA_CHARM = "Sea Charm"
    BLUE_RING = "Blue Ring"
    RED_CAPE = "Red Cape"
    EVIL_CHARM = "Evil Charm"
    ROSE_RING = "Rose Ring"
    ROYAL_RING = "Royal Ring"
    GOLD_CAPE = "Gold Cape"
    ANGEL_RING = "Angel Ring"
    WARD_GEM = "Ward Gem"
    JEWEL_EYE = "Jewel Eye"
    RUBY = "Ruby"
    SAPPHIRE = "Sapphire"
    TOPAZ = "Topaz"
    TOURMALINE = "Tourmaline"
    ADAMAS = "Adamas"
    HEX_DOLL = "Hex Doll"
    OCARINA = "Ocarina"
    LUTE = "Lute"
    FLUTE = "Flute"
    KITHARA = "Kithara"
    AULOS = "Aulos"
    ANGEL_HARP = "Angel Harp"
    SYRINX = "Syrinx"
    TOWN_MEDAL = "Town Medal"
    TOWN_CROWN = "Town Crown"
    MOSS_RING = "Moss Ring"
    MOSS_BAND = "Moss Band"
    SMALL_FANG = "Small Fang"
    SOFT_HIDE = "Soft Hide"
    BEAST_BONE = "Beast Bone"
    HARD_SHELL = "Hard Shell"
    BUG_WING = "Bug Wing"
    TINY_PETAL = "Tiny Petal"
    INSECT_EYE = "Insect Eye"
    HARE_TAIL = "Hare Tail"
    HORN = "Horn"
    HARDWOOD = "Hardwood"
    VINE = "Vine"
    CHARCOAL = "Charcoal"
    GUM_HIDE = "Gum Hide"
    THORN = "Thorn"
    METAL_HORN = "Metal Horn"
    STIFF_HIDE = "Stiff Hide"
    AMBER_LUMP = "Amber Lump"
    CRABAPPLE = "Crabapple"
    MUGWORT = "Mugwort"
    RED_FRUIT = "Red Fruit"
    WHITESTONE = "Whitestone"
    PYROXENE = "Pyroxene"
    GOLEM_ROCK = "Golem Rock"
    LARGE_FANG = "Large Fang"
    HUGE_FANG = "Huge Fang"
    WHITE_HIDE = "White Hide"
    SCYTHE = "Scythe"
    STICKY_GOO = "Sticky Goo"
    STEEL_LUMP = "Steel Lump"
    STINGER = "Stinger"
    STICKY_WEB = "Sticky Web"
    BENT_CLAW = "Bent Claw"
    LIGHT_WOOD = "Light Wood"
    DYE_PETAL = "Dye Petal"
    STARSEED = "Starseed"
    SCENT_WOOD = "Scent Wood"
    GUM_VINE = "Gum Vine"
    FEATHER = "Feather"
    TAILBONE = "Tailbone"
    CARMINITE = "Carminite"
    IRON_SHELL = "Iron Shell"
    THICK_LEAF = "Thick Leaf"
    BIRD_TALON = "Bird Talon"
    TIGER_FANG = "Tiger Fang"
    TIGER_FUR = "Tiger Fur"
    MINT_LEAF = "Mint Leaf"
    SCRAP_IRON = "Scrap Iron"
    FOSSIL = "Fossil"
    BEAR_FUR = "Bear Fur"
    BIRD_LIMB = "Bird Limb"
    THIN_SHELL = "Thin Shell"
    TOXIC_BARB = "Toxic Barb"
    SHARP_HORN = "Sharp Horn"
    TOUGH_WING = "Tough Wing"
    TOUGH_FANG = "Tough Fang"
    GREAT_TUSK = "Great Tusk"
    GUM_THROAT = "Gum Throat"
    ROCK_CORAL = "Rock Coral"
    ELASTIC = "Elastic"
    GLASS_EYE = "Glass Eye"
    STEEL_BONE = "Steel Bone"
    BONE_SHARD = "Bone Shard"
    CARAPACE = "Carapace"
    BUG_NEST = "Bug Nest"
    BAT_WING = "Bat Wing"
    SHINY_GOO = "Shiny Goo"
    SHRED_NAIL = "Shred Nail"
    RED_HIDE = "Red Hide"
    BLOOD_FANG = "Blood Fang"
    SWORDFISH_SCALE = "Swordfish Scale"
    SWORDFISH_FIN = "Swordfish Fin"
    CRAB_LEG = "Crab Leg"
    ANT_HONEY = "Ant Honey"
    STAB_SHELL = "Stab Shell"
    STRAWBERRY = "Strawberry"
    SEA_BRANCH = "Sea Branch"
    CORUNDUM = "Corundum"
    RED_BLADE = "Red Blade"
    DEATH_CLAW = "Death Claw"
    HUGE_FIN = "Huge Fin"
    HUNDRED_SHELL = "100 Shell"
    GATOR_SKIN = "Gator Skin"
    HEATED_FUR = "Heated Fur"
    FIRE_TAIL = "Fire Tail"
    WHITE_SKIN = "White Skin"
    WHITE_FANG = "White Fang"
    SHINY_HORN = "Shiny Horn"
    MUSK = "Musk"
    BROKEN_EYE = "Broken Eye"
    SILVER_EYE = "Silver Eye"
    NYX_SCYTHE = "Nyx Scythe"
    TENDON = "Tendon"
    DRIED_VINE = "Dried Vine"
    PURE_ROOT = "Pure Root"
    HARD_SHARD = "Hard Shard"
    INK_STICK = "Ink Stick"
    SAND_CLOTH = "Sand Cloth"
    SAND_TWIG = "Sand Twig"
    FAIRY_WING = "Fairy Wing"
    FAIRY_SAP = "Fairy Sap"
    RED_PLUME = "Red Plume"
    RED_BEAK = "Red Beak"
    DRY_PEACH = "Dry Peach"
    THROB_VINE = "Throb Vine"
    RED_STRING = "Red String"
    RED_THREAD = "Red Thread"
    OLEANDER = "Oleander"
    STEEL_CLAW = "Steel Claw"
    STEEL_CHIP = "Steel Chip"
    CULLINAN = "Cullinan"
    CORDYCEPS = "Cordyceps"
    SAP_WINE = "Sap Wine"
    SPACE_NAIL = "Space Nail"
    TINY_TOOTH = "Tiny Tooth"
    DEMON_FUR = "Demon Fur"
    REX_THROAT = "Rex Throat"
    GEM_CORE = "Gem Core"
    GUM_THREAD = "Gum Thread"
    RED_FUR = "Red Fur"
    RED_BLOOD = "Red Blood"
    GOLD_SHELL = "Gold Shell"
    BLUE_BLOOD = "Blue Blood"
    DEATH_STEM = "Death Stem"
    GOLD_FUR = "Gold Fur"
    GOLD_TUSK = "Gold Tusk"
    GOLD_HORN = "Gold Horn"
    SPACE_HUSK = "Space Husk"
    SPACE_CLAW = "Space Claw"
    ANGEL_WING = "Angel Wing"
    LIFE_HONEY = "Life Honey"
    STERNUM = "Sternum"
    CURSE_TUSK = "Curse Tusk"
    ROYAL_HIDE = "Royal Hide"
    SHROUD = "Shroud"
    RED_ORE = "Red Ore"
    AMBROSIA = "Ambrosia"
    HEADROOT = "Headroot"
    ARMROOT = "Armroot"
    LEGROOT = "Legroot"
    GUM_STRING = "Gum String"
    SHINY_VINE = "Shiny Vine"
    SHINY_SEED = "Shiny Seed"
    DRYWALL = "Drywall"
    CRYSTWALL = "Crystwall"
    JADE_ORE = "Jade Ore"
    AZURE_ORE = "Azure Ore"
    EVIL_SHELL = "Evil Shell"
    EVIL_SCALE = "Evil Scale"
    EVIL_PLUME = "Evil Plume"
    EVIL_CREST = "Evil Crest"
    OLD_SHELL = "Old Shell"
    GEM_SCALE = "Gem Scale"
    BLACK_ROOT = "Black Root"
    GEM_PLUME = "Gem Plume"
    HEX_MARROW = "Hex Marrow"
    GOLD_PLUME = "Gold Plume"
    HELL_WING = "Hell Wing"
    VELVET = "Velvet"
    HOLED_LIMB = "Holed Limb"
    RUBY_SKULL = "Ruby Skull"
    RUBY_BONE = "Ruby Bone"
    HEX_CHAIN = "Hex Chain"
    SWORD_RIB = "Sword Rib"
    FLAME_SKIN = "Flame Skin"
    FROST_SKIN = "Frost Skin"
    VOLT_SKIN = "Volt Skin"
    VOLT_CORE = "Volt Core"
    FIRE_SCALE = "Fire Scale"
    FIRE_FANG = "Fire Fang"
    STATUE_ARM = "Statue Arm"
    BEAST_EYE = "Beast Eye"
    FROST_BONE = "Frost Bone"
    DEMON_CORE = "Demon Core"
    EBON_PLUME = "Ebon Plume"
    SEA_KING_ICE = "Sea King Ice"
    BARBEL = "Barbel"
    ROYAL_VINE = "Royal Vine"
    HARVESTER = "Harvester"
    ROYAL_MANE = "Royal Mane"
    ICE_SCALE = "Ice Scale"
    WINE_WHIP = "Wine Whip"
    ROSE_WHIP = "Rose Whip"
    TOXIC_HAND = "Toxic Hand"
    VOLT_SCALE = "Volt Scale"
    YELLOW_ORE = "Yellow Ore"
    BUG_SCALE = "Bug Scale"
    COLD_SCALE = "Cold Scale"
    ODD_FRUIT = "Odd Fruit"
    CROSS_SEED = "Cross Seed"
    NARCISSUS = "Narcissus"
    MOSCHINO = "Moschino"
    SMALL_LEAF = "Small Leaf"
    MEDIUM_LEAF = "Medium Leaf"
    LARGE_LEAF = "Large Leaf"
    MEDICA = "Medica"
    MEDICA_II = "Medica II"
    MEDICA_III = "Medica III"
    MEDICA_IV = "Medica IV"
    MEDICA_V = "Medica V"
    AMRITA = "Amrita"
    AMRITA_II = "Amrita II"
    HAMAO = "Hamao"
    HAMAO_PRIME = "Hamao Prime"
    SOMA = "Soma"
    SOMA_PRIME = "Soma Prime"
    NECTAR = "Nectar"
    NECTAR_II = "Nectar II"
    NECTAR_III = "Nectar III"
    THERIACA_A = "Theriaca A"
    THERIACA_B = "Theriaca B"
    AXCELA = "Axcela"
    AXCELA_II = "Axcela II"
    AXCELA_III = "Axcela III"
    BRAVANT = "Bravant"
    BRAVANT_II = "Bravant II"
    STONARD = "Stonard"
    STONARD_II = "Stonard II"
    FIRE_MIST = "Fire Mist"
    ICE_MIST = "Ice Mist"
    VOLT_MIST = "Volt Mist"
    ALL_MIST = "All Mist"
    BLAZE_OIL = "Blaze Oil"
    FREEZE_OIL = "Freeze Oil"
    SHOCK_OIL = "Shock Oil"
    WARD_CHIME = "Ward Chime"
    GOLD_CHIME = "Gold Chime"
    POLE_STONE = "Pole Stone"
    MAP_EVENT = "Map Event"
    HOLY_WATER = "Holy Water"
    WATER = "Water"
    BOTTLE = "Bottle"
    JUNK_BOX = "Junk Box"
    LOCKET = "Locket"
    PLANT_SEED = "Plant Seed"
    GOLD_STONE = "Gold Stone"
    MOON_STONE = "Moon Stone"
    GOUDA = "Gouda"
    ODD_POWDER = "Odd Powder"
    LUCKY_COIN = "Lucky Coin"
    RUST_SWORD = "Rust Sword"
    BROKEN_AXE = "Broken Axe"
    OLD_WAND = "Old Wand"
    PANACEA = "Panacea"
    RARE_BLOOM = "Rare Bloom"
    GOLD_SEED = "Gold Seed"
    VOX_STONE = "Vox Stone"
    CLEAR_KEY = "Clear Key"
    VIOLET_KEY = "Violet Key"
    DRAGON_EGG = "Dragon Egg"
    CARD_KEY = "Card Key"
    HOLY_GRAIL = "Holy Grail"
    COPPER_TOP = "Copper Top"
    SHINY_DISC = "Shiny Disc"
    SOFT_GLASS = "Soft Glass"
    TOKEN = "Token"
    CLAM_TOOL = "Clam Tool"
    MAGIC_DOWN = "Magic Down"
    DIAMOND = "Diamond"
    BLACK_GEM = "Black Gem"
    SHINY_GEM = "Shiny Gem"
    OLD_SCROLL = "Old Scroll"
    HEX_BELL = "Hex Bell"
    LABYRINTH_MAP = "Labyrinth Map"
    RADHA_NOTE = "Radha Note"
    ARIADNE_THREAD = "Ariadne Thread"
    FROZEN_ARM = "Frozen Arm"
    ANKH_A = "Ankh A"
    ANKH_B = "Ankh B"
    ANKH_C = "Ankh C"
    ANKH_D = "Ankh D"
    ANKH_E = "Ankh E"
    ANKH_MOTOR = "Ankh Motor"
    BANDANNA = "Bandanna"
    PEARL = "Pearl"
    RARE_MEAT = "Rare Meat"

    # Custom items
    FIRST_STRATUM_CLEARED = "First Stratum Cleared"
    VICTORY = "Victory"
    EN500 = "500en"
    EN200 = "200en"
    EN100 = "100en"
    NIGHT_10TP = "Feeling Refreshed"
    FIRST_CHAR_10HP = "Red Fruit Eaten"
    EN50 = "50en"
    EN1 = "1en"

ITEM_NAME_TO_ID = {
    Items.KNIFE.value: 1,
    Items.SCRAMASAX.value: 2,
    Items.DAGGER.value: 3,
    Items.SHORTSWORD.value: 4,
    Items.BOAR_SPEAR.value: 5,
    Items.BROADSWORD.value: 6,
    Items.RAPIER.value: 7,
    Items.VIKING.value: 8,
    Items.SHAMSHIR.value: 9,
    Items.CLAYMORE.value: 10,
    Items.EXECUTOR.value: 11,
    Items.KATZBALGER.value: 12,
    Items.STEELSWORD.value: 13,
    Items.EPEE.value: 14,
    Items.LAST_ESTOC.value: 15,
    Items.PATTISA.value: 16,
    Items.FLAMBERGE.value: 17,
    Items.DUERGAR.value: 21,
    Items.DRAGONBANE.value: 23,
    Items.BONE_AXE.value: 30,
    Items.HAND_AXE.value: 31,
    Items.CELTIS.value: 32,
    Items.BROADAXE.value: 33,
    Items.BATTLE_AXE.value: 34,
    Items.BILIOMG.value: 35,
    Items.TABAR.value: 36,
    Items.GREAT_AXE.value: 37,
    Items.BARDICHE.value: 38,
    Items.HALBERD.value: 39,
    Items.WAND.value: 40,
    Items.BREAKER.value: 41,
    Items.LABYRIS.value: 42,
    Items.FRANCISCA.value: 43,
    Items.BHUJ.value: 44,
    Items.FASCES_AXE.value: 45,
    Items.FLAME_AXE.value: 48,
    Items.METEOR_AXE.value: 49,
    Items.HATCHET.value: 50,
    Items.STAFF.value: 54,
    Items.BONE_STAFF.value: 55,
    Items.BONE_MACE.value: 56,
    Items.DOWN_STAFF.value: 57,
    Items.BONE_FLAIL.value: 58,
    Items.GEM_STAFF.value: 59,
    Items.WAR_MACE.value: 60,
    Items.LUCK_STAFF.value: 61,
    Items.GODENDAG.value: 62,
    Items.MYSTIC_ROD.value: 63,
    Items.WARHAMMER.value: 64,
    Items.ARCANA_ROD.value: 65,
    Items.SAGE_WAND.value: 66,
    Items.WAKIZASHI.value: 73,
    Items.UCHIGATANA.value: 74,
    Items.OHDACHI.value: 75,
    Items.KOGARASU.value: 76,
    Items.SHIDA.value: 77,
    Items.ZANMATOU.value: 78,
    Items.KUZUNOSADA.value: 79,
    Items.HACHI.value: 80,
    Items.HISAMEMARU.value: 81,
    Items.MASAMUNE.value: 82,
    Items.WOOD_BOW.value: 88,
    Items.ENAMEL_BOW.value: 89,
    Items.SHORT_BOW.value: 90,
    Items.BEAST_BOW.value: 91,
    Items.HARD_SLING.value: 92,
    Items.LONG_BOW.value: 93,
    Items.HINDI.value: 94,
    Items.SELF_BOW.value: 95,
    Items.HUNTER_BOW.value: 96,
    Items.FIN_BOW.value: 97,
    Items.VINE_BOW.value: 98,
    Items.HEAVEN_BOW.value: 99,
    Items.SHIDGEDOU.value: 100,
    Items.WAR_BOW.value: 101,
    Items.ARBALEST.value: 102,
    Items.FAILNAUGHT.value: 103,
    Items.ZAMIEL_BOW.value: 105,
    Items.ARC_DRAWER.value: 106,
    Items.LIGHT_WHIP.value: 112,
    Items.FANG_WHIP.value: 113,
    Items.BULLWHIP.value: 114,
    Items.VINE_WHIP.value: 115,
    Items.NAIL_WHIP.value: 116,
    Items.EDGE_WHIP.value: 117,
    Items.TOXIC_WHIP.value: 118,
    Items.GUM_WHIP.value: 119,
    Items.WIND_WHIP.value: 120,
    Items.SHRED_WHIP.value: 121,
    Items.STING_WHIP.value: 122,
    Items.BLADE_WHIP.value: 123,
    Items.NINE_TAILS.value: 124,
    Items.KNOUT.value: 125,
    Items.DEAD_WHIP.value: 126,
    Items.TORMENTOR.value: 127,
    Items.DOMINATOR.value: 129,
    Items.VOLT_WHIP.value: 131,
    Items.THORN_WHIP.value: 132,
    Items.TWEED.value: 1001,
    Items.JERKIN.value: 1002,
    Items.LEAF_COAT.value: 1003,
    Items.HIDE_VEST.value: 1004,
    Items.HIDE_ARMOR.value: 1005,
    Items.PLATE.value: 1006,
    Items.DOUBLET.value: 1007,
    Items.BUFFCOAT.value: 1008,
    Items.BRIAULT.value: 1009,
    Items.CHAIN_MAIL.value: 1010,
    Items.PETAL_COAT.value: 1011,
    Items.LEAF_TUNIC.value: 1012,
    Items.IRON_PLATE.value: 1013,
    Items.RING_MAIL.value: 1014,
    Items.OAK_JACKET.value: 1015,
    Items.WING_COAT.value: 1016,
    Items.HAUBERK.value: 1017,
    Items.STUD_VEST.value: 1019,
    Items.FANCY_COAT.value: 1020,
    Items.COTARDIE.value: 1021,
    Items.FULL_ARMOR.value: 1022,
    Items.PLATE_MAIL.value: 1023,
    Items.SEVEN_DOUBLET.value: 1024,
    Items.SURCOAT.value: 1025,
    Items.TIGER_COAT.value: 1027,
    Items.FAIRY_ROBE.value: 1028,
    Items.DARK_TUNIC.value: 1029,
    Items.BRIGANDINE.value: 1030,
    Items.EBON_PLATE.value: 1031,
    Items.LYCORIS.value: 1032,
    Items.WYVERNMAIL.value: 1033,
    Items.JAZERAINT.value: 1034,
    Items.DEMON_COAT.value: 1035,
    Items.RUNE_TWEED.value: 1036,
    Items.RUNE_TUNIC.value: 1037,
    Items.BLOOD_MAIL.value: 1038,
    Items.COMPOSITE.value: 1039,
    Items.AZURE_COAT.value: 1040,
    Items.BLOOD_COAT.value: 1041,
    Items.DINO_PLATE.value: 1042,
    Items.DEMON_MAIL.value: 1043,
    Items.SYLPHEED.value: 1044,
    Items.HOLY_ARMOR.value: 1045,
    Items.GHOST_VEST.value: 1046,
    Items.MOBIUS_ALB.value: 1047,
    Items.ANGEL_ROBE.value: 1048,
    Items.FAIRY_MAIL.value: 1049,
    Items.RUBY_MAIL.value: 1050,
    Items.HEX_MANTLE.value: 1051,
    Items.MOSS_COAT.value: 1052,
    Items.FLAME_COAT.value: 1053,
    Items.FROST_COAT.value: 1054,
    Items.VOLT_COAT.value: 1055,
    Items.HAIRPIN.value: 2001,
    Items.HIDE_HAT.value: 2002,
    Items.PLUMED_HAT.value: 2003,
    Items.CHAIN_HELM.value: 2004,
    Items.GUM_HELM.value: 2005,
    Items.SCALE_HELM.value: 2006,
    Items.SCALE_CAP.value: 2007,
    Items.SANDY_PIN.value: 2008,
    Items.TIGER_CAP.value: 2009,
    Items.CIRCLET.value: 2010,
    Items.BLOOD_HELM.value: 2011,
    Items.ANGEL_HELM.value: 2012,
    Items.KNIT_GLOVE.value: 2018,
    Items.HIDE_GLOVE.value: 2019,
    Items.DOWN_GLOVE.value: 2020,
    Items.IRON_GLOVE.value: 2021,
    Items.BEAR_GLOVE.value: 2022,
    Items.GUM_GLOVE.value: 2023,
    Items.FANG_GLOVE.value: 2024,
    Items.SAND_GLOVE.value: 2025,
    Items.TIGER_HAND.value: 2026,
    Items.RUNE_GLOVE.value: 2027,
    Items.BLOOD_GAGE.value: 2028,
    Items.BRAVE_GAGE.value: 2029,
    Items.EBON_GLOVE.value: 2030,
    Items.ATHANOR.value: 2031,
    Items.RUBY_GAGE.value: 2032,
    Items.TOXIC_GAGE.value: 2033,
    Items.TARGE.value: 2038,
    Items.HIDE_ASPIS.value: 2039,
    Items.ASPIS.value: 2040,
    Items.OVAL_ASPIS.value: 2041,
    Items.HEAT_ASPIS.value: 2042,
    Items.GUM_ASPIS.value: 2043,
    Items.BODY_ASPIS.value: 2044,
    Items.EBON_ASPIS.value: 2045,
    Items.MOON_ASPIS.value: 2046,
    Items.KING_ASPIS.value: 2047,
    Items.HALO_ASPIS.value: 2048,
    Items.HOLY_ASPIS.value: 2049,
    Items.PAIN_ASPIS.value: 2050,
    Items.LEAF_BOOT.value: 2056,
    Items.HIDE_BOOT.value: 2057,
    Items.PLUME_BOOT.value: 2058,
    Items.CHAIN_BOOT.value: 2059,
    Items.MOCCASINS.value: 2060,
    Items.SCALE_BOOT.value: 2061,
    Items.FAIRY_BOOT.value: 2062,
    Items.TIGER_BOOT.value: 2063,
    Items.FLAME_BOOT.value: 2064,
    Items.FUR_BOOT.value: 2065,
    Items.DYED_BOOT.value: 2066,
    Items.SPEED_BOOT.value: 2067,
    Items.HIDE_BELT.value: 3001,
    Items.HIDE_RING.value: 3002,
    Items.RED_CHARM.value: 3003,
    Items.PETAL_RING.value: 3004,
    Items.CUT_CHARM.value: 3005,
    Items.GEM_RING.value: 3006,
    Items.LEAF_CAPE.value: 3007,
    Items.FIRE_RING.value: 3008,
    Items.STAR_CHARM.value: 3009,
    Items.TUSK_CHARM.value: 3010,
    Items.OLD_CHOKER.value: 3011,
    Items.HIDE_CAPE.value: 3012,
    Items.AMBER_RING.value: 3013,
    Items.SEA_CHARM.value: 3014,
    Items.BLUE_RING.value: 3015,
    Items.RED_CAPE.value: 3016,
    Items.EVIL_CHARM.value: 3017,
    Items.ROSE_RING.value: 3018,
    Items.ROYAL_RING.value: 3019,
    Items.GOLD_CAPE.value: 3020,
    Items.ANGEL_RING.value: 3021,
    Items.WARD_GEM.value: 3022,
    Items.JEWEL_EYE.value: 3023,
    Items.RUBY.value: 3024,
    Items.SAPPHIRE.value: 3025,
    Items.TOPAZ.value: 3026,
    Items.TOURMALINE.value: 3027,
    Items.ADAMAS.value: 3028,
    Items.HEX_DOLL.value: 3029,
    Items.OCARINA.value: 3030,
    Items.LUTE.value: 3031,
    Items.FLUTE.value: 3032,
    Items.KITHARA.value: 3033,
    Items.AULOS.value: 3034,
    Items.ANGEL_HARP.value: 3035,
    Items.SYRINX.value: 3036,
    Items.TOWN_MEDAL.value: 3037,
    Items.TOWN_CROWN.value: 3038,
    Items.MOSS_RING.value: 3039,
    Items.MOSS_BAND.value: 3040,
    Items.SMALL_FANG.value: 4001,
    Items.SOFT_HIDE.value: 4002,
    Items.BEAST_BONE.value: 4003,
    Items.HARD_SHELL.value: 4004,
    Items.BUG_WING.value: 4005,
    Items.TINY_PETAL.value: 4006,
    Items.INSECT_EYE.value: 4007,
    Items.HARE_TAIL.value: 4008,
    Items.HORN.value: 4009,
    Items.HARDWOOD.value: 4010,
    Items.VINE.value: 4011,
    Items.CHARCOAL.value: 4012,
    Items.GUM_HIDE.value: 4013,
    Items.THORN.value: 4014,
    Items.METAL_HORN.value: 4015,
    Items.STIFF_HIDE.value: 4016,
    Items.AMBER_LUMP.value: 4017,
    Items.CRABAPPLE.value: 4018,
    Items.MUGWORT.value: 4019,
    Items.RED_FRUIT.value: 4020,
    Items.WHITESTONE.value: 4021,
    Items.PYROXENE.value: 4022,
    Items.GOLEM_ROCK.value: 4023,
    Items.LARGE_FANG.value: 4025,
    Items.HUGE_FANG.value: 4026,
    Items.WHITE_HIDE.value: 4027,
    Items.SCYTHE.value: 4028,
    Items.STICKY_GOO.value: 4029,
    Items.STEEL_LUMP.value: 4030,
    Items.STINGER.value: 4031,
    Items.STICKY_WEB.value: 4032,
    Items.BENT_CLAW.value: 4033,
    Items.LIGHT_WOOD.value: 4034,
    Items.DYE_PETAL.value: 4035,
    Items.STARSEED.value: 4036,
    Items.SCENT_WOOD.value: 4037,
    Items.GUM_VINE.value: 4038,
    Items.FEATHER.value: 4039,
    Items.TAILBONE.value: 4040,
    Items.CARMINITE.value: 4041,
    Items.IRON_SHELL.value: 4042,
    Items.THICK_LEAF.value: 4043,
    Items.BIRD_TALON.value: 4044,
    Items.TIGER_FANG.value: 4045,
    Items.TIGER_FUR.value: 4046,
    Items.MINT_LEAF.value: 4047,
    Items.SCRAP_IRON.value: 4048,
    Items.FOSSIL.value: 4049,
    Items.BEAR_FUR.value: 4050,
    Items.BIRD_LIMB.value: 4051,
    Items.THIN_SHELL.value: 4052,
    Items.TOXIC_BARB.value: 4053,
    Items.SHARP_HORN.value: 4054,
    Items.TOUGH_WING.value: 4055,
    Items.TOUGH_FANG.value: 4056,
    Items.GREAT_TUSK.value: 4057,
    Items.GUM_THROAT.value: 4058,
    Items.ROCK_CORAL.value: 4059,
    Items.ELASTIC.value: 4060,
    Items.GLASS_EYE.value: 4061,
    Items.STEEL_BONE.value: 4062,
    Items.BONE_SHARD.value: 4063,
    Items.CARAPACE.value: 4064,
    Items.BUG_NEST.value: 4065,
    Items.BAT_WING.value: 4066,
    Items.SHINY_GOO.value: 4067,
    Items.SHRED_NAIL.value: 4068,
    Items.RED_HIDE.value: 4069,
    Items.BLOOD_FANG.value: 4070,
    Items.SWORDFISH_SCALE.value: 4071,
    Items.SWORDFISH_FIN.value: 4072,
    Items.CRAB_LEG.value: 4073,
    Items.ANT_HONEY.value: 4074,
    Items.STAB_SHELL.value: 4075,
    Items.STRAWBERRY.value: 4076,
    Items.SEA_BRANCH.value: 4077,
    Items.CORUNDUM.value: 4079,
    Items.RED_BLADE.value: 4080,
    Items.DEATH_CLAW.value: 4081,
    Items.HUGE_FIN.value: 4082,
    Items.HUNDRED_SHELL.value: 4084,
    Items.GATOR_SKIN.value: 4085,
    Items.HEATED_FUR.value: 4086,
    Items.FIRE_TAIL.value: 4087,
    Items.WHITE_SKIN.value: 4088,
    Items.WHITE_FANG.value: 4089,
    Items.SHINY_HORN.value: 4090,
    Items.MUSK.value: 4091,
    Items.BROKEN_EYE.value: 4092,
    Items.SILVER_EYE.value: 4093,
    Items.NYX_SCYTHE.value: 4094,
    Items.TENDON.value: 4095,
    Items.DRIED_VINE.value: 4096,
    Items.PURE_ROOT.value: 4097,
    Items.HARD_SHARD.value: 4098,
    Items.INK_STICK.value: 4099,
    Items.SAND_CLOTH.value: 4100,
    Items.SAND_TWIG.value: 4101,
    Items.FAIRY_WING.value: 4102,
    Items.FAIRY_SAP.value: 4103,
    Items.RED_PLUME.value: 4104,
    Items.RED_BEAK.value: 4105,
    Items.DRY_PEACH.value: 4106,
    Items.THROB_VINE.value: 4107,
    Items.RED_STRING.value: 4108,
    Items.RED_THREAD.value: 4109,
    Items.OLEANDER.value: 4110,
    Items.STEEL_CLAW.value: 4114,
    Items.STEEL_CHIP.value: 4115,
    Items.CULLINAN.value: 4116,
    Items.CORDYCEPS.value: 4117,
    Items.SAP_WINE.value: 4118,
    Items.SPACE_NAIL.value: 4119,
    Items.TINY_TOOTH.value: 4120,
    Items.DEMON_FUR.value: 4121,
    Items.REX_THROAT.value: 4122,
    Items.GEM_CORE.value: 4123,
    Items.GUM_THREAD.value: 4124,
    Items.RED_FUR.value: 4125,
    Items.RED_BLOOD.value: 4126,
    Items.GOLD_SHELL.value: 4127,
    Items.BLUE_BLOOD.value: 4128,
    Items.DEATH_STEM.value: 4129,
    Items.GOLD_FUR.value: 4130,
    Items.GOLD_TUSK.value: 4131,
    Items.GOLD_HORN.value: 4132,
    Items.SPACE_HUSK.value: 4133,
    Items.SPACE_CLAW.value: 4134,
    Items.ANGEL_WING.value: 4135,
    Items.LIFE_HONEY.value: 4136,
    Items.STERNUM.value: 4137,
    Items.CURSE_TUSK.value: 4138,
    Items.ROYAL_HIDE.value: 4139,
    Items.SHROUD.value: 4140,
    Items.RED_ORE.value: 4141,
    Items.AMBROSIA.value: 4144,
    Items.HEADROOT.value: 4148,
    Items.ARMROOT.value: 4149,
    Items.LEGROOT.value: 4150,
    Items.GUM_STRING.value: 4151,
    Items.SHINY_VINE.value: 4152,
    Items.SHINY_SEED.value: 4153,
    Items.DRYWALL.value: 4154,
    Items.CRYSTWALL.value: 4155,
    Items.JADE_ORE.value: 4156,
    Items.AZURE_ORE.value: 4157,
    Items.EVIL_SHELL.value: 4158,
    Items.EVIL_SCALE.value: 4159,
    Items.EVIL_PLUME.value: 4160,
    Items.EVIL_CREST.value: 4161,
    Items.OLD_SHELL.value: 4163,
    Items.GEM_SCALE.value: 4164,
    Items.BLACK_ROOT.value: 4165,
    Items.GEM_PLUME.value: 4166,
    Items.HEX_MARROW.value: 4167,
    Items.GOLD_PLUME.value: 4168,
    Items.HELL_WING.value: 4169,
    Items.VELVET.value: 4170,
    Items.HOLED_LIMB.value: 4171,
    Items.RUBY_SKULL.value: 4172,
    Items.RUBY_BONE.value: 4173,
    Items.HEX_CHAIN.value: 4174,
    Items.SWORD_RIB.value: 4175,
    Items.FLAME_SKIN.value: 4176,
    Items.FROST_SKIN.value: 4177,
    Items.VOLT_SKIN.value: 4178,
    Items.VOLT_CORE.value: 4179,
    Items.FIRE_SCALE.value: 4181,
    Items.FIRE_FANG.value: 4182,
    Items.STATUE_ARM.value: 4183,
    Items.BEAST_EYE.value: 4184,
    Items.FROST_BONE.value: 4185,
    Items.DEMON_CORE.value: 4186,
    Items.EBON_PLUME.value: 4187,
    Items.SEA_KING_ICE.value: 4188,
    Items.BARBEL.value: 4189,
    Items.ROYAL_VINE.value: 4190,
    Items.HARVESTER.value: 4191,
    Items.ROYAL_MANE.value: 4192,
    Items.ICE_SCALE.value: 4194,
    Items.WINE_WHIP.value: 4195,
    Items.ROSE_WHIP.value: 4196,
    Items.TOXIC_HAND.value: 4197,
    Items.VOLT_SCALE.value: 4198,
    Items.YELLOW_ORE.value: 4199,
    Items.BUG_SCALE.value: 4200,
    Items.COLD_SCALE.value: 4201,
    Items.ODD_FRUIT.value: 4202,
    Items.CROSS_SEED.value: 4203,
    Items.NARCISSUS.value: 4204,
    Items.MOSCHINO.value: 4205,
    Items.SMALL_LEAF.value: 4206,
    Items.MEDIUM_LEAF.value: 4207,
    Items.LARGE_LEAF.value: 4208,
    Items.MEDICA.value: 4279,
    Items.MEDICA_II.value: 4280,
    Items.MEDICA_III.value: 4281,
    Items.MEDICA_IV.value: 4282,
    Items.MEDICA_V.value: 4283,
    Items.AMRITA.value: 4284,
    Items.AMRITA_II.value: 4285,
    Items.HAMAO.value: 4286,
    Items.HAMAO_PRIME.value: 4287,
    Items.SOMA.value: 4288,
    Items.SOMA_PRIME.value: 4289,
    Items.NECTAR.value: 4290,
    Items.NECTAR_II.value: 4291,
    Items.NECTAR_III.value: 4292,
    Items.THERIACA_A.value: 4295,
    Items.THERIACA_B.value: 4296,
    Items.AXCELA.value: 4301,
    Items.AXCELA_II.value: 4302,
    Items.AXCELA_III.value: 4303,
    Items.BRAVANT.value: 4305,
    Items.BRAVANT_II.value: 4306,
    Items.STONARD.value: 4307,
    Items.STONARD_II.value: 4308,
    Items.FIRE_MIST.value: 4311,
    Items.ICE_MIST.value: 4312,
    Items.VOLT_MIST.value: 4313,
    Items.ALL_MIST.value: 4314,
    Items.BLAZE_OIL.value: 4315,
    Items.FREEZE_OIL.value: 4316,
    Items.SHOCK_OIL.value: 4317,
    Items.WARD_CHIME.value: 4319,
    Items.GOLD_CHIME.value: 4320,
    Items.POLE_STONE.value: 4332,
    Items.MAP_EVENT.value: 4333,
    Items.HOLY_WATER.value: 4334,
    Items.WATER.value: 4335,
    Items.BOTTLE.value: 4336,
    Items.JUNK_BOX.value: 4337,
    # Items.JUNK_BOX.value: 4338,
    Items.LOCKET.value: 4339,
    Items.PLANT_SEED.value: 4340,
    Items.GOLD_STONE.value: 4341,
    # Items.GOLD_STONE.value: 4342,
    Items.MOON_STONE.value: 4343,
    Items.GOUDA.value: 4344,
    Items.ODD_POWDER.value: 4345,
    Items.LUCKY_COIN.value: 4346,
    Items.RUST_SWORD.value: 4347,
    Items.BROKEN_AXE.value: 4348,
    Items.OLD_WAND.value: 4349,
    Items.PANACEA.value: 4350,
    Items.RARE_BLOOM.value: 4351,
    Items.GOLD_SEED.value: 4352,
    Items.VOX_STONE.value: 4353,
    Items.CLEAR_KEY.value: 4354,
    Items.VIOLET_KEY.value: 4355,
    Items.DRAGON_EGG.value: 4356,
    Items.CARD_KEY.value: 4357,
    Items.HOLY_GRAIL.value: 4358,
    Items.COPPER_TOP.value: 4359,
    Items.SHINY_DISC.value: 4360,
    Items.SOFT_GLASS.value: 4361,
    Items.TOKEN.value: 4362,
    Items.CLAM_TOOL.value: 4363,
    Items.MAGIC_DOWN.value: 4364,
    # Items.MAGIC_DOWN.value: 4365,
    # Items.MAGIC_DOWN.value: 4366,
    Items.DIAMOND.value: 4367,
    Items.BLACK_GEM.value: 4368,
    Items.SHINY_GEM.value: 4369,
    Items.OLD_SCROLL.value: 4370,
    Items.HEX_BELL.value: 4371,
    Items.LABYRINTH_MAP.value: 4372,
    Items.RADHA_NOTE.value: 4373,
    Items.ARIADNE_THREAD.value: 4374,
    # Items.TOUGH_FANG.value: 4375,
    # Items.TOUGH_WING.value: 4377,
    Items.FROZEN_ARM.value: 4413,
    Items.ANKH_A.value: 4414,
    Items.ANKH_B.value: 4415,
    Items.ANKH_C.value: 4416,
    Items.ANKH_D.value: 4417,
    Items.ANKH_E.value: 4418,
    Items.ANKH_MOTOR.value: 4419,
    Items.BANDANNA.value: 4420,
    Items.PEARL.value: 4421,
    Items.RARE_MEAT.value: 4422,

    # Custom items
    Items.FIRST_STRATUM_CLEARED.value: 1000001,
    Items.VICTORY.value: 1000002,
    Items.EN500.value: 1000003,
    Items.EN200.value: 1000004,
    Items.EN100.value: 1000005,
    Items.NIGHT_10TP.value: 1000006,
    Items.FIRST_CHAR_10HP.value: 1000007,
    Items.EN50.value: 1000008,
    Items.EN1.value: 1000009,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    Items.KNIFE.value: ItemClassification.useful | ItemClassification.filler,
    Items.SCRAMASAX.value: ItemClassification.useful | ItemClassification.filler,
    Items.DAGGER.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHORTSWORD.value: ItemClassification.useful | ItemClassification.filler,
    Items.BOAR_SPEAR.value: ItemClassification.useful | ItemClassification.filler,
    Items.BROADSWORD.value: ItemClassification.useful | ItemClassification.filler,
    Items.RAPIER.value: ItemClassification.useful | ItemClassification.filler,
    Items.VIKING.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHAMSHIR.value: ItemClassification.useful | ItemClassification.filler,
    Items.CLAYMORE.value: ItemClassification.useful | ItemClassification.filler,
    Items.EXECUTOR.value: ItemClassification.useful | ItemClassification.filler,
    Items.KATZBALGER.value: ItemClassification.useful | ItemClassification.filler,
    Items.STEELSWORD.value: ItemClassification.useful | ItemClassification.filler,
    Items.EPEE.value: ItemClassification.useful | ItemClassification.filler,
    Items.LAST_ESTOC.value: ItemClassification.useful | ItemClassification.filler,
    Items.PATTISA.value: ItemClassification.useful | ItemClassification.filler,
    Items.FLAMBERGE.value: ItemClassification.useful | ItemClassification.filler,
    Items.DUERGAR.value: ItemClassification.useful | ItemClassification.filler,
    Items.DRAGONBANE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BONE_AXE.value: ItemClassification.useful | ItemClassification.filler,
    Items.HAND_AXE.value: ItemClassification.useful | ItemClassification.filler,
    Items.CELTIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.BROADAXE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BATTLE_AXE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BILIOMG.value: ItemClassification.useful | ItemClassification.filler,
    Items.TABAR.value: ItemClassification.useful | ItemClassification.filler,
    Items.GREAT_AXE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BARDICHE.value: ItemClassification.useful | ItemClassification.filler,
    Items.HALBERD.value: ItemClassification.useful | ItemClassification.filler,
    Items.WAND.value: ItemClassification.useful | ItemClassification.filler,
    Items.BREAKER.value: ItemClassification.useful | ItemClassification.filler,
    Items.LABYRIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.FRANCISCA.value: ItemClassification.useful | ItemClassification.filler,
    Items.BHUJ.value: ItemClassification.useful | ItemClassification.filler,
    Items.FASCES_AXE.value: ItemClassification.useful | ItemClassification.filler,
    Items.FLAME_AXE.value: ItemClassification.useful | ItemClassification.filler,
    Items.METEOR_AXE.value: ItemClassification.useful | ItemClassification.filler,
    Items.HATCHET.value: ItemClassification.useful | ItemClassification.filler,
    Items.STAFF.value: ItemClassification.useful | ItemClassification.filler,
    Items.BONE_STAFF.value: ItemClassification.useful | ItemClassification.filler,
    Items.BONE_MACE.value: ItemClassification.useful | ItemClassification.filler,
    Items.DOWN_STAFF.value: ItemClassification.useful | ItemClassification.filler,
    Items.BONE_FLAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.GEM_STAFF.value: ItemClassification.useful | ItemClassification.filler,
    Items.WAR_MACE.value: ItemClassification.useful | ItemClassification.filler,
    Items.LUCK_STAFF.value: ItemClassification.useful | ItemClassification.filler,
    Items.GODENDAG.value: ItemClassification.useful | ItemClassification.filler,
    Items.MYSTIC_ROD.value: ItemClassification.useful | ItemClassification.filler,
    Items.WARHAMMER.value: ItemClassification.useful | ItemClassification.filler,
    Items.ARCANA_ROD.value: ItemClassification.useful | ItemClassification.filler,
    Items.SAGE_WAND.value: ItemClassification.useful | ItemClassification.filler,
    Items.WAKIZASHI.value: ItemClassification.useful | ItemClassification.filler,
    Items.UCHIGATANA.value: ItemClassification.useful | ItemClassification.filler,
    Items.OHDACHI.value: ItemClassification.useful | ItemClassification.filler,
    Items.KOGARASU.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHIDA.value: ItemClassification.useful | ItemClassification.filler,
    Items.ZANMATOU.value: ItemClassification.useful | ItemClassification.filler,
    Items.KUZUNOSADA.value: ItemClassification.useful | ItemClassification.filler,
    Items.HACHI.value: ItemClassification.useful | ItemClassification.filler,
    Items.HISAMEMARU.value: ItemClassification.useful | ItemClassification.filler,
    Items.MASAMUNE.value: ItemClassification.useful | ItemClassification.filler,
    Items.WOOD_BOW.value: ItemClassification.useful | ItemClassification.filler,
    Items.ENAMEL_BOW.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHORT_BOW.value: ItemClassification.useful | ItemClassification.filler,
    Items.BEAST_BOW.value: ItemClassification.useful | ItemClassification.filler,
    Items.HARD_SLING.value: ItemClassification.useful | ItemClassification.filler,
    Items.LONG_BOW.value: ItemClassification.useful | ItemClassification.filler,
    Items.HINDI.value: ItemClassification.useful | ItemClassification.filler,
    Items.SELF_BOW.value: ItemClassification.useful | ItemClassification.filler,
    Items.HUNTER_BOW.value: ItemClassification.useful | ItemClassification.filler,
    Items.FIN_BOW.value: ItemClassification.useful | ItemClassification.filler,
    Items.VINE_BOW.value: ItemClassification.useful | ItemClassification.filler,
    Items.HEAVEN_BOW.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHIDGEDOU.value: ItemClassification.useful | ItemClassification.filler,
    Items.WAR_BOW.value: ItemClassification.useful | ItemClassification.filler,
    Items.ARBALEST.value: ItemClassification.useful | ItemClassification.filler,
    Items.FAILNAUGHT.value: ItemClassification.useful | ItemClassification.filler,
    Items.ZAMIEL_BOW.value: ItemClassification.useful | ItemClassification.filler,
    Items.ARC_DRAWER.value: ItemClassification.useful | ItemClassification.filler,
    Items.LIGHT_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.FANG_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.BULLWHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.VINE_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.NAIL_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.EDGE_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.TOXIC_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.GUM_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.WIND_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHRED_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.STING_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.BLADE_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.NINE_TAILS.value: ItemClassification.useful | ItemClassification.filler,
    Items.KNOUT.value: ItemClassification.useful | ItemClassification.filler,
    Items.DEAD_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.TORMENTOR.value: ItemClassification.useful | ItemClassification.filler,
    Items.DOMINATOR.value: ItemClassification.useful | ItemClassification.filler,
    Items.VOLT_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.THORN_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.TWEED.value: ItemClassification.useful | ItemClassification.filler,
    Items.JERKIN.value: ItemClassification.useful | ItemClassification.filler,
    Items.LEAF_COAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.HIDE_VEST.value: ItemClassification.useful | ItemClassification.filler,
    Items.HIDE_ARMOR.value: ItemClassification.useful | ItemClassification.filler,
    Items.PLATE.value: ItemClassification.useful | ItemClassification.filler,
    Items.DOUBLET.value: ItemClassification.useful | ItemClassification.filler,
    Items.BUFFCOAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.BRIAULT.value: ItemClassification.useful | ItemClassification.filler,
    Items.CHAIN_MAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.PETAL_COAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.LEAF_TUNIC.value: ItemClassification.useful | ItemClassification.filler,
    Items.IRON_PLATE.value: ItemClassification.useful | ItemClassification.filler,
    Items.RING_MAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.OAK_JACKET.value: ItemClassification.useful | ItemClassification.filler,
    Items.WING_COAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.HAUBERK.value: ItemClassification.useful | ItemClassification.filler,
    Items.STUD_VEST.value: ItemClassification.useful | ItemClassification.filler,
    Items.FANCY_COAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.COTARDIE.value: ItemClassification.useful | ItemClassification.filler,
    Items.FULL_ARMOR.value: ItemClassification.useful | ItemClassification.filler,
    Items.PLATE_MAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.SEVEN_DOUBLET.value: ItemClassification.useful | ItemClassification.filler,
    Items.SURCOAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.TIGER_COAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.FAIRY_ROBE.value: ItemClassification.useful | ItemClassification.filler,
    Items.DARK_TUNIC.value: ItemClassification.useful | ItemClassification.filler,
    Items.BRIGANDINE.value: ItemClassification.useful | ItemClassification.filler,
    Items.EBON_PLATE.value: ItemClassification.useful | ItemClassification.filler,
    Items.LYCORIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.WYVERNMAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.JAZERAINT.value: ItemClassification.useful | ItemClassification.filler,
    Items.DEMON_COAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.RUNE_TWEED.value: ItemClassification.useful | ItemClassification.filler,
    Items.RUNE_TUNIC.value: ItemClassification.useful | ItemClassification.filler,
    Items.BLOOD_MAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.COMPOSITE.value: ItemClassification.useful | ItemClassification.filler,
    Items.AZURE_COAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.BLOOD_COAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.DINO_PLATE.value: ItemClassification.useful | ItemClassification.filler,
    Items.DEMON_MAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.SYLPHEED.value: ItemClassification.useful | ItemClassification.filler,
    Items.HOLY_ARMOR.value: ItemClassification.useful | ItemClassification.filler,
    Items.GHOST_VEST.value: ItemClassification.useful | ItemClassification.filler,
    Items.MOBIUS_ALB.value: ItemClassification.useful | ItemClassification.filler,
    Items.ANGEL_ROBE.value: ItemClassification.useful | ItemClassification.filler,
    Items.FAIRY_MAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.RUBY_MAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.HEX_MANTLE.value: ItemClassification.useful | ItemClassification.filler,
    Items.MOSS_COAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.FLAME_COAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.FROST_COAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.VOLT_COAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.HAIRPIN.value: ItemClassification.useful | ItemClassification.filler,
    Items.HIDE_HAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.PLUMED_HAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.CHAIN_HELM.value: ItemClassification.useful | ItemClassification.filler,
    Items.GUM_HELM.value: ItemClassification.useful | ItemClassification.filler,
    Items.SCALE_HELM.value: ItemClassification.useful | ItemClassification.filler,
    Items.SCALE_CAP.value: ItemClassification.useful | ItemClassification.filler,
    Items.SANDY_PIN.value: ItemClassification.useful | ItemClassification.filler,
    Items.TIGER_CAP.value: ItemClassification.useful | ItemClassification.filler,
    Items.CIRCLET.value: ItemClassification.useful | ItemClassification.filler,
    Items.BLOOD_HELM.value: ItemClassification.useful | ItemClassification.filler,
    Items.ANGEL_HELM.value: ItemClassification.useful | ItemClassification.filler,
    Items.KNIT_GLOVE.value: ItemClassification.useful | ItemClassification.filler,
    Items.HIDE_GLOVE.value: ItemClassification.useful | ItemClassification.filler,
    Items.DOWN_GLOVE.value: ItemClassification.useful | ItemClassification.filler,
    Items.IRON_GLOVE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BEAR_GLOVE.value: ItemClassification.useful | ItemClassification.filler,
    Items.GUM_GLOVE.value: ItemClassification.useful | ItemClassification.filler,
    Items.FANG_GLOVE.value: ItemClassification.useful | ItemClassification.filler,
    Items.SAND_GLOVE.value: ItemClassification.useful | ItemClassification.filler,
    Items.TIGER_HAND.value: ItemClassification.useful | ItemClassification.filler,
    Items.RUNE_GLOVE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BLOOD_GAGE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BRAVE_GAGE.value: ItemClassification.useful | ItemClassification.filler,
    Items.EBON_GLOVE.value: ItemClassification.useful | ItemClassification.filler,
    Items.ATHANOR.value: ItemClassification.useful | ItemClassification.filler,
    Items.RUBY_GAGE.value: ItemClassification.useful | ItemClassification.filler,
    Items.TOXIC_GAGE.value: ItemClassification.useful | ItemClassification.filler,
    Items.TARGE.value: ItemClassification.useful | ItemClassification.filler,
    Items.HIDE_ASPIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.ASPIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.OVAL_ASPIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.HEAT_ASPIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.GUM_ASPIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.BODY_ASPIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.EBON_ASPIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.MOON_ASPIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.KING_ASPIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.HALO_ASPIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.HOLY_ASPIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.PAIN_ASPIS.value: ItemClassification.useful | ItemClassification.filler,
    Items.LEAF_BOOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.HIDE_BOOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.PLUME_BOOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.CHAIN_BOOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.MOCCASINS.value: ItemClassification.useful | ItemClassification.filler,
    Items.SCALE_BOOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.FAIRY_BOOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.TIGER_BOOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.FLAME_BOOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.FUR_BOOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.DYED_BOOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.SPEED_BOOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.HIDE_BELT.value: ItemClassification.useful | ItemClassification.filler,
    Items.HIDE_RING.value: ItemClassification.useful | ItemClassification.filler,
    Items.RED_CHARM.value: ItemClassification.useful | ItemClassification.filler,
    Items.PETAL_RING.value: ItemClassification.useful | ItemClassification.filler,
    Items.CUT_CHARM.value: ItemClassification.useful | ItemClassification.filler,
    Items.GEM_RING.value: ItemClassification.useful | ItemClassification.filler,
    Items.LEAF_CAPE.value: ItemClassification.useful | ItemClassification.filler,
    Items.FIRE_RING.value: ItemClassification.useful | ItemClassification.filler,
    Items.STAR_CHARM.value: ItemClassification.useful | ItemClassification.filler,
    Items.TUSK_CHARM.value: ItemClassification.useful | ItemClassification.filler,
    Items.OLD_CHOKER.value: ItemClassification.useful | ItemClassification.filler,
    Items.HIDE_CAPE.value: ItemClassification.useful | ItemClassification.filler,
    Items.AMBER_RING.value: ItemClassification.useful | ItemClassification.filler,
    Items.SEA_CHARM.value: ItemClassification.useful | ItemClassification.filler,
    Items.BLUE_RING.value: ItemClassification.useful | ItemClassification.filler,
    Items.RED_CAPE.value: ItemClassification.useful | ItemClassification.filler,
    Items.EVIL_CHARM.value: ItemClassification.useful | ItemClassification.filler,
    Items.ROSE_RING.value: ItemClassification.useful | ItemClassification.filler,
    Items.ROYAL_RING.value: ItemClassification.useful | ItemClassification.filler,
    Items.GOLD_CAPE.value: ItemClassification.useful | ItemClassification.filler,
    Items.ANGEL_RING.value: ItemClassification.useful | ItemClassification.filler,
    Items.WARD_GEM.value: ItemClassification.useful | ItemClassification.filler,
    Items.JEWEL_EYE.value: ItemClassification.useful | ItemClassification.filler,
    Items.RUBY.value: ItemClassification.useful | ItemClassification.filler,
    Items.SAPPHIRE.value: ItemClassification.useful | ItemClassification.filler,
    Items.TOPAZ.value: ItemClassification.useful | ItemClassification.filler,
    Items.TOURMALINE.value: ItemClassification.useful | ItemClassification.filler,
    Items.ADAMAS.value: ItemClassification.useful | ItemClassification.filler,
    Items.HEX_DOLL.value: ItemClassification.useful | ItemClassification.filler,
    Items.OCARINA.value: ItemClassification.useful | ItemClassification.filler,
    Items.LUTE.value: ItemClassification.useful | ItemClassification.filler,
    Items.FLUTE.value: ItemClassification.useful | ItemClassification.filler,
    Items.KITHARA.value: ItemClassification.useful | ItemClassification.filler,
    Items.AULOS.value: ItemClassification.useful | ItemClassification.filler,
    Items.ANGEL_HARP.value: ItemClassification.useful | ItemClassification.filler,
    Items.SYRINX.value: ItemClassification.useful | ItemClassification.filler,
    Items.TOWN_MEDAL.value: ItemClassification.useful | ItemClassification.filler,
    Items.TOWN_CROWN.value: ItemClassification.useful | ItemClassification.filler,
    Items.MOSS_RING.value: ItemClassification.useful | ItemClassification.filler,
    Items.MOSS_BAND.value: ItemClassification.useful | ItemClassification.filler,
    Items.SMALL_FANG.value: ItemClassification.useful | ItemClassification.filler,
    Items.SOFT_HIDE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BEAST_BONE.value: ItemClassification.useful | ItemClassification.filler,
    Items.HARD_SHELL.value: ItemClassification.useful | ItemClassification.filler,
    Items.BUG_WING.value: ItemClassification.useful | ItemClassification.filler,
    Items.TINY_PETAL.value: ItemClassification.useful | ItemClassification.filler,
    Items.INSECT_EYE.value: ItemClassification.useful | ItemClassification.filler,
    Items.HARE_TAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.HORN.value: ItemClassification.useful | ItemClassification.filler,
    Items.HARDWOOD.value: ItemClassification.useful | ItemClassification.filler,
    Items.VINE.value: ItemClassification.useful | ItemClassification.filler,
    Items.CHARCOAL.value: ItemClassification.useful | ItemClassification.filler,
    Items.GUM_HIDE.value: ItemClassification.useful | ItemClassification.filler,
    Items.THORN.value: ItemClassification.useful | ItemClassification.filler,
    Items.METAL_HORN.value: ItemClassification.useful | ItemClassification.filler,
    Items.STIFF_HIDE.value: ItemClassification.useful | ItemClassification.filler,
    Items.AMBER_LUMP.value: ItemClassification.useful | ItemClassification.filler,
    Items.CRABAPPLE.value: ItemClassification.useful | ItemClassification.filler,
    Items.MUGWORT.value: ItemClassification.useful | ItemClassification.filler,
    Items.RED_FRUIT.value: ItemClassification.useful | ItemClassification.filler,
    Items.WHITESTONE.value: ItemClassification.useful | ItemClassification.filler,
    Items.PYROXENE.value: ItemClassification.useful | ItemClassification.filler,
    Items.GOLEM_ROCK.value: ItemClassification.useful | ItemClassification.filler,
    Items.LARGE_FANG.value: ItemClassification.useful | ItemClassification.filler,
    Items.HUGE_FANG.value: ItemClassification.useful | ItemClassification.filler,
    Items.WHITE_HIDE.value: ItemClassification.useful | ItemClassification.filler,
    Items.SCYTHE.value: ItemClassification.useful | ItemClassification.filler,
    Items.STICKY_GOO.value: ItemClassification.useful | ItemClassification.filler,
    Items.STEEL_LUMP.value: ItemClassification.useful | ItemClassification.filler,
    Items.STINGER.value: ItemClassification.useful | ItemClassification.filler,
    Items.STICKY_WEB.value: ItemClassification.useful | ItemClassification.filler,
    Items.BENT_CLAW.value: ItemClassification.useful | ItemClassification.filler,
    Items.LIGHT_WOOD.value: ItemClassification.useful | ItemClassification.filler,
    Items.DYE_PETAL.value: ItemClassification.useful | ItemClassification.filler,
    Items.STARSEED.value: ItemClassification.useful | ItemClassification.filler,
    Items.SCENT_WOOD.value: ItemClassification.useful | ItemClassification.filler,
    Items.GUM_VINE.value: ItemClassification.useful | ItemClassification.filler,
    Items.FEATHER.value: ItemClassification.useful | ItemClassification.filler,
    Items.TAILBONE.value: ItemClassification.useful | ItemClassification.filler,
    Items.CARMINITE.value: ItemClassification.useful | ItemClassification.filler,
    Items.IRON_SHELL.value: ItemClassification.useful | ItemClassification.filler,
    Items.THICK_LEAF.value: ItemClassification.useful | ItemClassification.filler,
    Items.BIRD_TALON.value: ItemClassification.useful | ItemClassification.filler,
    Items.TIGER_FANG.value: ItemClassification.useful | ItemClassification.filler,
    Items.TIGER_FUR.value: ItemClassification.useful | ItemClassification.filler,
    Items.MINT_LEAF.value: ItemClassification.useful | ItemClassification.filler,
    Items.SCRAP_IRON.value: ItemClassification.useful | ItemClassification.filler,
    Items.FOSSIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.BEAR_FUR.value: ItemClassification.useful | ItemClassification.filler,
    Items.BIRD_LIMB.value: ItemClassification.useful | ItemClassification.filler,
    Items.THIN_SHELL.value: ItemClassification.useful | ItemClassification.filler,
    Items.TOXIC_BARB.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHARP_HORN.value: ItemClassification.useful | ItemClassification.filler,
    Items.TOUGH_WING.value: ItemClassification.useful | ItemClassification.filler,
    Items.TOUGH_FANG.value: ItemClassification.useful | ItemClassification.filler,
    Items.GREAT_TUSK.value: ItemClassification.useful | ItemClassification.filler,
    Items.GUM_THROAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.ROCK_CORAL.value: ItemClassification.useful | ItemClassification.filler,
    Items.ELASTIC.value: ItemClassification.useful | ItemClassification.filler,
    Items.GLASS_EYE.value: ItemClassification.useful | ItemClassification.filler,
    Items.STEEL_BONE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BONE_SHARD.value: ItemClassification.useful | ItemClassification.filler,
    Items.CARAPACE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BUG_NEST.value: ItemClassification.useful | ItemClassification.filler,
    Items.BAT_WING.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHINY_GOO.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHRED_NAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.RED_HIDE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BLOOD_FANG.value: ItemClassification.useful | ItemClassification.filler,
    Items.SWORDFISH_SCALE.value: ItemClassification.useful | ItemClassification.filler,
    Items.SWORDFISH_FIN.value: ItemClassification.useful | ItemClassification.filler,
    Items.CRAB_LEG.value: ItemClassification.useful | ItemClassification.filler,
    Items.ANT_HONEY.value: ItemClassification.useful | ItemClassification.filler,
    Items.STAB_SHELL.value: ItemClassification.useful | ItemClassification.filler,
    Items.STRAWBERRY.value: ItemClassification.useful | ItemClassification.filler,
    Items.SEA_BRANCH.value: ItemClassification.useful | ItemClassification.filler,
    Items.CORUNDUM.value: ItemClassification.useful | ItemClassification.filler,
    Items.RED_BLADE.value: ItemClassification.useful | ItemClassification.filler,
    Items.DEATH_CLAW.value: ItemClassification.useful | ItemClassification.filler,
    Items.HUGE_FIN.value: ItemClassification.useful | ItemClassification.filler,
    Items.HUNDRED_SHELL.value: ItemClassification.useful | ItemClassification.filler,
    Items.GATOR_SKIN.value: ItemClassification.useful | ItemClassification.filler,
    Items.HEATED_FUR.value: ItemClassification.useful | ItemClassification.filler,
    Items.FIRE_TAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.WHITE_SKIN.value: ItemClassification.useful | ItemClassification.filler,
    Items.WHITE_FANG.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHINY_HORN.value: ItemClassification.useful | ItemClassification.filler,
    Items.MUSK.value: ItemClassification.useful | ItemClassification.filler,
    Items.BROKEN_EYE.value: ItemClassification.useful | ItemClassification.filler,
    Items.SILVER_EYE.value: ItemClassification.useful | ItemClassification.filler,
    Items.NYX_SCYTHE.value: ItemClassification.useful | ItemClassification.filler,
    Items.TENDON.value: ItemClassification.useful | ItemClassification.filler,
    Items.DRIED_VINE.value: ItemClassification.useful | ItemClassification.filler,
    Items.PURE_ROOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.HARD_SHARD.value: ItemClassification.useful | ItemClassification.filler,
    Items.INK_STICK.value: ItemClassification.useful | ItemClassification.filler,
    Items.SAND_CLOTH.value: ItemClassification.useful | ItemClassification.filler,
    Items.SAND_TWIG.value: ItemClassification.useful | ItemClassification.filler,
    Items.FAIRY_WING.value: ItemClassification.useful | ItemClassification.filler,
    Items.FAIRY_SAP.value: ItemClassification.useful | ItemClassification.filler,
    Items.RED_PLUME.value: ItemClassification.useful | ItemClassification.filler,
    Items.RED_BEAK.value: ItemClassification.useful | ItemClassification.filler,
    Items.DRY_PEACH.value: ItemClassification.useful | ItemClassification.filler,
    Items.THROB_VINE.value: ItemClassification.useful | ItemClassification.filler,
    Items.RED_STRING.value: ItemClassification.useful | ItemClassification.filler,
    Items.RED_THREAD.value: ItemClassification.useful | ItemClassification.filler,
    Items.OLEANDER.value: ItemClassification.useful | ItemClassification.filler,
    Items.STEEL_CLAW.value: ItemClassification.useful | ItemClassification.filler,
    Items.STEEL_CHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.CULLINAN.value: ItemClassification.useful | ItemClassification.filler,
    Items.CORDYCEPS.value: ItemClassification.useful | ItemClassification.filler,
    Items.SAP_WINE.value: ItemClassification.useful | ItemClassification.filler,
    Items.SPACE_NAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.TINY_TOOTH.value: ItemClassification.useful | ItemClassification.filler,
    Items.DEMON_FUR.value: ItemClassification.useful | ItemClassification.filler,
    Items.REX_THROAT.value: ItemClassification.useful | ItemClassification.filler,
    Items.GEM_CORE.value: ItemClassification.useful | ItemClassification.filler,
    Items.GUM_THREAD.value: ItemClassification.useful | ItemClassification.filler,
    Items.RED_FUR.value: ItemClassification.useful | ItemClassification.filler,
    Items.RED_BLOOD.value: ItemClassification.useful | ItemClassification.filler,
    Items.GOLD_SHELL.value: ItemClassification.useful | ItemClassification.filler,
    Items.BLUE_BLOOD.value: ItemClassification.useful | ItemClassification.filler,
    Items.DEATH_STEM.value: ItemClassification.useful | ItemClassification.filler,
    Items.GOLD_FUR.value: ItemClassification.useful | ItemClassification.filler,
    Items.GOLD_TUSK.value: ItemClassification.useful | ItemClassification.filler,
    Items.GOLD_HORN.value: ItemClassification.useful | ItemClassification.filler,
    Items.SPACE_HUSK.value: ItemClassification.useful | ItemClassification.filler,
    Items.SPACE_CLAW.value: ItemClassification.useful | ItemClassification.filler,
    Items.ANGEL_WING.value: ItemClassification.useful | ItemClassification.filler,
    Items.LIFE_HONEY.value: ItemClassification.useful | ItemClassification.filler,
    Items.STERNUM.value: ItemClassification.useful | ItemClassification.filler,
    Items.CURSE_TUSK.value: ItemClassification.useful | ItemClassification.filler,
    Items.ROYAL_HIDE.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHROUD.value: ItemClassification.useful | ItemClassification.filler,
    Items.RED_ORE.value: ItemClassification.useful | ItemClassification.filler,
    Items.AMBROSIA.value: ItemClassification.useful | ItemClassification.filler,
    Items.HEADROOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.ARMROOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.LEGROOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.GUM_STRING.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHINY_VINE.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHINY_SEED.value: ItemClassification.useful | ItemClassification.filler,
    Items.DRYWALL.value: ItemClassification.useful | ItemClassification.filler,
    Items.CRYSTWALL.value: ItemClassification.useful | ItemClassification.filler,
    Items.JADE_ORE.value: ItemClassification.useful | ItemClassification.filler,
    Items.AZURE_ORE.value: ItemClassification.useful | ItemClassification.filler,
    Items.EVIL_SHELL.value: ItemClassification.useful | ItemClassification.filler,
    Items.EVIL_SCALE.value: ItemClassification.useful | ItemClassification.filler,
    Items.EVIL_PLUME.value: ItemClassification.useful | ItemClassification.filler,
    Items.EVIL_CREST.value: ItemClassification.useful | ItemClassification.filler,
    Items.OLD_SHELL.value: ItemClassification.useful | ItemClassification.filler,
    Items.GEM_SCALE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BLACK_ROOT.value: ItemClassification.useful | ItemClassification.filler,
    Items.GEM_PLUME.value: ItemClassification.useful | ItemClassification.filler,
    Items.HEX_MARROW.value: ItemClassification.useful | ItemClassification.filler,
    Items.GOLD_PLUME.value: ItemClassification.useful | ItemClassification.filler,
    Items.HELL_WING.value: ItemClassification.useful | ItemClassification.filler,
    Items.VELVET.value: ItemClassification.useful | ItemClassification.filler,
    Items.HOLED_LIMB.value: ItemClassification.useful | ItemClassification.filler,
    Items.RUBY_SKULL.value: ItemClassification.useful | ItemClassification.filler,
    Items.RUBY_BONE.value: ItemClassification.useful | ItemClassification.filler,
    Items.HEX_CHAIN.value: ItemClassification.useful | ItemClassification.filler,
    Items.SWORD_RIB.value: ItemClassification.useful | ItemClassification.filler,
    Items.FLAME_SKIN.value: ItemClassification.useful | ItemClassification.filler,
    Items.FROST_SKIN.value: ItemClassification.useful | ItemClassification.filler,
    Items.VOLT_SKIN.value: ItemClassification.useful | ItemClassification.filler,
    Items.VOLT_CORE.value: ItemClassification.useful | ItemClassification.filler,
    Items.FIRE_SCALE.value: ItemClassification.useful | ItemClassification.filler,
    Items.FIRE_FANG.value: ItemClassification.useful | ItemClassification.filler,
    Items.STATUE_ARM.value: ItemClassification.useful | ItemClassification.filler,
    Items.BEAST_EYE.value: ItemClassification.useful | ItemClassification.filler,
    Items.FROST_BONE.value: ItemClassification.useful | ItemClassification.filler,
    Items.DEMON_CORE.value: ItemClassification.useful | ItemClassification.filler,
    Items.EBON_PLUME.value: ItemClassification.useful | ItemClassification.filler,
    Items.SEA_KING_ICE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BARBEL.value: ItemClassification.useful | ItemClassification.filler,
    Items.ROYAL_VINE.value: ItemClassification.useful | ItemClassification.filler,
    Items.HARVESTER.value: ItemClassification.useful | ItemClassification.filler,
    Items.ROYAL_MANE.value: ItemClassification.useful | ItemClassification.filler,
    Items.ICE_SCALE.value: ItemClassification.useful | ItemClassification.filler,
    Items.WINE_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.ROSE_WHIP.value: ItemClassification.useful | ItemClassification.filler,
    Items.TOXIC_HAND.value: ItemClassification.useful | ItemClassification.filler,
    Items.VOLT_SCALE.value: ItemClassification.useful | ItemClassification.filler,
    Items.YELLOW_ORE.value: ItemClassification.useful | ItemClassification.filler,
    Items.BUG_SCALE.value: ItemClassification.useful | ItemClassification.filler,
    Items.COLD_SCALE.value: ItemClassification.useful | ItemClassification.filler,
    Items.ODD_FRUIT.value: ItemClassification.useful | ItemClassification.filler,
    Items.CROSS_SEED.value: ItemClassification.useful | ItemClassification.filler,
    Items.NARCISSUS.value: ItemClassification.useful | ItemClassification.filler,
    Items.MOSCHINO.value: ItemClassification.useful | ItemClassification.filler,
    Items.SMALL_LEAF.value: ItemClassification.useful | ItemClassification.filler,
    Items.MEDIUM_LEAF.value: ItemClassification.useful | ItemClassification.filler,
    Items.LARGE_LEAF.value: ItemClassification.useful | ItemClassification.filler,
    Items.MEDICA.value: ItemClassification.useful | ItemClassification.filler,
    Items.MEDICA_II.value: ItemClassification.useful | ItemClassification.filler,
    Items.MEDICA_III.value: ItemClassification.useful | ItemClassification.filler,
    Items.MEDICA_IV.value: ItemClassification.useful | ItemClassification.filler,
    Items.MEDICA_V.value: ItemClassification.useful | ItemClassification.filler,
    Items.AMRITA.value: ItemClassification.useful | ItemClassification.filler,
    Items.AMRITA_II.value: ItemClassification.useful | ItemClassification.filler,
    Items.HAMAO.value: ItemClassification.useful | ItemClassification.filler,
    Items.HAMAO_PRIME.value: ItemClassification.useful | ItemClassification.filler,
    Items.SOMA.value: ItemClassification.useful | ItemClassification.filler,
    Items.SOMA_PRIME.value: ItemClassification.useful | ItemClassification.filler,
    Items.NECTAR.value: ItemClassification.useful | ItemClassification.filler,
    Items.NECTAR_II.value: ItemClassification.useful | ItemClassification.filler,
    Items.NECTAR_III.value: ItemClassification.useful | ItemClassification.filler,
    Items.THERIACA_A.value: ItemClassification.useful | ItemClassification.filler,
    Items.THERIACA_B.value: ItemClassification.useful | ItemClassification.filler,
    Items.AXCELA.value: ItemClassification.useful | ItemClassification.filler,
    Items.AXCELA_II.value: ItemClassification.useful | ItemClassification.filler,
    Items.AXCELA_III.value: ItemClassification.useful | ItemClassification.filler,
    Items.BRAVANT.value: ItemClassification.useful | ItemClassification.filler,
    Items.BRAVANT_II.value: ItemClassification.useful | ItemClassification.filler,
    Items.STONARD.value: ItemClassification.useful | ItemClassification.filler,
    Items.STONARD_II.value: ItemClassification.useful | ItemClassification.filler,
    Items.FIRE_MIST.value: ItemClassification.useful | ItemClassification.filler,
    Items.ICE_MIST.value: ItemClassification.useful | ItemClassification.filler,
    Items.VOLT_MIST.value: ItemClassification.useful | ItemClassification.filler,
    Items.ALL_MIST.value: ItemClassification.useful | ItemClassification.filler,
    Items.BLAZE_OIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.FREEZE_OIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHOCK_OIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.WARD_CHIME.value: ItemClassification.useful | ItemClassification.filler,
    Items.GOLD_CHIME.value: ItemClassification.useful | ItemClassification.filler,
    Items.POLE_STONE.value: ItemClassification.useful | ItemClassification.filler,
    Items.MAP_EVENT.value: ItemClassification.useful | ItemClassification.filler,
    Items.HOLY_WATER.value: ItemClassification.useful | ItemClassification.filler,
    Items.WATER.value: ItemClassification.useful | ItemClassification.filler,
    Items.BOTTLE.value: ItemClassification.useful | ItemClassification.filler,
    Items.JUNK_BOX.value: ItemClassification.useful | ItemClassification.filler,
    Items.LOCKET.value: ItemClassification.useful | ItemClassification.filler,
    Items.PLANT_SEED.value: ItemClassification.useful | ItemClassification.filler,
    Items.GOLD_STONE.value: ItemClassification.useful | ItemClassification.filler,
    Items.MOON_STONE.value: ItemClassification.useful | ItemClassification.filler,
    Items.GOUDA.value: ItemClassification.useful | ItemClassification.filler,
    Items.ODD_POWDER.value: ItemClassification.useful | ItemClassification.filler,
    Items.LUCKY_COIN.value: ItemClassification.useful | ItemClassification.filler,
    Items.RUST_SWORD.value: ItemClassification.useful | ItemClassification.filler,
    Items.BROKEN_AXE.value: ItemClassification.useful | ItemClassification.filler,
    Items.OLD_WAND.value: ItemClassification.useful | ItemClassification.filler,
    Items.PANACEA.value: ItemClassification.useful | ItemClassification.filler,
    Items.RARE_BLOOM.value: ItemClassification.useful | ItemClassification.filler,
    Items.GOLD_SEED.value: ItemClassification.useful | ItemClassification.filler,
    Items.VOX_STONE.value: ItemClassification.useful | ItemClassification.filler,
    Items.CLEAR_KEY.value: ItemClassification.progression,
    Items.VIOLET_KEY.value: ItemClassification.progression,
    Items.DRAGON_EGG.value: ItemClassification.useful | ItemClassification.filler,
    Items.CARD_KEY.value: ItemClassification.useful | ItemClassification.filler,
    Items.HOLY_GRAIL.value: ItemClassification.useful | ItemClassification.filler,
    Items.COPPER_TOP.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHINY_DISC.value: ItemClassification.useful | ItemClassification.filler,
    Items.SOFT_GLASS.value: ItemClassification.useful | ItemClassification.filler,
    Items.TOKEN.value: ItemClassification.useful | ItemClassification.filler,
    Items.CLAM_TOOL.value: ItemClassification.useful | ItemClassification.filler,
    Items.MAGIC_DOWN.value: ItemClassification.useful | ItemClassification.filler,
    Items.DIAMOND.value: ItemClassification.useful | ItemClassification.filler,
    Items.BLACK_GEM.value: ItemClassification.useful | ItemClassification.filler,
    Items.SHINY_GEM.value: ItemClassification.useful | ItemClassification.filler,
    Items.OLD_SCROLL.value: ItemClassification.useful | ItemClassification.filler,
    Items.HEX_BELL.value: ItemClassification.useful | ItemClassification.filler,
    Items.LABYRINTH_MAP.value: ItemClassification.progression,
    Items.RADHA_NOTE.value: ItemClassification.progression,
    Items.ARIADNE_THREAD.value: ItemClassification.useful | ItemClassification.filler,
    Items.FROZEN_ARM.value: ItemClassification.useful | ItemClassification.filler,
    Items.ANKH_A.value: ItemClassification.useful | ItemClassification.filler,
    Items.ANKH_B.value: ItemClassification.useful | ItemClassification.filler,
    Items.ANKH_C.value: ItemClassification.useful | ItemClassification.filler,
    Items.ANKH_D.value: ItemClassification.useful | ItemClassification.filler,
    Items.ANKH_E.value: ItemClassification.useful | ItemClassification.filler,
    Items.ANKH_MOTOR.value: ItemClassification.useful | ItemClassification.filler,
    Items.BANDANNA.value: ItemClassification.useful | ItemClassification.filler,
    Items.PEARL.value: ItemClassification.useful | ItemClassification.filler,
    Items.RARE_MEAT.value: ItemClassification.useful | ItemClassification.filler,
    
    # Custom items
    Items.FIRST_STRATUM_CLEARED.value: ItemClassification.progression,
    Items.VICTORY.value: ItemClassification.progression,
    Items.EN500.value: ItemClassification.useful,
    Items.EN200.value: ItemClassification.filler,
    Items.EN100.value: ItemClassification.filler,
    Items.NIGHT_10TP.value: ItemClassification.filler,
    Items.FIRST_CHAR_10HP.value: ItemClassification.filler,
    Items.EN50.value: ItemClassification.filler,
    Items.EN1.value: ItemClassification.filler,
}