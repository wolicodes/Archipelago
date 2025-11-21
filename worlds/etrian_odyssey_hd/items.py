from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item
from worlds.etrian_odyssey_hd.data.Items import DEFAULT_ITEM_CLASSIFICATIONS, ITEM_NAME_TO_ID, Items

if TYPE_CHECKING:
    from .world import EOHDWorld


class EOHDItem(Item):
    game = "Etrian Odyssey HD"


def get_random_filler_item_name(world: EOHDWorld) -> str:
    if world.random.randint(0, 100) == 1:
        return Items.EN1
    if world.random.randint(0, 100) <= 50:
        return Items.EN50
    return Items.EN100

def create_item_with_correct_classification(world: EOHDWorld, name: str) -> EOHDItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return EOHDItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: EOHDWorld) -> None:
    itempool: list[Item] = [
        world.create_item(Items.AXCELA),
        world.create_item(Items.AMRITA),
        world.create_item(Items.MEDICA),
        world.create_item(Items.MEDICA_II),
        world.create_item(Items.NECTAR),
        world.create_item(Items.NECTAR_II),
        world.create_item(Items.SCRAMASAX),
        world.create_item(Items.KNIFE),
        world.create_item(Items.STAFF),
        world.create_item(Items.WAND),
        world.create_item(Items.HATCHET),
        world.create_item(Items.WOOD_BOW),
        world.create_item(Items.LIGHT_WHIP),
        world.create_item(Items.TWEED),
        world.create_item(Items.TARGE),
        world.create_item(Items.HAIRPIN),
        world.create_item(Items.KNIT_GLOVE),
        world.create_item(Items.LEAF_BOOT),
        world.create_item(Items.HIDE_BELT),
        world.create_item(Items.WARD_CHIME),
        world.create_item(Items.ARIADNE_THREAD),
        world.create_item(Items.WHITESTONE),
        world.create_item(Items.GEM_STAFF),
        world.create_item(Items.PLUMED_HAT),
        world.create_item(Items.RAPIER),
        world.create_item(Items.CLEAR_KEY),
        world.create_item(Items.VIOLET_KEY),
        world.create_item(Items.FIRST_STRATUM_CLEARED),
        world.create_item(Items.RADHA_NOTE),
        world.create_item(Items.VICTORY),
        world.create_item(Items.EN500),
        world.create_item(Items.EN200),
        world.create_item(Items.EN100),
        world.create_item(Items.NIGHT_10TP),
        world.create_item(Items.FIRST_CHAR_10HP),
        world.create_item(Items.EN50),
        world.create_item(Items.EN1),
    ]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool
