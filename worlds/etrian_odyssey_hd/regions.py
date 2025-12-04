from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region
from .data import regions_constants as reg, items_constants as itm, entrances_constants as ent

if TYPE_CHECKING:
    from .world import EOHDWorld


def create_and_connect_regions(world: EOHDWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: EOHDWorld) -> None:
    regions = [
        Region(region_name, world.player, world.multiworld)
        for region_name in reg.ALL_REGIONS
    ]
    world.multiworld.regions += regions


def connect_regions(world: EOHDWorld) -> None:
    etria = world.get_region(reg.ETRIA)
    b1f = world.get_region(reg.B1F_MAIN)
    b1f_clear_crystal_room = world.get_region(reg.B1F_CLEAR_CRYSTAL_ROOM)
    b1f_violet_crystal_room = world.get_region(reg.B1F_VIOLET_CRYSTAL_ROOM)
    b1f_east = world.get_region(reg.B1F_EAST)
    b2f_main = world.get_region(reg.B2F_MAIN)
    b2f_south = world.get_region(reg.B2F_SOUTH)

    etria.connect(b1f, ent.ENTER_THE_LABYRINTH)
    b1f.connect(b1f_clear_crystal_room, ent.B1F_CLEAR_CRYSTAL_ROOM_ACCESS,
                lambda state: state.has(itm.CLEAR_KEY, world.player))
    b1f.connect(b1f_violet_crystal_room, ent.B1F_VIOLET_CRYSTAL_ROOM_ACCESS,
                lambda state: state.has(itm.VIOLET_KEY, world.player))
    b1f.connect(b1f_east, ent.B1F_EAST_ACCESS, lambda state: state.has(itm.FIRST_STRATUM_CLEARED, world.player))
    b1f.connect(b2f_main, ent.B2F_ACCESS)
    b2f_main.connect(b2f_south, ent.B2F_SOUTH_ACCESS, lambda state: state.has(itm.CLEAR_KEY, world.player))
