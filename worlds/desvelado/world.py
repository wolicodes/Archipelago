from collections.abc import Mapping
from typing import Any

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, locations, regions, rules, web_world
from . import options as desvelado_options  # rename due to a name conflict with World.options

class DesveladoWorld(World):
    """
    Desvelado is a short and cute puzzle-platformer developed by Vampi Team.
    """
    game = "Desvelado"
    web = web_world.DesveladoWebWorld()

    options_dataclass = desvelado_options.DesveladoOptions
    options: desvelado_options.DesveladoOptions  # Common mistake: This has to be a colon (:), not an equals sign (=).

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Map Screen"

    ut_can_gen_without_yaml = True

    # UT
    def generate_early(self) -> None:
        passthrough = getattr(self.multiworld, "re_gen_passthrough", {}).get(self.game)
        if not passthrough:
            return
        options = self.options
        options.goal = options.goal.from_any(passthrough["goal"])
        options.shuffle_bonnies_bones = options.shuffle_bonnies_bones.from_any(passthrough["shuffle_bonnies_bones"])

    # UT
    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

    # Our world class must have certain functions ("steps") that get called during generation.
    # The main ones are: create_regions, set_rules, create_items.
    # For better structure and readability, we put each of these in their own file.
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.DesveladoItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "goal", "shuffle_bonnies_bones"
        )
