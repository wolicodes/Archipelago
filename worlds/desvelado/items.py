from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import DesveladoWorld

ITEM_NAME_TO_ID = {
    "Single Keys": 1,
    "Double Keys": 2,
    "Laser Eyes": 3,
    "Dash Walls": 4,
    "Glass Torches": 5,
    "Bonnie's Bone": 6,
    "Meow": 7,
    "Onwards to bed!": 8,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Single Keys": ItemClassification.progression | ItemClassification.useful,
    "Double Keys": ItemClassification.progression | ItemClassification.useful,
    "Laser Eyes": ItemClassification.progression | ItemClassification.useful,
    "Dash Walls": ItemClassification.progression | ItemClassification.useful,
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

    if name == "Bonnie's Bone" and world.options.goal.current_key == "complete_bonnie":
        classification = ItemClassification.progression_deprioritized_skip_balancing

    return DesveladoItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: DesveladoWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Single Keys"),
        world.create_item("Double Keys"),
        world.create_item("Laser Eyes"),
        world.create_item("Dash Walls"),
        world.create_item("Glass Torches"),
    ]

    for i in range(15):
        itempool.append(
            world.create_item("Bonnie's Bone")
        )

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

