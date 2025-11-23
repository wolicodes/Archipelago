from enum import Enum

class Locations(str, Enum):
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

ETRIA_LOCATIONS = [
    Locations.APOTHECARY_AXCELA.value,
    Locations.APOTHECARY_AMRITA.value,
    Locations.APOTHECARY_MEDICA.value,
    Locations.SHOP_SCRAMASAX.value,
    Locations.SHOP_KNIFE.value,
    Locations.SHOP_STAFF.value,
    Locations.SHOP_WAND.value,
    Locations.SHOP_HATCHET.value,
    Locations.SHOP_WOOD_BOW.value,
    Locations.SHOP_LIGHT_WHIP.value,
    Locations.SHOP_TWEED.value,
    Locations.SHOP_TARGE.value,
    Locations.SHOP_HAIRPIN.value,
    Locations.SHOP_KNIT_GLOVE.value,
    Locations.SHOP_LEAF_BOOT.value,
    Locations.SHOP_HIDE_BELT.value,
    Locations.SHOP_WARD_CHIME.value,
    Locations.SHOP_ARIADNE_THREAD.value,
    Locations.ADVENTURERS_INITIATION_REWARD_1.value,
    Locations.ADVENTURERS_INITIATION_REWARD_2.value
]

B1F_MAIN_LOCATIONS = [
    Locations.B1F_MAIN_MOLES_WHITESTONE.value,
    Locations.B1F_MAIN_A3_TOP_CHEST.value,
    Locations.B1F_MAIN_A3_MIDDLE_CHEST.value,
    Locations.B1F_MAIN_A3_BOTTOM_CHEST.value,
    Locations.B1F_MAIN_EVENT_MOLES_ATTACK.value,
    Locations.B1F_MAIN_EVENT_SIP_WATER.value,
    Locations.B1F_MAIN_EVENT_RED_FRUIT.value,
    Locations.B1F_MAIN_EVENT_OLD_RUCKSACK.value,
    Locations.B1F_MAIN_EVENT_VENOMFLIES_ATTACK.value,
    Locations.B1F_MAIN_D1_CHOP.value,
    Locations.B1F_MAIN_D3_CHOP.value,
]

LOCATION_NAME_TO_ID = {
    Locations.APOTHECARY_AXCELA.value: 1,
    Locations.APOTHECARY_AMRITA.value: 2,
    Locations.APOTHECARY_MEDICA.value: 3,
    Locations.SHOP_SCRAMASAX.value: 4,
    Locations.SHOP_KNIFE.value: 5,
    Locations.SHOP_STAFF.value: 6,
    Locations.SHOP_WAND.value: 7,
    Locations.SHOP_HATCHET.value: 8,
    Locations.SHOP_WOOD_BOW.value: 9,
    Locations.SHOP_LIGHT_WHIP.value: 10,
    Locations.SHOP_TWEED.value: 11,
    Locations.SHOP_TARGE.value: 12,
    Locations.SHOP_HAIRPIN.value: 13,
    Locations.SHOP_KNIT_GLOVE.value: 14,
    Locations.SHOP_LEAF_BOOT.value: 15,
    Locations.SHOP_HIDE_BELT.value: 16,
    Locations.SHOP_WARD_CHIME.value: 17,
    Locations.SHOP_ARIADNE_THREAD.value: 19,
    Locations.B1F_MAIN_MOLES_WHITESTONE.value: 20,
    Locations.B1F_MAIN_A3_TOP_CHEST.value: 21,
    Locations.B1F_MAIN_A3_MIDDLE_CHEST.value: 22,
    Locations.B1F_MAIN_A3_BOTTOM_CHEST.value: 23,
    Locations.B1F_CLEAR_CRYSTAL_ROOM_CHEST.value: 24,
    Locations.B1F_VIOLET_CRYSTAL_ROOM_TOP_CHEST.value: 25,
    Locations.B1F_VIOLET_CRYSTAL_ROOM_BOTTOM_CHEST.value: 26,
    Locations.B1F_EAST_NORTH_CHEST.value: 27,
    Locations.B1F_EAST_RAGELOPE_TOP_CHEST.value: 28,
    Locations.B1F_EAST_RAGELOPE_MIDDLE_CHEST.value: 29,
    Locations.B1F_EAST_RAGELOPE_BOTTOM_CHEST.value: 30,
    Locations.B1F_MAIN_EVENT_MOLES_ATTACK.value: 31,
    Locations.B1F_MAIN_EVENT_SIP_WATER.value: 32,
    Locations.B1F_MAIN_EVENT_RED_FRUIT.value: 33,
    Locations.B1F_MAIN_EVENT_OLD_RUCKSACK.value: 34,
    Locations.B1F_MAIN_EVENT_VENOMFLIES_ATTACK.value: 35,
    Locations.B1F_MAIN_D1_CHOP.value: 36,
    Locations.B1F_MAIN_D3_CHOP.value: 37,
    Locations.ADVENTURERS_INITIATION_COMPLETE.value: 38,
    Locations.ADVENTURERS_INITIATION_REWARD_1.value: 39,
    Locations.ADVENTURERS_INITIATION_REWARD_2.value: 40,
}