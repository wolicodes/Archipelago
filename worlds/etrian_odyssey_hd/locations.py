from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Location
from .data import items_constants as itm, locations_constants as loc, regions_constants as reg
from . import items, options

if TYPE_CHECKING:
    from .world import EOHDWorld


class EOHDLocation(Location):
    game = "Etrian Odyssey HD"

def get_region_locations(region_name: str, option: str = None) -> dict[str, int | None]:
    return {
        location_name: data["id"]
        for location_name, data in loc.LOCATION_DATA.items()
        if data["region"] == region_name
        and data.get("option") == option
        and data.get("event") is None
    }
    

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

    etria.add_locations(get_region_locations(reg.ETRIA), EOHDLocation)
    if world.options.shop_sanity:
        etria.add_locations(get_region_locations(reg.ETRIA, options.SHOP_SANITY), EOHDLocation)
    b1f_main.add_locations(get_region_locations(reg.B1F_MAIN), EOHDLocation)
    b1f_clear_crystal_room.add_locations(get_region_locations(reg.B1F_CLEAR_CRYSTAL_ROOM), EOHDLocation)
    b1f_violet_crystal_room.add_locations(get_region_locations(reg.B1F_VIOLET_CRYSTAL_ROOM), EOHDLocation)
    b1f_east.add_locations(get_region_locations(reg.B1F_EAST), EOHDLocation)


def create_events(world: EOHDWorld) -> None:
    # Gather all locations with an event, grouped by their region
    region_to_events: dict[str, list[tuple[str, str]]] = {}
    for location_name, data in loc.LOCATION_DATA.items():
        if data.get("event"):
            region_to_events.setdefault(data["region"], []).append(
                (location_name, data.get("event"))
            )
    # For each region, get the region object once and add all its events
    for region_name, events in region_to_events.items():
        region = world.get_region(region_name)
        for location_name, event in events:
            region.add_event(
                location_name, event, location_type=EOHDLocation, item_type=items.EOHDItem
            )
