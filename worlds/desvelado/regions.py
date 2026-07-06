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
    stage1_1 = Region("1-1", world.player, world.multiworld)
    stage1_2 = Region("1-2", world.player, world.multiworld)
    stage2_1 = Region("2-1", world.player, world.multiworld)
    stage2_2_room1_2 = Region("2-2 room 1-2", world.player, world.multiworld)
    stage2_2_room3_13 = Region("2-2 room 3-13", world.player, world.multiworld)  # single key
    stage2_2_room14_end = Region("2-2 14-end", world.player, world.multiworld)  # eyes
    stage2_3_room1_2 = Region("2-3 room 1-2", world.player, world.multiworld)
    stage2_3_room3 = Region("2-3 room 3", world.player, world.multiworld)  # double key
    stage2_3_room4 = Region("2-3 room 4", world.player, world.multiworld)  # eyes
    stage2_3_room5_end = Region("2-3 room 5-end", world.player, world.multiworld)  # single key
    stage3_1_room1_12 = Region("3-1 room 1-12", world.player, world.multiworld)
    stage3_1_room13_end = Region("3-1 room 13-end", world.player, world.multiworld)  # torch bulbs
    stage3_2_room1_2 = Region("3-2 room 1-2", world.player, world.multiworld)
    stage3_2_room3_5 = Region("3-2 room 3-5", world.player, world.multiworld)  # walls
    stage3_2_room6_end = Region("3-2 room 6-end", world.player, world.multiworld)  # torch bulbs
    stage3_3_room1 = Region("3-3 room 1", world.player, world.multiworld)
    stage3_3_room2_3 = Region("3-3 room 2-3", world.player, world.multiworld)  # single key/torch bulbs
    stage3_3_room4_12 = Region("3-3 room 4-12", world.player, world.multiworld)  # eyes/walls
    stage3_3_room13_end = Region("3-3 room 13-end", world.player, world.multiworld)  # double keys
    run_1 = Region("Boss Level 1", world.player, world.multiworld)
    run_2 = Region("Boss Level 2", world.player, world.multiworld)
    run_3 = Region("Boss Level 3", world.player, world.multiworld)
    bonnie_room = Region("Bonnie Room", world.player, world.multiworld)

    regions = [
        map_screen,
        stage1_1,
        stage1_2,
        stage2_1,
        stage2_2_room1_2,
        stage2_2_room3_13,
        stage2_2_room14_end,
        stage2_3_room1_2,
        stage2_3_room3,
        stage2_3_room4,
        stage2_3_room5_end,
        stage3_1_room1_12,
        stage3_1_room13_end,
        stage3_2_room1_2,
        stage3_2_room3_5,
        stage3_2_room6_end,
        stage3_3_room1,
        stage3_3_room2_3,
        stage3_3_room4_12,
        stage3_3_room13_end,
        run_1,
        run_2,
        run_3,
        bonnie_room,
    ]

    world.multiworld.regions += regions


def connect_regions(world: DesveladoWorld) -> None:
    map_screen = world.get_region("Map Screen")
    stage1_1 = world.get_region("1-1")
    stage1_2 = world.get_region("1-2")
    stage2_1 = world.get_region("2-1")
    stage2_2_room1_2 = world.get_region("2-2 room 1-2")
    stage2_2_room3_13 = world.get_region("2-2 room 3-13")
    stage2_2_room14_end = world.get_region("2-2 14-end")
    stage2_3_room1_2 = world.get_region("2-3 room 1-2")
    stage2_3_room3 = world.get_region("2-3 room 3")
    stage2_3_room4 = world.get_region("2-3 room 4")
    stage2_3_room5_end = world.get_region("2-3 room 5-end")
    stage3_1_room1_12 = world.get_region("3-1 room 1-12")
    stage3_1_room13_end = world.get_region("3-1 room 13-end")
    stage3_2_room1_2 = world.get_region("3-2 room 1-2")
    stage3_2_room3_5 = world.get_region("3-2 room 3-5")
    stage3_2_room6_end = world.get_region("3-2 room 6-end")
    stage3_3_room1 = world.get_region("3-3 room 1")
    stage3_3_room2_3 = world.get_region("3-3 room 2-3")
    stage3_3_room4_12 = world.get_region("3-3 room 4-12")
    stage3_3_room13_end = world.get_region("3-3 room 13-end")
    run_1 = world.get_region("Boss Level 1")
    run_2 = world.get_region("Boss Level 2")
    run_3 = world.get_region("Boss Level 3")
    bonnie_room = world.get_region("Bonnie Room")

    map_screen.connect(stage1_1, "Map Screen -> 1-1")
    map_screen.connect(stage1_2, "Map Screen -> 1-2")
    map_screen.connect(stage2_1, "Map Screen -> 2-1")

    map_screen.connect(stage2_2_room1_2, "Map Screen -> 2-2 room 1-2")
    stage2_2_room1_2.connect(stage2_2_room3_13, "2-2 room 1-2 -> 2-2 room 3-13")
    stage2_2_room3_13.connect(stage2_2_room14_end, "2-2 room 3-13 -> 2-2 room 14-end")

    map_screen.connect(stage2_3_room1_2, "Map Screen -> 2-3 room 1-2")
    stage2_3_room1_2.connect(stage2_3_room3, "2-3 room 1-2 -> 2-3 room 3")
    stage2_3_room3.connect(stage2_3_room4, "2-3 room 3 -> 2-3 room 4")
    stage2_3_room4.connect(stage2_3_room5_end, "2-3 room 4 -> 2-3 room 5-end")

    map_screen.connect(stage3_1_room1_12, "Map Screen -> 3-1 room 1-12")
    stage3_1_room1_12.connect(stage3_1_room13_end, "3-1 room 1-12 -> 3-1 room 13-end")

    map_screen.connect(stage3_2_room1_2, "Map Screen -> 3-2 room 1-2")
    stage3_2_room1_2.connect(stage3_2_room3_5, "3-2 room 1-2 -> 3-2 room 3-5")
    stage3_2_room3_5.connect(stage3_2_room6_end, "3-2 room 3-5 -> 3-2 room 6-end")

    map_screen.connect(stage3_3_room1, "Map Screen -> 3-3 room 1")
    stage3_3_room1.connect(stage3_3_room2_3, "3-3 room 1 -> 3-3 room 2-3")
    stage3_3_room2_3.connect(stage3_3_room4_12, "3-3 room 2-3 -> 3-3 room 4-12")
    stage3_3_room4_12.connect(stage3_3_room13_end, "3-3 room 4-12 -> 3-3 room 13-end")

    map_screen.connect(run_1, "Map Screen -> Boss Level 1")
    map_screen.connect(run_2, "Map Screen -> Boss Level 2")
    map_screen.connect(run_3, "Map Screen -> Boss Level 3")
    run_3.connect(bonnie_room, "Boss Level 3 -> Bonnie Room")
