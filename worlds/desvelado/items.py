from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import DesveladoWorld

ITEM_NAME_TO_ID = {
    "Single Keys": 1,
    "Double Keys": 2,
    "Ghost Switches": 3,
    "Ghost Walls": 4,
    "Glass Torches": 5,
    "Bonnie's Bone": 6,
    "Meow": 7,
    "Onwards to bed!": 8,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Single Keys": ItemClassification.progression | ItemClassification.useful,
    "Double Keys": ItemClassification.progression | ItemClassification.useful,
    "Ghost Switches": ItemClassification.progression | ItemClassification.useful,
    "Ghost Walls": ItemClassification.progression | ItemClassification.useful,
    "Glass Torches": ItemClassification.progression | ItemClassification.useful,
    "Bonnie's Bone": ItemClassification.filler,
    "Meow": ItemClassification.filler,
    "Onwards to bed!": ItemClassification.filler,
}


class DesveladoItem(Item):
    game = "Desvelado"


def get_random_filler_item_name(world: DesveladoWorld) -> str:
    if world.random.randint(0, 99) < 90:
        return "Meow"
    return "Onwards to bed!"


def create_item_with_correct_classification(world: DesveladoWorld, name: str) -> DesveladoItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    if name == "Bonnie's Bone" and "complete_bonnie" in world.options.goal.value:
        classification = ItemClassification.progression_deprioritized_skip_balancing

    return DesveladoItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: DesveladoWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Single Keys"),
        world.create_item("Double Keys"),
        world.create_item("Ghost Switches"),
        world.create_item("Ghost Walls"),
        world.create_item("Glass Torches"),
    ]

    if world.options.shuffle_bonnies_bones:
        for i in range(15):
            itempool.append(
                world.create_item("Bonnie's Bone")
            )
    else:
        bonus_locations = [
            "1-1 Room 09 Bonus", "1-1 Room 19 Bonus", "1-1 Room 22 Bonus",
            "1-2 Room 05 Bonus", "1-2 Room 12 Bonus",
            "2-1 Room 08 Bonus",
            "2-2 Room 09 Bonus", "2-2 Room 14 Bonus",
            "2-3 Room 02 Bonus", "2-3 Room 12 Bonus",
            "3-1 Room 16 Bonus",
            "3-2 Room 08 Bonus", "3-2 Room 11 Bonus",
            "3-3 Room 04 Bonus", "3-3 Room 08 Bonus",
        ]
        for location_name in bonus_locations:
            world.get_location(location_name).place_locked_item(world.create_item("Bonnie's Bone"))

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

