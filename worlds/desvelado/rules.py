from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAll

if TYPE_CHECKING:
    from .world import DesveladoWorld

HAS_SINGLE_KEYS = Has("Single Keys")
HAS_DOUBLE_KEYS = Has("Double Keys")
HAS_LASER_EYES = Has("Laser Eyes")
HAS_DASH_WALLS = Has("Dash Walls")
HAS_GLASS_TORCHES = Has("Glass Torches")


def set_all_rules(world: DesveladoWorld) -> None:
    set_all_entrance_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: DesveladoWorld) -> None:
    zone2_2_single_keys = world.get_entrance("2-2 room 1-2 -> 2-2 room 3-13")
    zone2_2_laser_eyes = world.get_entrance("2-2 room 3-13 -> 2-2 room 14-end")

    zone2_3_double_keys = world.get_entrance("2-3 room 1-2 -> 2-3 room 3")
    zone2_3_laser_eyes = world.get_entrance("2-3 room 3 -> 2-3 room 4")
    zone2_3_single_keys = world.get_entrance("2-3 room 4 -> 2-3 room 5-end")

    zone3_1_glass_torches = world.get_entrance("3-1 room 1-12 -> 3-1 room 13-end")

    zone3_2_dash_walls = world.get_entrance("3-2 room 1-2 -> 3-2 room 3-5")
    zone3_2_glass_torches = world.get_entrance("3-2 room 3-5 -> 3-2 room 6-end")

    zone3_3_skey_glass = world.get_entrance("3-3 room 1 -> 3-3 room 2-3")
    zone3_3_eyes_walls = world.get_entrance("3-3 room 2-3 -> 3-3 room 4-12")
    zone3_3_double_keys = world.get_entrance("3-3 room 4-12 -> 3-3 room 13-end")

    victory = world.get_entrance("Run 3 -> Bonnie Room")

    world.set_rule(zone2_2_single_keys, HAS_SINGLE_KEYS)
    world.set_rule(zone2_2_laser_eyes, HAS_LASER_EYES)

    world.set_rule(zone2_3_double_keys, HAS_DOUBLE_KEYS)
    world.set_rule(zone2_3_laser_eyes, HAS_LASER_EYES)
    world.set_rule(zone2_3_single_keys, HAS_SINGLE_KEYS)

    world.set_rule(zone3_1_glass_torches, HAS_GLASS_TORCHES)

    world.set_rule(zone3_2_dash_walls, HAS_DASH_WALLS)
    world.set_rule(zone3_2_glass_torches, HAS_GLASS_TORCHES)

    world.set_rule(zone3_3_skey_glass, HAS_GLASS_TORCHES & HAS_SINGLE_KEYS)
    world.set_rule(zone3_3_eyes_walls, HAS_LASER_EYES & HAS_DASH_WALLS)
    world.set_rule(zone3_3_double_keys, HAS_DOUBLE_KEYS)

    goals = world.options.goal.value
    victory_rule = HAS_DASH_WALLS & HAS_GLASS_TORCHES & HAS_DOUBLE_KEYS
    if "complete_bonnie" in goals:
        victory_rule &= HasAll("Bonnie's Bone")
    if "map_clear" in goals:
        victory_rule &= (Has("Zone 1-1 Won")
            & Has("Zone 1-2 Won")
            & Has("Run 1 Won")
            & Has("Zone 2-1 Won")
            & Has("Zone 2-2 Won")
            & Has("Zone 2-3 Won")
            & Has("Run 2 Won")
            & Has("Zone 3-1 Won")
            & Has("Zone 3-2 Won")
            & Has("Zone 3-3 Won"))
    world.set_rule(victory, victory_rule)

def set_all_location_rules(world: DesveladoWorld) -> None:
    stage2_2_room9_bonus = world.get_location("2-2 Room 9 Bonus")
    stage2_3_room2_bonus = world.get_location("2-3 Room 2 Bonus")
    stage3_2_room8_bonus = world.get_location("3-2 Room 8 Bonus")
    stage3_3_room4_bonus = world.get_location("3-3 Room 4 Bonus")
    stage3_3_room8_bonus = world.get_location("3-3 Room 8 Bonus")
    run_2_map = world.get_location("Run 2 Map")
    
    world.set_rule(stage2_2_room9_bonus, HAS_DOUBLE_KEYS)
    world.set_rule(stage2_3_room2_bonus, HAS_SINGLE_KEYS)
    world.set_rule(stage3_2_room8_bonus, HAS_SINGLE_KEYS)
    world.set_rule(stage3_3_room4_bonus, HAS_DOUBLE_KEYS)
    world.set_rule(stage3_3_room8_bonus, HAS_DOUBLE_KEYS)
    world.set_rule(run_2_map, HAS_SINGLE_KEYS & HAS_LASER_EYES)


def set_completion_condition(world: DesveladoWorld) -> None:
    world.set_completion_rule(Has("Victory"))
