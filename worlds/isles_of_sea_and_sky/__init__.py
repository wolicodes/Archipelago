import os.path
import warnings
from typing import Any

from .Items import IslesOfSeaAndSkyItem, item_table, non_key_items, key_items, note_items, \
    mysterious_items, meteorite_items, mysterious_meteorite_items, junk_weights, progression_items, trap_weights
from .Locations import IslesOfSeaAndSkyAdvancement, AdvData, advancement_table, exclusion_table, \
    jellyfish_table, seashell_table, note_table, mysterious_table, meteorite_table, \
    circlet_meteorite_table, locksanity_table, snakesanity_table, secrets_table, get_locations, \
    mysterious_snakesanity_table, meteorite_snakesanity_table, circlet_meteorite_snakesanity_table
from .Regions import isles_of_sea_and_sky_regions, circlet_regions, meteorite_regions, \
    mandatory_connections, meteorite_connections, circlet_connections, warp_logic_connections, \
    circlet_meteorite_connections, warp_logic_regions, circlet_meteorite_regions
from .Rules import set_rules, set_completion_rules
#from worlds.generic.Rules import exclusion_rules
from BaseClasses import Region, Entrance, Tutorial, Item, ItemClassification as IC
from .Options import IslesOfSeaAndSkyOptions, isles_of_sea_and_sky_option_groups
from worlds.AutoWorld import World, WebWorld
import worlds.LauncherComponents as LauncherComponents

from settings import (
    Group,
    FilePath,
)





def launch_client() -> None:
    from .Client import main
    LauncherComponents.launch_subprocess(main, name="IslesOfSeaAndSkyClient")


LauncherComponents.components.append(
    LauncherComponents.Component(
        "Isles Of Sea And Sky Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
        icon="isles_of_sea_and_sky"
    )
)


isles_component = LauncherComponents.components[len(LauncherComponents.components) - 1]
# Checks first component for a Class property that should be shared by all components
# for backwards compatibility
if hasattr(isles_component, "description"):
    isles_component.description = "That Sokoban Adventure Game by Cicada Games!"

LauncherComponents.icon_paths["isles_of_sea_and_sky"] = f"ap:{__name__}/data/sprites/isles_of_sea_and_sky.png"

def data_path(file_name: str):
    import pkgutil
    return pkgutil.get_data(__name__, "data/" + file_name)

def read_data(file_path: str):
    import pkgutil
    return pkgutil.get_data(__name__, file_path)


class IslesOfSeaAndSkySettings(Group):
    class GMDataFile(FilePath):
        """Path to IslesOfSeaAndSky Vanilla data file"""
        description = "Isles Of Sea And Sky Vanilla File"
        md5s = [
            "FD3AE5AE6D9DC29F7A7BF3FCF63CE96D" # steam, v2.6a first release
            #"",  # epic
            # "",  # itch.io, does not work
            ]
        # the hashes for vanilla to be verified by the /patch command
        required = True
    steam_install = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\IslesOfSeaAndSky"
    data_file: GMDataFile = GMDataFile(os.path.join(steam_install, "data.win"))

class IslesOfSeaAndSkyWeb(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Isles Of Sea And Sky software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Kim-Delicious"]
    )]

    option_groups = isles_of_sea_and_sky_option_groups


class IslesOfSeaAndSkyWorld(World):
    """
    Isles Of Sea And Sky is a sokoban-style puzzle game with metroidvania elements.
    As the player collects items, and equipment they can explore islands to collect as many goodies as they can,
    until they reach the Sanctum, and learn just what all these Stars are for.
    """
    game = "Isles Of Sea And Sky"
    options_dataclass = IslesOfSeaAndSkyOptions
    settings: IslesOfSeaAndSkySettings
    options: IslesOfSeaAndSkyOptions
    web = IslesOfSeaAndSkyWeb()

    ut_can_gen_without_yaml = True

    #explicit_indirect_conditions = False

    item_name_to_id = {name: data.code for name, data in item_table.items()}

    location_name_to_id = (
            {name: data.id for name, data in advancement_table.items()} |
            {name: data.id for name, data in jellyfish_table.items()} |
            {name: data.id for name, data in seashell_table.items()} |
            {name: data.id for name, data in note_table.items()} |
            {name: data.id for name, data in mysterious_table.items()} |
            {name: data.id for name, data in meteorite_table.items()} |
            {name: data.id for name, data in circlet_meteorite_table.items()} |
            {name: data.id for name, data in locksanity_table.items()} |
            {name: data.id for name, data in snakesanity_table.items()}|
            {name: data.id for name, data in mysterious_snakesanity_table.items()}|
            {name: data.id for name, data in meteorite_snakesanity_table.items()}|
            {name: data.id for name, data in circlet_meteorite_snakesanity_table.items()}|
            {name: data.id for name, data in secrets_table.items()}
    )


    def _get_isles_of_sea_and_sky_data(self):
        return {
            "world_seed":                   self.random.getrandbits(32),
            "seed_name":                    self.multiworld.seed_name,
            "player_name":                  self.multiworld.get_player_name(self.player),
            "player_id":                    self.player,
            "client_version":               self.required_client_version,
            "race":                         self.multiworld.is_race,
            "route_required":               self.options.route_required.current_key,
            "star_pieces_required":         int(self.options.star_pieces_required.value),
            "pyramidions_required":         int(self.options.pyramidions_required.value),
            "shuffle_gems":                 bool(self.options.shuffle_gems.value),
            "shuffle_notes":                bool(self.options.shuffle_notes.value),
            "shuffle_pyramidions":          bool(self.options.shuffle_pyramidions.value),
            "shuffle_meteorites":           bool(self.options.shuffle_meteorites.value),
            "shuffle_elemental_quests":     bool(self.options.shuffle_elemental_quests.value),
            "shuffle_big_bell_hits":        bool(self.options.shuffle_big_bell_hits.value),
            "shuffle_sanctum_shard_hits":   bool(self.options.shuffle_sanctum_shard_hits.value),
            "enable_locksanity":            False, # bool(self.options.enable_locksanity.value),
            "enable_snakesanity":           bool(self.options.enable_snakesanity.value),
            "include_seashells":            False, # bool(self.options.include_seashells.value),
            "include_jellyfish":            False, # bool(self.options.include_jellyfish.value),
            "serpent_puzzle_memorization":  bool(self.options.serpent_puzzle_memorization.value),
            "warps_in_logic":               bool(self.options.warps_in_logic.value),
            "phoenix_anywhere":             bool(self.options.phoenix_anywhere.value),
            "traps":                        self.options.traps.current_key,
            "filler_composition":           self.options.filler_composition.current_key,
            "secretsanity":                 False, # bool(self.options.secretsanity.value),
            "death_link":                   bool(self.options.death_link.value),
            "death_amnesty_total":          int(self.options.death_amnesty_total.value),
            "alt_rooms":                    False # bool(self.options.alt_rooms.value),

        }

    # UT
    def generate_early(self) -> None:
        options = self.options

        # Warps are mandatory when meteorites are in logic
        options.warps_in_logic.value = options.warps_in_logic.value | options.shuffle_meteorites.value

        passthrough = getattr(self.multiworld, "re_gen_passthrough", {}).get(self.game)
        if not passthrough:
            return
        options.route_required = options.route_required.from_any(passthrough["route_required"])
        options.star_pieces_required = options.star_pieces_required.from_any(passthrough["star_pieces_required"])
        options.pyramidions_required = options.pyramidions_required.from_any(passthrough["pyramidions_required"])
        options.shuffle_gems = passthrough["shuffle_gems"]
        options.shuffle_notes = passthrough["shuffle_notes"]
        options.shuffle_pyramidions = passthrough["shuffle_pyramidions"]
        options.shuffle_meteorites = passthrough["shuffle_meteorites"]
        options.shuffle_elemental_quests = passthrough["shuffle_elemental_quests"]
        options.shuffle_big_bell_hits = passthrough["shuffle_big_bell_hits"]
        options.shuffle_sanctum_shard_hits = passthrough["shuffle_sanctum_shard_hits"]
        # options.enable_locksanity = passthrough["enable_locksanity"]
        options.enable_snakesanity = passthrough["enable_snakesanity"]
        # options.secretsanity = passthrough["secretsanity"]
        # options.include_seashells = passthrough["include_seashells"]
        # options.include_jellyfish = passthrough["include_jellyfish"]
        options.serpent_puzzle_memorization = passthrough["serpent_puzzle_memorization"]
        options.warps_in_logic = passthrough["warps_in_logic"]
        options.phoenix_anywhere = passthrough["phoenix_anywhere"]

    # UT
    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

    def get_filler_item_name(self):

        junk_pool = junk_weights
        return self.random.choices(list(junk_pool.keys()), weights=list(junk_pool.values()))[0]

    def create_items(self):

        self.multiworld.get_location("Ancient B3 - Ancient Key", self.player).place_locked_item(
            self.create_item("Ancient Key"))
        self.multiworld.get_location("Ancient A1 - Ancient Key", self.player).place_locked_item(
            self.create_item("Ancient Key"))
        self.multiworld.get_location("Ancient A2 - SE - Ancient Key", self.player).place_locked_item(
            self.create_item("Ancient Key"))
        self.multiworld.get_location("Ancient A3 - N - Ancient Key", self.player).place_locked_item(
            self.create_item("Ancient Key"))
        self.multiworld.get_location("Ancient A3 - S - Ancient Key", self.player).place_locked_item(
            self.create_item("Ancient Key"))
        self.multiworld.get_location("Ancient C2 - Ancient Key", self.player).place_locked_item(
            self.create_item("Ancient Key"))

        self.multiworld.get_location("Ancient C0 - Star Piece", self.player).place_locked_item(
            self.create_item("Star Piece"))

        # Create copies of pools so that data isn't changed when multiple worlds are used
        progression_pool = progression_items.copy()
        key_pool = key_items.copy()
        non_key_pool = non_key_items.copy()
        note_pool = note_items.copy()
        junk_pool = junk_weights.copy()
        trap_pool = trap_weights.copy()

        if self.options.circlet_content_enabled:
            for name, num in mysterious_items.items():
                if name in progression_pool: progression_pool[name] += num
                if name in key_pool: key_pool[name] += num
                if name in non_key_pool: non_key_pool[name] += num


        if self.options.shuffle_meteorites:
            for name, num in meteorite_items.items():
                if name in progression_pool: progression_pool[name] += num
                if name in key_pool: key_pool[name] += num
                if name in non_key_pool: non_key_pool[name] += num
            if self.options.circlet_content_enabled:
                for name, num in mysterious_meteorite_items.items():
                    if name in progression_pool: progression_pool[name] += num
                    if name in key_pool: key_pool[name] += num
                    if name in non_key_pool: non_key_pool[name] += num
        
        # Remove the pre-placed items from generation
        key_pool['Ancient Key'] -= 6
        key_pool['Star Piece'] -= 1

        if not self.options.shuffle_gems:
            gem_names = {"Topaz", "Sapphire", "Ruby", "Diamond", "Obsidian"}
            expected_gem_locations = (66 if self.options.shuffle_pyramidions else 62)
            gem_locations = {loc_name: loc_name.rsplit(" - ", 1)[-1]
                             for loc_name in advancement_table
                             if loc_name.rsplit(" - ", 1)[-1] in gem_names}
            if (self.options.shuffle_pyramidions):
                gem_locations |= {loc_name: loc_name.rsplit(" - ", 1)[-1]
                             for loc_name in mysterious_table
                             if loc_name.rsplit(" - ", 1)[-1] in gem_names}
            assert len(gem_locations) == expected_gem_locations, \
                f"Expected {expected_gem_locations} gem locations, found {len(gem_locations)}"
            for loc_name, gem in gem_locations.items():
                self.multiworld.get_location(loc_name, self.player).place_locked_item(
                    self.create_item(gem))
                key_pool[gem] -= 1
                    
        if not self.options.shuffle_elemental_quests:
            elemental_quests_vanilla_placements = {
                "Stone C0 - Topaz Quest Complete": "Awaken Earth Elementals",
                "Water C0 - Sapphire Quest Complete": "Awaken Water Elementals",
                "Fire C0 - Ruby Quest Complete": "Awaken Fire Elementals",
                "Wind C2 - Diamond Quest Complete": "Awaken Wind Elementals",
                "Serpent A1 - Obsidian Quest Complete": "Awaken Shadow Elementals",
            }
            for loc_name, item_name in elemental_quests_vanilla_placements.items():
                self.multiworld.get_location(loc_name, self.player).place_locked_item(
                    self.create_item(item_name))
                progression_pool[item_name] -= 1
                
        if not self.options.shuffle_big_bell_hits:
            beast_bell_vanilla_placements = {
                "Rolling B0 - Big Bell Rung": "Big Bell Hit - Rolling",
                "Sunken B1 - Big Bell Rung": "Big Bell Hit - Sunken",
                "Aggro A1 - Big Bell Rung": "Big Bell Hit - Aggro",
                "Nunatak A1 - Big Bell Rung": "Big Bell Hit - Nunatak",
            }
            for loc_name, item_name in beast_bell_vanilla_placements.items():
                self.multiworld.get_location(loc_name, self.player).place_locked_item(
                    self.create_item(item_name))
                key_pool[item_name] -= 1

        if not self.options.shuffle_sanctum_shard_hits:
            sanctum_hits_vanilla_placements = {
                "Sanctum A2 - Topaz Shard Hit": "Sanctum Shard Hit - Earth",
                "Sanctum C2 - Sapphire Shard Hit": "Sanctum Shard Hit - Water",
                "Sanctum C0 - Ruby Shard Hit": "Sanctum Shard Hit - Fire",
                "Sanctum A0 - Diamond Shard Hit": "Sanctum Shard Hit - Wind",
            }
            for loc_name, item_name in sanctum_hits_vanilla_placements.items():
                self.multiworld.get_location(loc_name, self.player).place_locked_item(
                    self.create_item(item_name))
                key_pool[item_name] -= 1

        if ((self.options.route_required == "mysterious_ending") and (not self.options.shuffle_pyramidions)):
            # The one key
            self.multiworld.get_location("Sunken A1 Serpent Secret - Ancient Key", self.player).place_locked_item(
                    self.create_item("Ancient Key"))
            key_pool["Ancient Key"] -= 1
            # 4 obsidian
            if (self.options.shuffle_gems): # If shuffle gems is off then we already placed this gem in its vanilla location
                obsidian_locations = {
                    "Fire D3 Serpent Secret - Obsidian",
                    "Aggro A0 Serpent Secret - Obsidian",
                    "Nunatak A1 Serpent Secret - Obsidian",
                    "Tropic A1 Serpent Secret - Obsidian"
                }
                for loc_name in obsidian_locations:
                    self.multiworld.get_location(loc_name, self.player).place_locked_item(
                        self.create_item("Obsidian"))
                    key_pool["Obsidian"] -= 1
            # 30 pyramidions
            pyramidion_locations = {loc_name: loc_name
                             for loc_name in mysterious_table
                             if " Pyramidion" in loc_name}
            assert len(pyramidion_locations) == 30, \
                f"Expected 30 pyramidion locations, found {len(pyramidion_locations)}"
            for loc_name in pyramidion_locations:
                self.multiworld.get_location(loc_name, self.player).place_locked_item(
                    self.create_item("Pyramidion"))
                non_key_pool["Pyramidion"] -= 1

        if False and (not self.options.shuffle_meteorites): # For upcoming meteorite goal
            warp_placements = {
                "Stone C2 - Earth Warp Pattern":            "Warp Pattern - Earth",
                "Water B4 - Water Warp Pattern":            "Warp Pattern - Water",
                "Fire C3 - Fire Warp Pattern":              "Warp Pattern - Fire",
                "Wind B3 - Wind Warp Pattern":              "Warp Pattern - Wind",
                "Warp ?? - Tropic Warp Pattern":            "Warp Pattern - Tropic",
                "Lost B1 - Lost Warp Pattern":              "Warp Pattern - Lost",
                "Ancient Cavern B1 - Ancient Warp Pattern": "Warp Pattern - Ancient",
                "Lost A0 - Compass Warp Pattern":           "Warp Pattern - Compass"
            }
            for loc_name, item_name in warp_placements.items():
                self.multiworld.get_location(loc_name, self.player).place_locked_item(
                    self.create_item(item_name))
                key_pool[item_name] -= 1
                meteorite_locations = {
                    "Tropic B1 - Meteorite",
                    "Lost A0 - Meteorite",
                    "Ancient A0 - Meteorite",
                    "Totem B0 - Meteorite"
                }
            for loc_name in meteorite_locations:
                self.multiworld.get_location(loc_name, self.player).place_locked_item(
                    self.create_item("Meteorite"))
                non_key_pool["Meteorite"] -= 1

        # Bias generation to reduce fill errors
        self.multiworld.early_items[self.player]["Topaz Rune Stone"] = 1

        # Generate item pool
        itempool = []
        # Add all required progression items
        for name, num in progression_pool.items():
            itempool += [name] * num
        for name, num in key_pool.items():
            itempool += [name] * num
        for name, num in non_key_pool.items():
            itempool += [name] * num

        if self.options.shuffle_notes:
            for name, num in note_pool.items():
                itempool += [name] * num

        missing_items = len(self.multiworld.get_unfilled_locations(self.player) ) - len(itempool)
        print("Creating " + str(missing_items) + " Filler Items for " + str(self.game) )

        # Create a limited number of traps based on a weighted list of items.
        trap_number = 0
        match self.options.traps.current_key:
            case "some_traps":
                trap_number = self.random.randrange(4, 9)
            case "plenty_traps":
                trap_number = self.random.randrange(10, 20)
            case _:  # default
                pass

        if trap_number > missing_items:
            trap_number = missing_items

        if trap_number > 0:
            print("Converting " + str(trap_number) + " Filler Items into Traps")
            trap_item_weights = []

            for name, num in trap_pool.items():
                trap_item_weights += [name] * num

            while trap_number > 0:
                rand_item = self.random.choice(trap_item_weights)
                itempool += [rand_item]
                trap_number -= 1
                missing_items -= 1

        composition = self.options.filler_composition.current_key
        weight_list = []
        # Add filler weights to potential filler pool
        for name, num in junk_pool.items():
            if composition == "default" and name != "Seashell":
                continue
            if composition == "only_goodies" and name == "Seashell":
                continue
            weight_list += [name] * num

        # For each free filler spot, choose an item from weight_list at random, then add it to the item pool
        while missing_items > 0:
            itempool += [self.random.choice(weight_list)]
            missing_items -= 1

        # Convert itempool into real items
        itempool = [item for item in map(lambda item_name: self.create_item(item_name), itempool)]

        self.multiworld.itempool += itempool

    def set_rules(self):
        set_rules(self)
        set_completion_rules(self)

        '''# for creating visuals, should be disabled for unittests
        from Utils import visualize_regions
        state = self.multiworld.get_all_state(False)
        state.update_reachable_regions(self.player)
        state.allow_partial_entrances = True
        visualize_regions(self.get_region("Menu"), "my_world.puml", show_entrance_names=True,
                          regions_to_highlight=state.reachable_regions[self.player])'''

    def create_regions(self):
        def IslesOfSeaAndSkyRegion(region_name: str, exits: list[str] | None=None, locations: list[tuple[str, AdvData]] | None=None):
            if exits is None:
                exits = []
            if locations is None:
                locations = []

            ret = Region(region_name, self.player, self.multiworld)

            # Locations
            ret.locations += [IslesOfSeaAndSkyAdvancement(self.player, loc_name, loc_data.id, ret)
                              for loc_name, loc_data in locations]

            for region_exit in exits:
                ret.exits.append(Entrance(self.player, region_exit, ret))

            return ret

        # Collect all regions, exits, and items
        # Declare a dictionary to amalgamate our entrances and items. This allows us to amalgamate our tables in a reasonable amount of time
        regions: dict[str, tuple[list[str], list[tuple[str, AdvData]]]] = (
            dict([(region, (entrances.copy(), [])) for region, entrances in isles_of_sea_and_sky_regions]))

        # Amalgamate Entrances
        if self.options.circlet_content_enabled:
            for region, exits in circlet_regions:
                if region in regions: regions[region][0].extend(exits)
                else: regions[region] = (exits.copy(), [])
        if self.options.warps_in_logic:
            for region, exits in warp_logic_regions:
                if region in regions: regions[region][0].extend(exits)
                else: regions[region] = (exits.copy(), [])
        if self.options.shuffle_meteorites:
            for region, exits in meteorite_regions:
                if region in regions: regions[region][0].extend(exits)
                else: regions[region] = (exits.copy(), [])
        if self.options.shuffle_meteorites & self.options.circlet_content_enabled:
            for region, exits in circlet_meteorite_regions:
                if region in regions: regions[region][0].extend(exits)
                else: regions[region] = (exits.copy(), [])

        # Get Locations
        locations = get_locations(self.options)
        # Assign Locations to their regions

        # Assign Locations to Regions
        for location_name, advData in locations.items():
            if advData.region in regions:
                regions[advData.region][1].append((location_name, advData))
            else: raise Exception(f"Failed to place location '{location_name}', region '{advData.region}' does not exist!")

        # Create Regions
        self.multiworld.regions += [IslesOfSeaAndSkyRegion(region, entrances, locations) for region, (entrances, locations) in regions.items()]
        self.link_regions()

    def link_regions(self):
        world = self.multiworld
        player = self.player
        created_regions = {region.name for region in world.get_regions(player)}
        created_exits = {region_exit.name
                         for region in world.get_regions(player)
                         for region_exit in region.exits}
        connections = list(mandatory_connections).copy()
        if self.options.circlet_content_enabled:
            connections += circlet_connections
        if self.options.warps_in_logic:
            connections += warp_logic_connections
        if self.options.shuffle_meteorites:
            connections += meteorite_connections
        if self.options.shuffle_meteorites & self.options.circlet_content_enabled:
            connections += circlet_meteorite_connections

        for (region_exit, region) in connections:
            world.get_entrance(region_exit, player).connect(world.get_region(region, player))

    def fill_slot_data(self):
        return self._get_isles_of_sea_and_sky_data()

    def create_item(self, name: str) -> Item:
        if name is None:
            warnings.warn("Attempted to create an item with a None name")
            name = "Seashell"

        item_data = item_table[name]
        classification = item_data.classification
        if name  == "Pyramidion" and self.options.route_required != "mysterious_ending":
            classification = IC.filler
        item = IslesOfSeaAndSkyItem(name, classification, item_data.code, self.player)
        return item
