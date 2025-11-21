from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region
from .data.Regions import Regions, Entrances
from .data.Items import Items

if TYPE_CHECKING:
    from .world import EOHDWorld


def create_and_connect_regions(world: EOHDWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: EOHDWorld) -> None:
    etria = Region(Regions.ETRIA, world.player, world.multiworld)
    b1f_main = Region(Regions.B1F_MAIN, world.player, world.multiworld)
    b1f_clear_crystal_room = Region(Regions.B1F_CLEAR_CRYSTAL_ROOM, world.player, world.multiworld)
    b1f_violet_crystal_room = Region(Regions.B1F_VIOLET_CRYSTAL_ROOM, world.player, world.multiworld)
    b1f_east = Region(Regions.B1F_EAST, world.player, world.multiworld)
    b2f = Region(Regions.B2F_MAIN, world.player, world.multiworld)

    regions = [etria, b1f_main, b1f_clear_crystal_room, b1f_violet_crystal_room, b1f_east, b2f]
    world.multiworld.regions += regions


def connect_regions(world: EOHDWorld) -> None:
    etria = world.get_region(Regions.ETRIA)
    b1f = world.get_region(Regions.B1F_MAIN)
    b1f_clear_crystal_room = world.get_region(Regions.B1F_CLEAR_CRYSTAL_ROOM)
    b1f_violet_crystal_room = world.get_region(Regions.B1F_VIOLET_CRYSTAL_ROOM)
    b1f_east = world.get_region(Regions.B1F_EAST)
    b2f = world.get_region(Regions.B2F_MAIN)

    etria.connect(b1f, Entrances.ENTER_THE_LABYRINTH)

    b1f.connect(b1f_clear_crystal_room, Entrances.B1F_CLEAR_CRYSTAL_ROOM_ACCESS, lambda state: state.has(Items.CLEAR_KEY, world.player))
    b1f.connect(b1f_violet_crystal_room, Entrances.B1F_VIOLET_CRYSTAL_ROOM_ACCESS, lambda state: state.has(Items.VIOLET_KEY, world.player))
    b1f.connect(b1f_east, Entrances.B1F_EAST_ACCESS, lambda state: state.has(Items.FIRST_STRATUM_CLEARED, world.player))
    b1f.connect(b2f, Entrances.B2F_ACCESS, lambda state: state.has(Items.RADHA_NOTE, world.player))
