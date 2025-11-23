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
    etria = Region(Regions.ETRIA.value, world.player, world.multiworld)
    b1f_main = Region(Regions.B1F_MAIN.value, world.player, world.multiworld)
    b1f_clear_crystal_room = Region(Regions.B1F_CLEAR_CRYSTAL_ROOM.value, world.player, world.multiworld)
    b1f_violet_crystal_room = Region(Regions.B1F_VIOLET_CRYSTAL_ROOM.value, world.player, world.multiworld)
    b1f_east = Region(Regions.B1F_EAST.value, world.player, world.multiworld)
    b2f = Region(Regions.B2F_MAIN.value, world.player, world.multiworld)

    regions = [etria, b1f_main, b1f_clear_crystal_room, b1f_violet_crystal_room, b1f_east, b2f]
    world.multiworld.regions += regions


def connect_regions(world: EOHDWorld) -> None:
    etria = world.get_region(Regions.ETRIA.value)
    b1f = world.get_region(Regions.B1F_MAIN.value)
    b1f_clear_crystal_room = world.get_region(Regions.B1F_CLEAR_CRYSTAL_ROOM.value)
    b1f_violet_crystal_room = world.get_region(Regions.B1F_VIOLET_CRYSTAL_ROOM.value)
    b1f_east = world.get_region(Regions.B1F_EAST.value)
    b2f = world.get_region(Regions.B2F_MAIN.value)

    etria.connect(b1f, Entrances.ENTER_THE_LABYRINTH.value)

    b1f.connect(b1f_clear_crystal_room, Entrances.B1F_CLEAR_CRYSTAL_ROOM_ACCESS.value, lambda state: state.has(Items.CLEAR_KEY.value, world.player))
    b1f.connect(b1f_violet_crystal_room, Entrances.B1F_VIOLET_CRYSTAL_ROOM_ACCESS.value, lambda state: state.has(Items.VIOLET_KEY.value, world.player))
    b1f.connect(b1f_east, Entrances.B1F_EAST_ACCESS.value, lambda state: state.has(Items.FIRST_STRATUM_CLEARED.value, world.player))
    b1f.connect(b2f, Entrances.B2F_ACCESS.value, lambda state: state.has(Items.RADHA_NOTE.value, world.player))
