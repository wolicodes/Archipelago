from collections.abc import Mapping
from typing import Any
from worlds.AutoWorld import World
from worlds.etrian_odyssey_hd.data.Items import ITEM_NAME_TO_ID
from worlds.etrian_odyssey_hd.data.Locations import LOCATION_NAME_TO_ID
from . import items, locations, options, regions, rules, web_world

class EOHDWorld(World):
    """
    Etrian Odyssey is a dungeon crawler RPG first developed by Atlus in 2007 on the Nintendo DS,
    re-released in 2023 in HD on Steam and the Nintendo Switch.
    Lead a team of explorers into the dungeon with the promise of checks, Burger Kings, and goaling your seed!
    """
    game = "Etrian Odyssey HD"
    web = web_world.EOHDWebWorld()

    options_dataclass = options.EOHDOptions
    options: options.EOHDOptions

    location_name_to_id = LOCATION_NAME_TO_ID
    item_name_to_id = ITEM_NAME_TO_ID

    origin_region_name = "Etria"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.EOHDItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "starting_money"
        )
