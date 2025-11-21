from __future__ import annotations

from typing import TYPE_CHECKING

from worlds.etrian_odyssey_hd.data.Items import Items
from worlds.etrian_odyssey_hd.data.Regions import Entrances
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from .world import EOHDWorld


def set_all_rules(world: EOHDWorld) -> None:
    set_all_entrance_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: EOHDWorld) -> None:
    b1f_clear_crystal_room_access = world.get_entrance(Entrances.B1F_CLEAR_CRYSTAL_ROOM_ACCESS)
    b1f_violet_crystal_room_access = world.get_entrance(Entrances.B1F_VIOLET_CRYSTAL_ROOM_ACCESS)
    b1f_east_access = world.get_entrance(Entrances.B1F_EAST_ACCESS)
    b2f_access = world.get_entrance(Entrances.B2F_ACCESS)

    set_rule(b1f_clear_crystal_room_access, lambda state: state.has(Items.CLEAR_KEY, world.player))
    set_rule(b1f_violet_crystal_room_access, lambda state: state.has(Items.VIOLET_KEY, world.player))
    set_rule(b1f_east_access, lambda state: state.has(Items.FIRST_STRATUM_CLEARED, world.player))
    set_rule(b2f_access, lambda state: state.has(Items.RADHA_NOTE, world.player))


def set_completion_condition(world: EOHDWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has(Items.VICTORY, world.player)
