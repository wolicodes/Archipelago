from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item
from worlds.etrian_odyssey_hd.data.Items import DEFAULT_ITEM_CLASSIFICATIONS, ITEM_NAME_TO_ID, Items

if TYPE_CHECKING:
    from .world import EOHDWorld


class EOHDItem(Item):
    game = "Etrian Odyssey HD"


def get_random_filler_item_name(world: EOHDWorld) -> str:
    if world.random.randint(0, 100) == 1:
        return Items.EN1.value
    if world.random.randint(0, 100) <= 50:
        return Items.EN50.value
    return Items.EN100.value


def create_item_with_correct_classification(world: EOHDWorld, name: str) -> EOHDItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return EOHDItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: EOHDWorld) -> None:
    itempool: list[Item] = [
        world.create_item(Items.AXCELA.value),
        world.create_item(Items.AMRITA.value),
        world.create_item(Items.MEDICA.value),
        world.create_item(Items.SCRAMASAX.value),
        world.create_item(Items.KNIFE.value),
        world.create_item(Items.STAFF.value),
        world.create_item(Items.WAND.value),
        world.create_item(Items.HATCHET.value),
        world.create_item(Items.WOOD_BOW.value),
        world.create_item(Items.LIGHT_WHIP.value),
        world.create_item(Items.TWEED.value),
        world.create_item(Items.TARGE.value),
        world.create_item(Items.HAIRPIN.value),
        world.create_item(Items.KNIT_GLOVE.value),
        world.create_item(Items.LEAF_BOOT.value),
        world.create_item(Items.HIDE_BELT.value),
        world.create_item(Items.WARD_CHIME.value),
        world.create_item(Items.ARIADNE_THREAD.value),
        # world.create_item(Items.VICTORY.value),
        world.create_item(Items.RADHA_NOTE.value),
        world.create_item(Items.EN500.value),
        world.create_item(Items.WHITESTONE.value),
        world.create_item(Items.SCRAMASAX.value),
        world.create_item(Items.MEDICA_II.value),
        world.create_item(Items.EN200.value),
        # B1F Main: Event Moles Attack
        world.create_item(Items.NIGHT_10TP.value),
        world.create_item(Items.FIRST_CHAR_10HP.value),
        world.create_item(Items.EN100.value),
        # B1F Main: Event Venomflies Attack
        # B1F Main: D1 Chop
        # B1F Main: D3 Chop
        world.create_item(Items.NECTAR.value),
        world.create_item(Items.NECTAR_II.value),
        world.create_item(Items.GEM_STAFF.value),
        world.create_item(Items.PLUMED_HAT.value),
        world.create_item(Items.MEDICA_II.value),
        world.create_item(Items.RAPIER.value),
        world.create_item(Items.EN500.value),
        # No locations for these yet
        world.create_item(Items.CLEAR_KEY.value),
        world.create_item(Items.VIOLET_KEY.value),
        world.create_item(Items.FIRST_STRATUM_CLEARED.value),
    ]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool
