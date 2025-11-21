
from enum import Enum
from BaseClasses import Item, ItemClassification

class Items(str, Enum):
    AXCELA = "Axcela"
    AMRITA = "Amrita"
    MEDICA = "Medica"
    MEDICA_II = "Medica II"
    NECTAR = "Nectar"
    NECTAR_II = "Nectar II"
    SCRAMASAX = "Scramasax"
    KNIFE = "Knife"
    STAFF = "Staff"
    WAND = "Wand"
    HATCHET = "Hatchet"
    WOOD_BOW = "Wood Bow"
    LIGHT_WHIP = "Light Whip"
    TWEED = "Tweed"
    TARGE = "Targe"
    HAIRPIN = "Hairpin"
    KNIT_GLOVE = "Knit Glove"
    LEAF_BOOT = "Leaf Boot"
    HIDE_BELT = "Hide Belt"
    WARD_CHIME = "Ward Chime"
    ARIADNE_THREAD = "Ariadne Thread"
    WHITESTONE = "Whitestone"
    GEM_STAFF = "Gem Staff"
    PLUMED_HAT = "Plumed Hat"
    RAPIER = "Rapier"
    CLEAR_KEY = "Clear Key"
    VIOLET_KEY = "Violet Key"
    FIRST_STRATUM_CLEARED = "First Stratum Cleared"
    RADHA_NOTE = "Radha Note"
    VICTORY = "Victory"
    EN500 = "500en"
    EN200 = "200en"
    EN100 = "100en"
    NIGHT_10TP = "Feeling refreshed"
    FIRST_CHAR_10HP = "Ate a red fruit"
    # Fillers
    EN50 = "50en"
    EN1 = "1en"

ITEM_NAME_TO_ID = {
    Items.AXCELA: 1,
    Items.AMRITA: 2,
    Items.MEDICA: 3,
    Items.MEDICA_II: 4,
    Items.NECTAR: 5,
    Items.NECTAR_II: 6,
    Items.SCRAMASAX: 7,
    Items.KNIFE: 8,
    Items.STAFF: 9,
    Items.WAND: 10,
    Items.HATCHET: 11,
    Items.WOOD_BOW: 12,
    Items.LIGHT_WHIP: 13,
    Items.TWEED: 14,
    Items.TARGE: 15,
    Items.HAIRPIN: 16,
    Items.KNIT_GLOVE: 17,
    Items.LEAF_BOOT: 18,
    Items.HIDE_BELT: 19,
    Items.WARD_CHIME: 20,
    Items.ARIADNE_THREAD: 21,
    Items.WHITESTONE: 22,
    Items.GEM_STAFF: 23,
    Items.PLUMED_HAT: 24,
    Items.RAPIER: 25,
    Items.CLEAR_KEY: 26,
    Items.VIOLET_KEY: 27,
    Items.FIRST_STRATUM_CLEARED: 28,
    Items.RADHA_NOTE: 29,
    Items.VICTORY: 30,
    Items.EN500: 31,
    Items.EN200: 32,
    Items.EN100: 33,
    Items.NIGHT_10TP: 34,
    Items.FIRST_CHAR_10HP: 35,
    Items.EN50: 36,
    Items.EN1: 37,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    Items.AXCELA: ItemClassification.useful,
    Items.AMRITA: ItemClassification.useful,
    Items.MEDICA: ItemClassification.useful,
    Items.MEDICA_II: ItemClassification.useful,
    Items.NECTAR: ItemClassification.useful,
    Items.NECTAR_II: ItemClassification.useful,
    Items.SCRAMASAX: ItemClassification.useful,
    Items.KNIFE: ItemClassification.useful,
    Items.STAFF: ItemClassification.useful,
    Items.WAND: ItemClassification.useful,
    Items.HATCHET: ItemClassification.useful,
    Items.WOOD_BOW: ItemClassification.useful,
    Items.LIGHT_WHIP: ItemClassification.useful,
    Items.TWEED: ItemClassification.useful,
    Items.TARGE: ItemClassification.useful,
    Items.HAIRPIN: ItemClassification.useful,
    Items.KNIT_GLOVE: ItemClassification.useful,
    Items.LEAF_BOOT: ItemClassification.useful,
    Items.HIDE_BELT: ItemClassification.useful,
    Items.WARD_CHIME: ItemClassification.useful,
    Items.ARIADNE_THREAD: ItemClassification.useful,
    Items.WHITESTONE: ItemClassification.useful,
    Items.GEM_STAFF: ItemClassification.useful,
    Items.PLUMED_HAT: ItemClassification.useful,
    Items.RAPIER: ItemClassification.useful,
    Items.CLEAR_KEY: ItemClassification.progression,
    Items.VIOLET_KEY: ItemClassification.progression,
    Items.FIRST_STRATUM_CLEARED: ItemClassification.progression,
    Items.RADHA_NOTE: ItemClassification.progression,
    Items.VICTORY: ItemClassification.progression,
    Items.EN500: ItemClassification.useful,
    Items.EN200: ItemClassification.filler,
    Items.EN100: ItemClassification.filler,
    Items.NIGHT_10TP: ItemClassification.filler,
    Items.FIRST_CHAR_10HP: ItemClassification.filler,
    Items.EN50: ItemClassification.filler,
    Items.EN1: ItemClassification.filler,
}