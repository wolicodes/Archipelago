from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import DesveladoWorld

LOCATION_NAME_TO_ID = {
    "Zone 1-1 Map": 1,
    "Zone 1-2 Map": 2,
    "Run 1 Map": 3,
    "Zone 2-1 Map": 4,
    "Zone 2-2 Map": 5,
    "Zone 2-3 Map": 6,
    "Run 2 Map": 7,
    "Zone 3-1 Map": 8,
    "Zone 3-2 Map": 9,
    "Zone 3-3 Map": 10,
    "1-1 Room 9 Bonus": 11,
    "1-1 Room 19 Bonus": 12,
    "1-1 Room 22 Bonus": 13,
    "1-2 Room 5 Bonus": 14,
    "1-2 Room 12 Bonus": 15,
    "2-1 Room 8 Bonus": 16,
    "2-2 Room 9 Bonus": 17,
    "2-2 Room 14 Bonus": 18,
    "2-3 Room 2 Bonus": 19,
    "2-3 Room 12 Bonus": 20,
    "3-1 Room 16 Bonus": 21,
    "3-2 Room 8 Bonus": 22,
    "3-2 Room 11 Bonus": 23,
    "3-3 Room 4 Bonus": 24,
    "3-3 Room 8 Bonus": 25,
}


class DesveladoLocation(Location):
    game = "Desvelado"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: DesveladoWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: DesveladoWorld) -> None:
    zone1_1 = world.get_region("1-1")
    zone1_2 = world.get_region("1-2")
    zone2_1 = world.get_region("2-1")
    zone2_2_room3_13 = world.get_region("2-2 room 3-13")
    zone2_2_room14_end = world.get_region("2-2 14-end")
    zone2_3_room1_2 = world.get_region("2-3 room 1-2")
    zone2_3_room5_end = world.get_region("2-3 room 5-end")
    zone3_1_room13_end = world.get_region("3-1 room 13-end")
    zone3_2_room6_end = world.get_region("3-2 room 6-end")
    zone3_3_room4_12 = world.get_region("3-3 room 4-12")
    zone3_3_room13_end = world.get_region("3-3 room 13-end")
    run_1 = world.get_region("Run 1")
    run_2 = world.get_region("Run 2")

    zone1_1.add_locations(get_location_names_with_ids(
        ["Zone 1-1 Map"]
    ), DesveladoLocation)

    zone1_2.add_locations(get_location_names_with_ids(
        ["Zone 1-2 Map"]
    ), DesveladoLocation)

    zone2_1.add_locations(get_location_names_with_ids(
        ["Zone 2-1 Map"]
    ), DesveladoLocation)

    zone2_2_room14_end.add_locations(get_location_names_with_ids(
        ["Zone 2-2 Map"]
    ), DesveladoLocation)

    zone2_3_room5_end.add_locations(get_location_names_with_ids(
        ["Zone 2-3 Map"]
    ), DesveladoLocation)

    zone3_1_room13_end.add_locations(get_location_names_with_ids(
        ["Zone 3-1 Map"]
    ), DesveladoLocation)

    zone3_2_room6_end.add_locations(get_location_names_with_ids(
        ["Zone 3-2 Map"]
    ), DesveladoLocation)

    zone3_3_room13_end.add_locations(get_location_names_with_ids(
        ["Zone 3-3 Map"]
    ), DesveladoLocation)

    run_1.add_locations(get_location_names_with_ids(
        ["Run 1 Map"]
    ), DesveladoLocation)

    run_2.add_locations(get_location_names_with_ids(
        ["Run 2 Map"]
    ), DesveladoLocation)

    if world.options.shuffle_bonnies_bones:
        zone1_1.add_locations(get_location_names_with_ids(
            ["1-1 Room 9 Bonus", "1-1 Room 19 Bonus", "1-1 Room 22 Bonus"]
        ), DesveladoLocation)
        zone1_2.add_locations(get_location_names_with_ids(
            ["1-2 Room 5 Bonus", "1-2 Room 12 Bonus"]
        ), DesveladoLocation)
        zone2_1.add_locations(get_location_names_with_ids(
            ["2-1 Room 8 Bonus"]
        ), DesveladoLocation)
        zone2_2_room3_13.add_locations(get_location_names_with_ids(
            ["2-2 Room 9 Bonus"]
        ), DesveladoLocation)
        zone2_2_room14_end.add_locations(get_location_names_with_ids(
            ["2-2 Room 14 Bonus"]
        ), DesveladoLocation)
        zone2_3_room1_2.add_locations(get_location_names_with_ids(
            ["2-3 Room 2 Bonus"]
        ), DesveladoLocation)
        zone2_3_room5_end.add_locations(get_location_names_with_ids(
            ["2-3 Room 12 Bonus"]
        ), DesveladoLocation)
        zone3_1_room13_end.add_locations(get_location_names_with_ids(
            ["3-1 Room 16 Bonus"]
        ), DesveladoLocation)
        zone3_2_room6_end.add_locations(get_location_names_with_ids(
            ["3-2 Room 8 Bonus", "3-2 Room 11 Bonus"]
        ), DesveladoLocation)
        zone3_3_room4_12.add_locations(get_location_names_with_ids(
            ["3-3 Room 4 Bonus", "3-3 Room 8 Bonus"]
        ), DesveladoLocation)


def create_events(world: DesveladoWorld) -> None:
    zone1_1 = world.get_region("1-1")
    zone1_2 = world.get_region("1-2")
    run_1 = world.get_region("Run 1")

    zone2_1 = world.get_region("2-1")
    zone2_2_room14_end = world.get_region("2-2 14-end")
    zone2_3_room5_end = world.get_region("2-3 room 5-end")
    run_2 = world.get_region("Run 2")

    zone3_1_room13_end = world.get_region("3-1 room 13-end")
    zone3_2_room6_end = world.get_region("3-2 room 6-end")
    zone3_3_room13_end = world.get_region("3-3 room 13-end")

    bonnie_room = world.get_region("Bonnie Room")

    zone1_1.add_event("Zone 1-1 Cleared", "Zone 1-1 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    zone1_2.add_event("Zone 1-2 Cleared", "Zone 1-2 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    run_1.add_event("Run 1 Cleared", "Run 1 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    zone2_1.add_event("Zone 2-1 Cleared", "Zone 2-1 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    zone2_2_room14_end.add_event("Zone 2-2 Cleared", "Zone 2-2 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    zone2_3_room5_end.add_event("Zone 2-3 Cleared", "Zone 2-3 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    run_2.add_event("Run 2 Cleared", "Run 2 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    zone3_1_room13_end.add_event("Zone 3-1 Cleared", "Zone 3-1 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    zone3_2_room6_end.add_event("Zone 3-2 Cleared", "Zone 3-2 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)
    zone3_3_room13_end.add_event("Zone 3-3 Cleared", "Zone 3-3 Won", location_type=DesveladoLocation, item_type=items.DesveladoItem)

    bonnie_room.add_event(
        "Reach Bonnie Room", "Victory", location_type=DesveladoLocation, item_type=items.DesveladoItem
    )
