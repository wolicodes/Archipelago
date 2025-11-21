
from enum import Enum
from BaseClasses import Item, ItemClassification

class EOHDItem(Item):
    game = "Etrian Odyssey HD"

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
    Items.CLEAR_KEY: 1,
    Items.VIOLET_KEY: 2,
    Items.FIRST_STRATUM_CLEARED: 3,
    Items.RADHA_NOTE: 4,
    Items.VICTORY: 5,
    Items.EN200: 6,
    Items.EN100: 7,
    Items.EN50: 8,
    Items.EN1: 9,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    Items.CLEAR_KEY: ItemClassification.progression,
    Items.VIOLET_KEY: ItemClassification.progression,
    Items.FIRST_STRATUM_CLEARED: ItemClassification.progression,
    Items.RADHA_NOTE: ItemClassification.progression,
    Items.VICTORY: ItemClassification.progression,
    Items.EN200: ItemClassification.filler,
    Items.EN100: ItemClassification.filler,
    Items.EN50: ItemClassification.filler,
    Items.EN1: ItemClassification.filler,
}