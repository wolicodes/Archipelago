"""Module containing all the location data for Etrian Odyssey HD"""

from dataclasses import dataclass
from enum import Flag, auto
from typing import Optional
from . import items_constants as itm, regions_constants as reg


class EOHDFlag(Flag):
    """
    This class represents flags used for categorizing game locations.
    Flags are used to group locations by their specific gameplay or logic attributes.
    """

    ALWAYS = auto()
    SHOP = auto()
    EVENT = auto()
    EVENT_ITEM = auto()


@dataclass(frozen=True)
class EOHDLocationData:
    """
    This class represents the data for a location in Etrian Odyssey HD.

    :param code: The unique code identifier for the location.
    :param flags: The flags that categorize the location.
    :param region: The name of the region where the location resides.
    :param item: The item that will be shuffled in the pool when this location is active.
    """

    id: int
    region: str
    item: Optional[str]
    event: Optional[str]
    flags: EOHDFlag


# Missing Clear key, violet key, first stratum complete, victory
LOCATION_DATA: dict[str, EOHDLocationData] = {
    "Etria - Apothecary Axcela": EOHDLocationData(1, reg.ETRIA, itm.AXCELA, None, EOHDFlag.SHOP),
    "Etria - Apothecary Amrita": EOHDLocationData(2, reg.ETRIA, itm.AMRITA, None, EOHDFlag.SHOP),
    "Etria - Apothecary Medica": EOHDLocationData(3, reg.ETRIA, itm.MEDICA, None, EOHDFlag.SHOP),
    "Etria - Shop Scramasax": EOHDLocationData(4, reg.ETRIA, itm.SCRAMASAX, None, EOHDFlag.SHOP),
    "Etria - Shop Knife": EOHDLocationData(5, reg.ETRIA, itm.KNIFE, None, EOHDFlag.SHOP),
    "Etria - Shop Staff": EOHDLocationData(6, reg.ETRIA, itm.STAFF, None, EOHDFlag.SHOP),
    "Etria - Shop Wand": EOHDLocationData(7, reg.ETRIA, itm.WAND, None, EOHDFlag.SHOP),
    "Etria - Shop Hatchet": EOHDLocationData(8, reg.ETRIA, itm.HATCHET, None, EOHDFlag.SHOP),
    "Etria - Shop Wood Bow": EOHDLocationData(9, reg.ETRIA, itm.WOOD_BOW, None, EOHDFlag.SHOP),
    "Etria - Shop Light Whip": EOHDLocationData(10, reg.ETRIA, itm.LIGHT_WHIP, None, EOHDFlag.SHOP),
    "Etria - Shop Tweed": EOHDLocationData(11, reg.ETRIA, itm.TWEED, None, EOHDFlag.SHOP),
    "Etria - Shop Targe": EOHDLocationData(12, reg.ETRIA, itm.TARGE, None, EOHDFlag.SHOP),
    "Etria - Shop Hairpin": EOHDLocationData(13, reg.ETRIA, itm.HAIRPIN, None, EOHDFlag.SHOP),
    "Etria - Shop Knit Glove": EOHDLocationData(14, reg.ETRIA, itm.KNIT_GLOVE, None, EOHDFlag.SHOP),
    "Etria - Shop Leaf Boot": EOHDLocationData(15, reg.ETRIA, itm.LEAF_BOOT, None, EOHDFlag.SHOP),
    "Etria - Shop Hide Belt": EOHDLocationData(16, reg.ETRIA, itm.HIDE_BELT, None, EOHDFlag.SHOP),
    "Etria - Shop Ward Chime": EOHDLocationData(17, reg.ETRIA, itm.WARD_CHIME, None, EOHDFlag.SHOP),
    "Etria - Shop Ariadne Thread": EOHDLocationData(18, reg.ETRIA, itm.ARIADNE_THREAD, None, EOHDFlag.SHOP),
    "Etria - Adventurers Initiation Reward 1": EOHDLocationData(19, reg.ETRIA, itm.RADHA_NOTE, None, EOHDFlag.ALWAYS),
    "Etria - Adventurers Initiation Reward 2": EOHDLocationData(20, reg.ETRIA, itm.EN500, None, EOHDFlag.ALWAYS),

    "B1F Main - Event Moles Attack": EOHDLocationData(21, reg.B1F_MAIN, None, None, EOHDFlag.EVENT),
    "B1F Main - Moles Whitestone": EOHDLocationData(22, reg.B1F_MAIN, itm.WHITESTONE, None, EOHDFlag.EVENT_ITEM),
    "B1F Main - A3 Top Chest": EOHDLocationData(23, reg.B1F_MAIN, itm.SCRAMASAX, None, EOHDFlag.ALWAYS),
    "B1F Main - A3 Middle Chest": EOHDLocationData(24, reg.B1F_MAIN, itm.MEDICA_II, None, EOHDFlag.ALWAYS),
    "B1F Main - A3 Bottom Chest": EOHDLocationData(25, reg.B1F_MAIN, itm.EN200, None, EOHDFlag.ALWAYS),
    "B1F Main - Event Red Fruit": EOHDLocationData(26, reg.B1F_MAIN, None, None, EOHDFlag.EVENT),
    "B1F Main - Event Old Rucksack": EOHDLocationData(27, reg.B1F_MAIN, None, None, EOHDFlag.EVENT),
    "B1F Main - Old Rucksack 100en": EOHDLocationData(28, reg.B1F_MAIN, itm.EN100, None, EOHDFlag.EVENT_ITEM),
    "B1F Main - Event Venomflies Attack": EOHDLocationData(29, reg.B1F_MAIN, None, None, EOHDFlag.EVENT),

    "B1F Clear Crystal Room - Chest": EOHDLocationData(30, reg.B1F_CLEAR_CRYSTAL_ROOM, itm.NECTAR, None, EOHDFlag.ALWAYS),

    "B1F Violet Crystal Room - Top Chest": EOHDLocationData(31, reg.B1F_VIOLET_CRYSTAL_ROOM, itm.NECTAR_II, None, EOHDFlag.ALWAYS),
    "B1F Violet Crystal Room - Bottom Chest": EOHDLocationData(32, reg.B1F_VIOLET_CRYSTAL_ROOM, itm.GEM_STAFF, None, EOHDFlag.ALWAYS),

    "B1F East - North Chest": EOHDLocationData(33, reg.B1F_EAST, itm.PLUMED_HAT, None, EOHDFlag.ALWAYS),
    "B1F East - Ragelope Top Chest": EOHDLocationData(34, reg.B1F_EAST, itm.MEDICA_II, None, EOHDFlag.ALWAYS),
    "B1F East - Ragelope Middle Chest": EOHDLocationData(35, reg.B1F_EAST, itm.RAPIER, None, EOHDFlag.ALWAYS),
    "B1F East - Ragelope Bottom Chest": EOHDLocationData(36, reg.B1F_EAST, itm.EN500, None, EOHDFlag.ALWAYS),

    # B2F
    "B2F Main - A3 Chest": EOHDLocationData(37, reg.B2F_MAIN, itm.ARIADNE_THREAD, None, EOHDFlag.ALWAYS),
    "B2F Main - C1 Chest": EOHDLocationData(38, reg.B2F_MAIN, itm.NECTAR, None, EOHDFlag.ALWAYS),
    "B2F Main - A6 Chest": EOHDLocationData(39, reg.B2F_MAIN, itm.BUFFCOAT, None, EOHDFlag.ALWAYS),
    "B2F Clear Crystal Room - Top Chest": EOHDLocationData(40, reg.B2F_CLEAR_CRYSTAL_ROOM, itm.MEDICA_IV, None, EOHDFlag.ALWAYS),
    "B2F Clear Crystal Room - Bottom Chest": EOHDLocationData(41, reg.B2F_CLEAR_CRYSTAL_ROOM, itm.SOMA, None, EOHDFlag.ALWAYS),
    # B3F
    "B3F Main - Stalker Hallway Top Chest": EOHDLocationData(41, reg.B3F_MAIN, itm.EN400, None, EOHDFlag.ALWAYS),
    "B3F Main - Stalker Hallway Middle Chest": EOHDLocationData(42, reg.B3F_MAIN, itm.MEDICA_III, None, EOHDFlag.ALWAYS),
    "B3F Main - Stalker Hallway Bottom Chest": EOHDLocationData(43, reg.B3F_MAIN, itm.HIDE_BOOT, None, EOHDFlag.ALWAYS),
    "B3F Main - F2 Chest": EOHDLocationData(44, reg.B3F_MAIN, itm.THERIACA_A, None, EOHDFlag.ALWAYS),
    "B3F Main - F4 Chest": EOHDLocationData(45, reg.B3F_MAIN, itm.EN500, None, EOHDFlag.ALWAYS),
    # B4F
    "B4F Main - F2 Chest": EOHDLocationData(46, reg.B4F_MAIN, itm.BRAVANT, None, EOHDFlag.ALWAYS),
    "B4F Main - Wolf Circling Chest": EOHDLocationData(47, reg.B4F_MAIN, itm.PLATE, None, EOHDFlag.ALWAYS),
    "B4F Main - B3 Chest": EOHDLocationData(48, reg.B4F_MAIN, itm.MEDICA_II, None, EOHDFlag.ALWAYS),
    "B4F Main - A1 Chest": EOHDLocationData(49, reg.B4F_MAIN, itm.AMRITA, None, EOHDFlag.ALWAYS),
    # B5F
    "B5F Main - E1 Left Chest": EOHDLocationData(50, reg.B5F_MAIN, itm.NECTAR_II, None, EOHDFlag.ALWAYS),
    "B5F Main - E1 Right Chest": EOHDLocationData(51, reg.B5F_MAIN, itm.BRAVANT_II, None, EOHDFlag.ALWAYS),
    "B5F Main - E6 Chest": EOHDLocationData(52, reg.B5F_MAIN, itm.BLAZE_OIL, None, EOHDFlag.ALWAYS),
    "B5F Main - B7 Chest": EOHDLocationData(53, reg.B5F_MAIN, itm.AMRITA, None, EOHDFlag.ALWAYS),
    "B5F Main - C7 Chest": EOHDLocationData(54, reg.B5F_MAIN, itm.BOAR_SPEAR, None, EOHDFlag.ALWAYS),
}

LOCATION_NAME_TO_ID = {
    name: data.id for name, data in LOCATION_DATA.items()
}
