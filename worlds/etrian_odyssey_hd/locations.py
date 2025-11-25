from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Location
from .data import items_constants as itm, locations_constants as loc, regions_constants as reg
from . import items

if TYPE_CHECKING:
    from .world import EOHDWorld


class EOHDLocation(Location):
    game = "Etrian Odyssey HD"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: loc.LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: EOHDWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: EOHDWorld) -> None:
    etria = world.get_region(reg.ETRIA)
    b1f_main = world.get_region(reg.B1F_MAIN)
    b1f_clear_crystal_room = world.get_region(reg.B1F_CLEAR_CRYSTAL_ROOM)
    b1f_violet_crystal_room = world.get_region(reg.B1F_VIOLET_CRYSTAL_ROOM)
    b1f_east = world.get_region(reg.B1F_EAST)
    # b2f = world.get_region(reg.B2F_MAIN)

    etria.add_locations(get_location_names_with_ids(loc.ETRIA_LOCATIONS), EOHDLocation)
    b1f_main.add_locations(get_location_names_with_ids(loc.B1F_MAIN_LOCATIONS), EOHDLocation)
    b1f_clear_crystal_room.add_locations(get_location_names_with_ids([loc.B1F_CLEAR_CRYSTAL_ROOM_CHEST]), EOHDLocation)
    b1f_violet_crystal_room.add_locations(get_location_names_with_ids(loc.B1F_VIOLET_CRYSTAL_ROOM_LOCATIONS), EOHDLocation)
    b1f_east.add_locations(get_location_names_with_ids(loc.B1F_EAST_LOCATIONS), EOHDLocation)


def create_events(world: EOHDWorld) -> None:
    etria = world.get_region(reg.ETRIA)
    etria.add_event(
        loc.ADVENTURERS_INITIATION_COMPLETE, itm.VICTORY, location_type=EOHDLocation, item_type=items.EOHDItem
    )
