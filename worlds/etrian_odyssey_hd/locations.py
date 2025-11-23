from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Location
from worlds.etrian_odyssey_hd.data.Items import Items
from .data.Locations import ETRIA_LOCATIONS, B1F_MAIN_LOCATIONS, LOCATION_NAME_TO_ID, Locations
from .data.Regions import Regions
from . import items

if TYPE_CHECKING:
    from .world import EOHDWorld


class EOHDLocation(Location):
    game = "Etrian Odyssey HD"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: EOHDWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: EOHDWorld) -> None:
    etria = world.get_region(Regions.ETRIA.value)
    b1f_main = world.get_region(Regions.B1F_MAIN.value)
    b1f_clear_crystal_room = world.get_region(Regions.B1F_CLEAR_CRYSTAL_ROOM.value)
    b1f_violet_crystal_room = world.get_region(Regions.B1F_VIOLET_CRYSTAL_ROOM.value)
    b1f_east = world.get_region(Regions.B1F_EAST.value)
    # b2f = world.get_region(Regions.B2F_MAIN.value)

    etria.add_locations(get_location_names_with_ids(ETRIA_LOCATIONS), EOHDLocation)
    b1f_main.add_locations(get_location_names_with_ids(B1F_MAIN_LOCATIONS), EOHDLocation)
    b1f_clear_crystal_room.add_locations(get_location_names_with_ids([Locations.B1F_CLEAR_CRYSTAL_ROOM_CHEST.value]), EOHDLocation)
    b1f_violet_crystal_room.add_locations(get_location_names_with_ids([Locations.B1F_VIOLET_CRYSTAL_ROOM_TOP_CHEST.value, Locations.B1F_VIOLET_CRYSTAL_ROOM_BOTTOM_CHEST.value]), EOHDLocation)
    b1f_east.add_locations(get_location_names_with_ids([Locations.B1F_EAST_NORTH_CHEST.value, Locations.B1F_EAST_RAGELOPE_TOP_CHEST.value, Locations.B1F_EAST_RAGELOPE_MIDDLE_CHEST.value, Locations.B1F_EAST_RAGELOPE_BOTTOM_CHEST.value]), EOHDLocation)


def create_events(world: EOHDWorld) -> None:
    etria = world.get_region(Regions.ETRIA.value)
    etria.add_event(
        Locations.ADVENTURERS_INITIATION_COMPLETE.value, Items.VICTORY.value, location_type=EOHDLocation, item_type=items.EOHDItem
    )
