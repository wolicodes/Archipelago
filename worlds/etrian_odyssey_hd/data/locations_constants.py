from . import items_constants as itm, regions_constants as reg
from .. import options

# Etria
APOTHECARY_AXCELA = "Apothecary - Axcela"
APOTHECARY_AMRITA = "Apothecary - Amrita"
APOTHECARY_MEDICA = "Apothecary - Medica"
SHOP_SCRAMASAX = "Shop - Scramasax"
SHOP_KNIFE = "Shop - Knife"
SHOP_STAFF = "Shop - Staff"
SHOP_WAND = "Shop - Wand"
SHOP_HATCHET = "Shop - Hatchet"
SHOP_WOOD_BOW = "Shop - Wood Bow"
SHOP_LIGHT_WHIP = "Shop - Light Whip"
SHOP_TWEED = "Shop - Tweed"
SHOP_TARGE = "Shop - Targe"
SHOP_HAIRPIN = "Shop - Hairpin"
SHOP_KNIT_GLOVE = "Shop - Knit Glove"
SHOP_LEAF_BOOT = "Shop - Leaf Boot"
SHOP_HIDE_BELT = "Shop - Hide Belt"
SHOP_WARD_CHIME = "Shop - Ward Chime"
SHOP_ARIADNE_THREAD = "Shop - Ariadne Thread"
ADVENTURERS_INITIATION_COMPLETE = "Adventurers Initiation - Complete"
ADVENTURERS_INITIATION_REWARD_1 = "Adventurers Initiation - Reward 1"
ADVENTURERS_INITIATION_REWARD_2 = "Adventurers Initiation - Reward 2"
# B1F
B1F_MAIN_MOLES_WHITESTONE = "B1F Main - Moles Whitestone" # Whitestone
B1F_MAIN_A3_TOP_CHEST = "B1F Main - A3 Top Chest" # Scramasax
B1F_MAIN_A3_MIDDLE_CHEST = "B1F Main - A3 Middle Chest" # Medica II
B1F_MAIN_A3_BOTTOM_CHEST = "B1F Main - A3 Bottom Chest" # 200en
B1F_MAIN_EVENT_MOLES_ATTACK = "B1F Main - Event Moles Attack" # Nothing
B1F_MAIN_EVENT_SIP_WATER = "B1F Main - Event Sip Water" # 10TP at night
B1F_MAIN_EVENT_RED_FRUIT = "B1F Main - Event Red Fruit" # 10HP First character
B1F_MAIN_EVENT_OLD_RUCKSACK = "B1F Main - Event Old Rucksack" # 100en
B1F_MAIN_EVENT_VENOMFLIES_ATTACK = "B1F Main - Event Venomflies Attack" # Nothing
B1F_MAIN_D1_CHOP = "B1F Main - D1 Chop"
B1F_MAIN_D3_CHOP = "B1F Main - D3 Chop"
B1F_CLEAR_CRYSTAL_ROOM_CHEST = "B1F Clear Crystal Room - Chest" # Nectar
B1F_VIOLET_CRYSTAL_ROOM_TOP_CHEST = "B1F Violet Crystal Room - Top Chest" # Nectar II
B1F_VIOLET_CRYSTAL_ROOM_BOTTOM_CHEST = "B1F Violet Crystal Room - Bottom Chest" # Gem Staff
B1F_EAST_NORTH_CHEST = "B1F East - North Chest" # Plumed Hat
B1F_EAST_RAGELOPE_TOP_CHEST = "B1F East - Ragelope Top Chest" # Medica II
B1F_EAST_RAGELOPE_MIDDLE_CHEST = "B1F East - Ragelope Middle Chest" # Rapier
B1F_EAST_RAGELOPE_BOTTOM_CHEST = "B1F East - Ragelope Bottom Chest" # 500en
# B5F
FIRST_STRATUM_CLEARED = "First Stratum Cleard"

LOCATION_DATA = {
    APOTHECARY_AXCELA: {
        "id": 1,
        "region": reg.ETRIA,
        "vanilla": itm.AXCELA,
        "option": options.SHOP_SANITY
    },
    APOTHECARY_AMRITA: {
        "id": 2,
        "region": reg.ETRIA,
        "vanilla": itm.AMRITA,
        "option": options.SHOP_SANITY
    },
    APOTHECARY_MEDICA: {
        "id": 3,
        "region": reg.ETRIA,
        "vanilla": itm.MEDICA,
        "option": options.SHOP_SANITY
    },
    SHOP_SCRAMASAX: {
        "id": 4,
        "region": reg.ETRIA,
        "vanilla": itm.SCRAMASAX,
        "option": options.SHOP_SANITY
    },
    SHOP_KNIFE: {
        "id": 5,
        "region": reg.ETRIA,
        "vanilla": itm.KNIFE,
        "option": options.SHOP_SANITY
    },
    SHOP_STAFF: {
        "id": 6,
        "region": reg.ETRIA,
        "vanilla": itm.STAFF,
        "option": options.SHOP_SANITY
    },
    SHOP_WAND: {
        "id": 7,
        "region": reg.ETRIA,
        "vanilla": itm.WAND,
        "option": options.SHOP_SANITY
    },
    SHOP_HATCHET: {
        "id": 8,
        "region": reg.ETRIA,
        "vanilla": itm.HATCHET,
        "option": options.SHOP_SANITY
    },
    SHOP_WOOD_BOW: {
        "id": 9,
        "region": reg.ETRIA,
        "vanilla": itm.WOOD_BOW,
        "option": options.SHOP_SANITY
    },
    SHOP_LIGHT_WHIP: {
        "id": 10,
        "region": reg.ETRIA,
        "vanilla": itm.LIGHT_WHIP,
        "option": options.SHOP_SANITY
    },
    SHOP_TWEED: {
        "id": 11,
        "region": reg.ETRIA,
        "vanilla": itm.TWEED,
        "option": options.SHOP_SANITY
    },
    SHOP_TARGE: {
        "id": 12,
        "region": reg.ETRIA,
        "vanilla": itm.TARGE,
        "option": options.SHOP_SANITY
    },
    SHOP_HAIRPIN: {
        "id": 13,
        "region": reg.ETRIA,
        "vanilla": itm.HAIRPIN,
        "option": options.SHOP_SANITY
    },
    SHOP_KNIT_GLOVE: {
        "id": 14,
        "region": reg.ETRIA,
        "vanilla": itm.KNIT_GLOVE,
        "option": options.SHOP_SANITY
    },
    SHOP_LEAF_BOOT: {
        "id": 15,
        "region": reg.ETRIA,
        "vanilla": itm.LEAF_BOOT,
        "option": options.SHOP_SANITY
    },
    SHOP_HIDE_BELT: {
        "id": 16,
        "region": reg.ETRIA,
        "vanilla": itm.HIDE_BELT,
        "option": options.SHOP_SANITY
    },
    SHOP_WARD_CHIME: {
        "id": 17,
        "region": reg.ETRIA,
        "vanilla": itm.WARD_CHIME,
        "option": options.SHOP_SANITY
    },
    SHOP_ARIADNE_THREAD: {
        "id": 19,
        "region": reg.ETRIA,
        "vanilla": itm.ARIADNE_THREAD,
        "option": options.SHOP_SANITY
    },
    B1F_MAIN_MOLES_WHITESTONE: {
        "id": 20,
        "region": reg.B1F_MAIN,
        "vanilla": itm.WHITESTONE
    },
    B1F_MAIN_A3_TOP_CHEST: {
        "id": 21,
        "region": reg.B1F_MAIN,
        "vanilla": itm.SCRAMASAX
    },
    B1F_MAIN_A3_MIDDLE_CHEST: {
        "id": 22,
        "region": reg.B1F_MAIN,
        "vanilla": itm.MEDICA_II
    },
    B1F_MAIN_A3_BOTTOM_CHEST: {
        "id": 23,
        "region": reg.B1F_MAIN,
        "vanilla": itm.EN200
    },
    B1F_CLEAR_CRYSTAL_ROOM_CHEST: {
        "id": 24,
        "region": reg.B1F_CLEAR_CRYSTAL_ROOM,
        "vanilla": itm.NECTAR
    },
    B1F_VIOLET_CRYSTAL_ROOM_TOP_CHEST: {
        "id": 25,
        "region": reg.B1F_VIOLET_CRYSTAL_ROOM,
        "vanilla": itm.NECTAR_II
    },
    B1F_VIOLET_CRYSTAL_ROOM_BOTTOM_CHEST: {
        "id": 26,
        "region": reg.B1F_VIOLET_CRYSTAL_ROOM,
        "vanilla": itm.GEM_STAFF
    },
    B1F_EAST_NORTH_CHEST: {
        "id": 27,
        "region": reg.B1F_EAST,
        "vanilla": itm.PLUMED_HAT
    },
    B1F_EAST_RAGELOPE_TOP_CHEST: {
        "id": 28,
        "region": reg.B1F_EAST,
        "vanilla": itm.MEDICA_II
    },
    B1F_EAST_RAGELOPE_MIDDLE_CHEST: {
        "id": 29,
        "region": reg.B1F_EAST,
        "vanilla": itm.RAPIER
    },
    B1F_EAST_RAGELOPE_BOTTOM_CHEST: {
        "id": 30,
        "region": reg.B1F_EAST,
        "vanilla": itm.EN500
    },
    B1F_MAIN_EVENT_MOLES_ATTACK: {
        "id": 31,
        "region": reg.B1F_MAIN,
        "vanilla": None
    },
    B1F_MAIN_EVENT_SIP_WATER: {
        "id": 32,
        "region": reg.B1F_MAIN,
        "vanilla": itm.NIGHT_10TP
    },
    B1F_MAIN_EVENT_RED_FRUIT: {
        "id": 33,
        "region": reg.B1F_MAIN,
        "vanilla": itm.FIRST_CHAR_10HP
    },
    B1F_MAIN_EVENT_OLD_RUCKSACK: {
        "id": 34,
        "region": reg.B1F_MAIN,
        "vanilla": itm.EN100
    },
    B1F_MAIN_EVENT_VENOMFLIES_ATTACK: {
        "id": 35,
        "region": reg.B1F_MAIN,
        "vanilla": None,
        "event": itm.FIRST_STRATUM_CLEARED
    },
    B1F_MAIN_D1_CHOP: {
        "id": 36,
        "region": reg.B1F_MAIN,
        "vanilla": itm.VIOLET_KEY # TODO Change this
    },
    B1F_MAIN_D3_CHOP: {
        "id": 37,
        "region": reg.B1F_MAIN,
        "vanilla": itm.CLEAR_KEY # TODO Change this
    },
    ADVENTURERS_INITIATION_COMPLETE: {
        "id": 38,
        "region": reg.ETRIA,
        "vanilla": None,
        "event": itm.VICTORY
    },
    ADVENTURERS_INITIATION_REWARD_1: {
        "id": 39,
        "region": reg.ETRIA,
        "vanilla": itm.RADHA_NOTE
    },
    ADVENTURERS_INITIATION_REWARD_2: {
        "id": 40,
        "region": reg.ETRIA,
        "vanilla": itm.EN500
    },
}

LOCATION_NAME_TO_ID = {
    name: data["id"] for name, data in LOCATION_DATA.items()
}
