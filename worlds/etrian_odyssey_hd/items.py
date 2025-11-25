from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item
from worlds.etrian_odyssey_hd.data import items_constants as itm

if TYPE_CHECKING:
    from .world import EOHDWorld


class EOHDItem(Item):
    game = "Etrian Odyssey HD"


def get_random_filler_item_name(world: EOHDWorld) -> str:
    if world.random.randint(0, 100) == 1:
        return itm.EN1
    if world.random.randint(0, 100) <= 50:
        return itm.EN50
    return itm.EN100


def create_item_with_correct_classification(world: EOHDWorld, name: str) -> EOHDItem:
    classification = itm.DEFAULT_ITEM_CLASSIFICATIONS[name]
    return EOHDItem(name, classification, itm.ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: EOHDWorld) -> None:
    itempool: list[Item] = [
        world.create_item(itm.AXCELA),
        world.create_item(itm.AMRITA),
        world.create_item(itm.MEDICA),
        world.create_item(itm.SCRAMASAX),
        world.create_item(itm.KNIFE),
        world.create_item(itm.STAFF),
        world.create_item(itm.WAND),
        world.create_item(itm.HATCHET),
        world.create_item(itm.WOOD_BOW),
        world.create_item(itm.LIGHT_WHIP),
        world.create_item(itm.TWEED),
        world.create_item(itm.TARGE),
        world.create_item(itm.HAIRPIN),
        world.create_item(itm.KNIT_GLOVE),
        world.create_item(itm.LEAF_BOOT),
        world.create_item(itm.HIDE_BELT),
        world.create_item(itm.WARD_CHIME),
        world.create_item(itm.ARIADNE_THREAD),
        # world.create_item(itm.VICTORY),
        world.create_item(itm.RADHA_NOTE),
        world.create_item(itm.EN500),
        world.create_item(itm.WHITESTONE),
        world.create_item(itm.SCRAMASAX),
        world.create_item(itm.MEDICA_II),
        world.create_item(itm.EN200),
        # B1F Main: Event Moles Attack
        world.create_item(itm.NIGHT_10TP),
        world.create_item(itm.FIRST_CHAR_10HP),
        world.create_item(itm.EN100),
        # B1F Main: Event Venomflies Attack
        # B1F Main: D1 Chop
        # B1F Main: D3 Chop
        world.create_item(itm.NECTAR),
        world.create_item(itm.NECTAR_II),
        world.create_item(itm.GEM_STAFF),
        world.create_item(itm.PLUMED_HAT),
        world.create_item(itm.MEDICA_II),
        world.create_item(itm.RAPIER),
        world.create_item(itm.EN500),
        # No locations for these yet
        world.create_item(itm.CLEAR_KEY),
        world.create_item(itm.VIOLET_KEY),
        world.create_item(itm.FIRST_STRATUM_CLEARED),
    ]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool
