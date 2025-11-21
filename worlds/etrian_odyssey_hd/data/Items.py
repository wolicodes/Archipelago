
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
    Items.AXCELA.value: 1,
    Items.AMRITA.value: 2,
    Items.MEDICA.value: 3,
    Items.MEDICA_II.value: 4,
    Items.NECTAR.value: 5,
    Items.NECTAR_II.value: 6,
    Items.SCRAMASAX.value: 7,
    Items.KNIFE.value: 8,
    Items.STAFF.value: 9,
    Items.WAND.value: 10,
    Items.HATCHET.value: 11,
    Items.WOOD_BOW.value: 12,
    Items.LIGHT_WHIP.value: 13,
    Items.TWEED.value: 14,
    Items.TARGE.value: 15,
    Items.HAIRPIN.value: 16,
    Items.KNIT_GLOVE.value: 17,
    Items.LEAF_BOOT.value: 18,
    Items.HIDE_BELT.value: 19,
    Items.WARD_CHIME.value: 20,
    Items.ARIADNE_THREAD.value: 21,
    Items.WHITESTONE.value: 22,
    Items.GEM_STAFF.value: 23,
    Items.PLUMED_HAT.value: 24,
    Items.RAPIER.value: 25,
    Items.CLEAR_KEY.value: 26,
    Items.VIOLET_KEY.value: 27,
    Items.FIRST_STRATUM_CLEARED.value: 28,
    Items.RADHA_NOTE.value: 29,
    Items.VICTORY.value: 30,
    Items.EN500.value: 31,
    Items.EN200.value: 32,
    Items.EN100.value: 33,
    Items.NIGHT_10TP.value: 34,
    Items.FIRST_CHAR_10HP.value: 35,
    Items.EN50.value: 36,
    Items.EN1.value: 37,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    Items.AXCELA.value: ItemClassification.useful,
    Items.AMRITA.value: ItemClassification.useful,
    Items.MEDICA.value: ItemClassification.useful,
    Items.MEDICA_II.value: ItemClassification.useful,
    Items.NECTAR.value: ItemClassification.useful,
    Items.NECTAR_II.value: ItemClassification.useful,
    Items.SCRAMASAX.value: ItemClassification.useful,
    Items.KNIFE.value: ItemClassification.useful,
    Items.STAFF.value: ItemClassification.useful,
    Items.WAND.value: ItemClassification.useful,
    Items.HATCHET.value: ItemClassification.useful,
    Items.WOOD_BOW.value: ItemClassification.useful,
    Items.LIGHT_WHIP.value: ItemClassification.useful,
    Items.TWEED.value: ItemClassification.useful,
    Items.TARGE.value: ItemClassification.useful,
    Items.HAIRPIN.value: ItemClassification.useful,
    Items.KNIT_GLOVE.value: ItemClassification.useful,
    Items.LEAF_BOOT.value: ItemClassification.useful,
    Items.HIDE_BELT.value: ItemClassification.useful,
    Items.WARD_CHIME.value: ItemClassification.useful,
    Items.ARIADNE_THREAD.value: ItemClassification.useful,
    Items.WHITESTONE.value: ItemClassification.useful,
    Items.GEM_STAFF.value: ItemClassification.useful,
    Items.PLUMED_HAT.value: ItemClassification.useful,
    Items.RAPIER.value: ItemClassification.useful,
    Items.CLEAR_KEY.value: ItemClassification.progression,
    Items.VIOLET_KEY.value: ItemClassification.progression,
    Items.FIRST_STRATUM_CLEARED.value: ItemClassification.progression,
    Items.RADHA_NOTE.value: ItemClassification.progression,
    Items.VICTORY.value: ItemClassification.progression,
    Items.EN500.value: ItemClassification.useful,
    Items.EN200.value: ItemClassification.filler,
    Items.EN100.value: ItemClassification.filler,
    Items.NIGHT_10TP.value: ItemClassification.filler,
    Items.FIRST_CHAR_10HP.value: ItemClassification.filler,
    Items.EN50.value: ItemClassification.filler,
    Items.EN1.value: ItemClassification.filler,
}