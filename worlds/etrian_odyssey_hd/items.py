from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item
from .data import items_constants as itm, locations_constants as loc
from . import locations
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
    itempool: list[Item] = []

    all_locs = locations.get_all_locations()
    for name in all_locs:
        data = loc.LOCATION_DATA[name]
        if data.item:
            itempool.append(world.create_item(data.item))
    
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool
