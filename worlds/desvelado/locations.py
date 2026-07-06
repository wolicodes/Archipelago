from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import DesveladoWorld

LOCATION_NAME_TO_ID = {
    "1-1 Map": 1,
    "1-2 Map": 2,
    "Boss Level 1 Map": 3,
    "2-1 Map": 4,
    "2-2 Map": 5,
    "2-3 Map": 6,
    "Boss Level 2 Map": 7,
    "3-1 Map": 8,
    "3-2 Map": 9,
    "3-3 Map": 10,
    "1-1 Room 09 Bonus": 11,
    "1-1 Room 19 Bonus": 12,
    "1-1 Room 22 Bonus": 13,
    "1-2 Room 05 Bonus": 14,
    "1-2 Room 12 Bonus": 15,
    "2-1 Room 08 Bonus": 16,
    "2-2 Room 09 Bonus": 17,
    "2-2 Room 14 Bonus": 18,
    "2-3 Room 02 Bonus": 19,
    "2-3 Room 12 Bonus": 20,
    "3-1 Room 16 Bonus": 21,
    "3-2 Room 08 Bonus": 22,
    "3-2 Room 11 Bonus": 23,
    "3-3 Room 04 Bonus": 24,
    "3-3 Room 08 Bonus": 25,
}


class DesveladoLocation(Location):
    game = "Desvelado"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: DesveladoWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: DesveladoWorld) -> None:
    stage1_1 = world.get_region("1-1")
    stage1_2 = world.get_region("1-2")
    stage2_1 = world.get_region("2-1")
    stage2_2_room3_13 = world.get_region("2-2 room 3-13")
    stage2_2_room14_end = world.get_region("2-2 14-end")
    stage2_3_room1_2 = world.get_region("2-3 room 1-2")
    stage2_3_room5_end = world.get_region("2-3 room 5-end")
    stage3_1_room13_end = world.get_region("3-1 room 13-end")
    stage3_2_room6_end = world.get_region("3-2 room 6-end")
    stage3_3_room4_12 = world.get_region("3-3 room 4-12")
    stage3_3_room13_end = world.get_region("3-3 room 13-end")
    run_1 = world.get_region("Boss Level 1")
    run_2 = world.get_region("Boss Level 2")

    stage1_1.add_locations(get_location_names_with_ids(
        ["1-1 Map", "1-1 Room 09 Bonus", "1-1 Room 19 Bonus", "1-1 Room 22 Bonus"]
    ), DesveladoLocation)

    stage1_2.add_locations(get_location_names_with_ids(
        ["1-2 Map", "1-2 Room 05 Bonus", "1-2 Room 12 Bonus"]
    ), DesveladoLocation)

    stage2_1.add_locations(get_location_names_with_ids(
        ["2-1 Map", "2-1 Room 08 Bonus"]
    ), DesveladoLocation)

    stage2_2_room3_13.add_locations(get_location_names_with_ids(
        ["2-2 Room 09 Bonus"]
    ), DesveladoLocation)

    stage2_2_room14_end.add_locations(get_location_names_with_ids(
        ["2-2 Map", "2-2 Room 14 Bonus"]
    ), DesveladoLocation)

    stage2_3_room1_2.add_locations(get_location_names_with_ids(
        ["2-3 Room 02 Bonus"]
    ), DesveladoLocation)

    stage2_3_room5_end.add_locations(get_location_names_with_ids(
        ["2-3 Map", "2-3 Room 12 Bonus"]
    ), DesveladoLocation)

    stage3_1_room13_end.add_locations(get_location_names_with_ids(
        ["3-1 Map", "3-1 Room 16 Bonus"]
    ), DesveladoLocation)

    stage3_2_room6_end.add_locations(get_location_names_with_ids(
        ["3-2 Map", "3-2 Room 08 Bonus", "3-2 Room 11 Bonus"]
    ), DesveladoLocation)

    stage3_3_room4_12.add_locations(get_location_names_with_ids(
        ["3-3 Room 04 Bonus", "3-3 Room 08 Bonus"]
    ), DesveladoLocation)

    stage3_3_room13_end.add_locations(get_location_names_with_ids(
        ["3-3 Map"]
    ), DesveladoLocation)

    run_1.add_locations(get_location_names_with_ids(
        ["Boss Level 1 Map"]
    ), DesveladoLocation)

    run_2.add_locations(get_location_names_with_ids(
        ["Boss Level 2 Map"]
    ), DesveladoLocation)


def create_events(world: DesveladoWorld) -> None:
    stage1_1 = world.get_region("1-1")
    stage1_2 = world.get_region("1-2")
    run_1 = world.get_region("Boss Level 1")

    stage2_1 = world.get_region("2-1")
    stage2_2_room14_end = world.get_region("2-2 14-end")
    stage2_3_room5_end = world.get_region("2-3 room 5-end")
    run_2 = world.get_region("Boss Level 2")

    stage3_1_room13_end = world.get_region("3-1 room 13-end")
    stage3_2_room6_end = world.get_region("3-2 room 6-end")
    stage3_3_room13_end = world.get_region("3-3 room 13-end")

    bonnie_room = world.get_region("Bonnie Room")

    stage1_1.add_event("1-1 Cleared", "1-1 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    stage1_2.add_event("1-2 Cleared", "1-2 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    run_1.add_event("Boss Level 1 Cleared", "Boss Level 1 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    stage2_1.add_event("2-1 Cleared", "2-1 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    stage2_2_room14_end.add_event("2-2 Cleared", "2-2 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    stage2_3_room5_end.add_event("2-3 Cleared", "2-3 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    run_2.add_event("Boss Level 2 Cleared", "Boss Level 2 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    stage3_1_room13_end.add_event("3-1 Cleared", "3-1 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    stage3_2_room6_end.add_event("3-2 Cleared", "3-2 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    stage3_3_room13_end.add_event("3-3 Cleared", "3-3 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)

    bonnie_room.add_event(
        "Reach Bonnie Room", "Victory", location_type=DesveladoLocation, item_type=items.DesveladoItem
    )
