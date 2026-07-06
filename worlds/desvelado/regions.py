from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import DesveladoWorld


def create_and_connect_regions(world: DesveladoWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: DesveladoWorld) -> None:
    map_screen = Region("Map Screen", world.player, world.multiworld)
    zone1_1 = Region("1-1", world.player, world.multiworld)
    zone1_2 = Region("1-2", world.player, world.multiworld)
    zone2_1 = Region("2-1", world.player, world.multiworld)
    zone2_2_room1_2 = Region("2-2 room 1-2", world.player, world.multiworld)
    zone2_2_room3_13 = Region("2-2 room 3-13", world.player, world.multiworld)  # single key
    zone2_2_room14_end = Region("2-2 14-end", world.player, world.multiworld)  # eyes
    zone2_3_room1_2 = Region("2-3 room 1-2", world.player, world.multiworld)
    zone2_3_room3 = Region("2-3 room 3", world.player, world.multiworld)  # double key
    zone2_3_room4 = Region("2-3 room 4", world.player, world.multiworld)  # eyes
    zone2_3_room5_end = Region("2-3 room 5-end", world.player, world.multiworld)  # single key
    zone3_1_room1_12 = Region("3-1 room 1-12", world.player, world.multiworld)
    zone3_1_room13_end = Region("3-1 room 13-end", world.player, world.multiworld)  # torch bulbs
    zone3_2_room1_2 = Region("3-2 room 1-2", world.player, world.multiworld)
    zone3_2_room3_5 = Region("3-2 room 3-5", world.player, world.multiworld)  # walls
    zone3_2_room6_end = Region("3-2 room 6-end", world.player, world.multiworld)  # torch bulbs
    zone3_3_room1 = Region("3-3 room 1", world.player, world.multiworld)
    zone3_3_room2_3 = Region("3-3 room 2-3", world.player, world.multiworld)  # single key/torch bulbs
    zone3_3_room4_12 = Region("3-3 room 4-12", world.player, world.multiworld)  # eyes/walls
    zone3_3_room13_end = Region("3-3 room 13-end", world.player, world.multiworld)  # double keys
    run_1 = Region("Run 1", world.player, world.multiworld)
    run_2 = Region("Run 2", world.player, world.multiworld)
    run_3 = Region("Run 3", world.player, world.multiworld)
    bonnie_room = Region("Bonnie Room", world.player, world.multiworld)

    regions = [
        map_screen,
        zone1_1,
        zone1_2,
        zone2_1,
        zone2_2_room1_2,
        zone2_2_room3_13,
        zone2_2_room14_end,
        zone2_3_room1_2,
        zone2_3_room3,
        zone2_3_room4,
        zone2_3_room5_end,
        zone3_1_room1_12,
        zone3_1_room13_end,
        zone3_2_room1_2,
        zone3_2_room3_5,
        zone3_2_room6_end,
        zone3_3_room1,
        zone3_3_room2_3,
        zone3_3_room4_12,
        zone3_3_room13_end,
        run_1,
        run_2,
        run_3,
        bonnie_room,
    ]

    world.multiworld.regions += regions


def connect_regions(world: DesveladoWorld) -> None:
    map_screen = world.get_region("Map Screen")
    zone1_1 = world.get_region("1-1")
    zone1_2 = world.get_region("1-2")
    zone2_1 = world.get_region("2-1")
    zone2_2_room1_2 = world.get_region("2-2 room 1-2")
    zone2_2_room3_13 = world.get_region("2-2 room 3-13")
    zone2_2_room14_end = world.get_region("2-2 14-end")
    zone2_3_room1_2 = world.get_region("2-3 room 1-2")
    zone2_3_room3 = world.get_region("2-3 room 3")
    zone2_3_room4 = world.get_region("2-3 room 4")
    zone2_3_room5_end = world.get_region("2-3 room 5-end")
    zone3_1_room1_12 = world.get_region("3-1 room 1-12")
    zone3_1_room13_end = world.get_region("3-1 room 13-end")
    zone3_2_room1_2 = world.get_region("3-2 room 1-2")
    zone3_2_room3_5 = world.get_region("3-2 room 3-5")
    zone3_2_room6_end = world.get_region("3-2 room 6-end")
    zone3_3_room1 = world.get_region("3-3 room 1")
    zone3_3_room2_3 = world.get_region("3-3 room 2-3")
    zone3_3_room4_12 = world.get_region("3-3 room 4-12")
    zone3_3_room13_end = world.get_region("3-3 room 13-end")
    run_1 = world.get_region("Run 1")
    run_2 = world.get_region("Run 2")
    run_3 = world.get_region("Run 3")
    bonnie_room = world.get_region("Bonnie Room")

    map_screen.connect(zone1_1, "Map Screen -> 1-1")
    map_screen.connect(zone1_2, "Map Screen -> 1-2")
    map_screen.connect(zone2_1, "Map Screen -> 2-1")

    map_screen.connect(zone2_2_room1_2, "Map Screen -> 2-2 room 1-2")
    zone2_2_room1_2.connect(zone2_2_room3_13, "2-2 room 1-2 -> 2-2 room 3-13")
    zone2_2_room3_13.connect(zone2_2_room14_end, "2-2 room 3-13 -> 2-2 room 14-end")

    map_screen.connect(zone2_3_room1_2, "Map Screen -> 2-3 room 1-2")
    zone2_3_room1_2.connect(zone2_3_room3, "2-3 room 1-2 -> 2-3 room 3")
    zone2_3_room3.connect(zone2_3_room4, "2-3 room 3 -> 2-3 room 4")
    zone2_3_room4.connect(zone2_3_room5_end, "2-3 room 4 -> 2-3 room 5-end")

    map_screen.connect(zone3_1_room1_12, "Map Screen -> 3-1 room 1-12")
    zone3_1_room1_12.connect(zone3_1_room13_end, "3-1 room 1-12 -> 3-1 room 13-end")

    map_screen.connect(zone3_2_room1_2, "Map Screen -> 3-2 room 1-2")
    zone3_2_room1_2.connect(zone3_2_room3_5, "3-2 room 1-2 -> 3-2 room 3-5")
    zone3_2_room3_5.connect(zone3_2_room6_end, "3-2 room 3-5 -> 3-2 room 6-end")

    map_screen.connect(zone3_3_room1, "Map Screen -> 3-3 room 1")
    zone3_3_room1.connect(zone3_3_room2_3, "3-3 room 1 -> 3-3 room 2-3")
    zone3_3_room2_3.connect(zone3_3_room4_12, "3-3 room 2-3 -> 3-3 room 4-12")
    zone3_3_room4_12.connect(zone3_3_room13_end, "3-3 room 4-12 -> 3-3 room 13-end")

    map_screen.connect(run_1, "Map Screen -> Run 1")
    map_screen.connect(run_2, "Map Screen -> Run 2")
    map_screen.connect(run_3, "Map Screen -> Run 3")
    run_3.connect(bonnie_room, "Run 3 -> Bonnie Room")
