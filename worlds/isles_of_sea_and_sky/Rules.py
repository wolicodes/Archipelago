from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import CanReachRegion, Has

from .Options import PhoenixAnywhere, EnableNotesanity

if TYPE_CHECKING:
    from . import IslesOfSeaAndSkyWorld


# Sets rules on entrances and advancements that are always applied
def set_rules(world: "IslesOfSeaAndSkyWorld"):

    ### WILL IMPACT PERFORMANCE OF GAME GENERATION
    # world.explicit_indirect_conditions = False

    set_rechecks(world)

    ### Entrances
    world.set_rule(world.get_entrance("Ancient West Exit"),
                   CanReachRegion("Ruby Sea"))  # Obsidian Sea

    '''world.set_rule(world.get_entrance("Ancient East Exit"),
                   Has("Ancient Key", 6) & Has("Star Piece"))  # Topaz Sea'''


    ## Required for completion detection
    world.set_rule(world.get_entrance("Ancient North Exit"),
                   Has("Awaken Earth Elementals")
                   & Has("Awaken Water Elementals")
                   & Has("Awaken Fire Elementals")
                   & Has("Awaken Wind Elementals"))  # Sanctum

    ## Required for completion detection
    world.set_rule(world.get_entrance("Elemental Rock Path"),
                   Has("Sanctum Shard Hit - Earth")
                   & Has("Sanctum Shard Hit - Water")
                   & Has("Sanctum Shard Hit - Fire")
                   & Has("Sanctum Shard Hit - Wind"))  # Sanctum Peak


    world.set_rule(world.get_entrance("Diamond Sea West Entrance"),
                   Has("Star Piece", 3))  # Diamond Sea

    world.set_rule(world.get_entrance("Stony Exit To Post-Rune"),
                   Has("Topaz Rune Stone"))  # Stony Cliffs Post-Rune
    world.set_rule(world.get_entrance("Stony West Exit"),
                   Has("Topaz Rune Stone"))  # Stony Cliffs NW
    world.set_rule(world.get_entrance("Stony NW East Exit"),
                   Has("Topaz Rune Stone"))  # Stony Cliffs
    world.set_rule(world.get_entrance("Stony NW West Exit"),
                   Has("Star Piece", 5))  # Sapphire Sea

    world.set_rule(world.get_entrance("Stony West Entrance"),
                   Has("Star Piece", 5))  # Stony NW



    # NOTE: Has only works with items classified as progression

    world.set_rule(world.get_entrance("Ruby Sea West Entrance"),
                   Has("Star Piece", 15))  # Ruby Sea

    world.set_rule(world.get_entrance("Diamond Sea Exit"),
                   Has("Star Piece", 30))  # North Diamond Sea

    world.set_rule(world.get_entrance("North Diamond Sea South Exit"),
                   Has("Star Piece", 30))  # Diamond Sea
    world.set_rule(world.get_entrance("North Diamond Sea East Exit"),
                   CanReachRegion("Lost Sea"))  # Northeast Sea


    world.set_rule(world.get_entrance("Serpent Entrance"),
                   Has("Star Piece", 45))  # Serpent Stacks

    world.set_rule(world.get_entrance("Tidal S Exit"),
                   Has("Sapphire Rune Stone")
                   | Has("Frog Flippers"))  # Tidal Reef
    world.set_rule(world.get_entrance("Tidal Exit To Post-Rune"),
                   Has("Sapphire Rune Stone"))  # Tidal Reef Post-Rune
    world.set_rule(world.get_entrance("Tidal S Exit To Post-Rune"),
                   Has("Sapphire Rune Stone"))  # Tidal Reef Post-Rune
    world.set_rule(world.get_entrance("Tidal Exit To S"),
                   Has("Sapphire Rune Stone")
                   | Has("Frog Flippers"))  # Tidal Reef S
    world.set_rule(world.get_entrance("Tidal S Entrance From Post-Rune"),
                   Has("Frog Flippers"))  # Tidal Reef S

    world.set_rule(world.get_entrance("Raging Exit To Post-Rune"),
                   Has("Ruby Rune Stone"))  # Raging Volcano Post-Rune
    world.set_rule(world.get_entrance("Raging NE Exit"),
                   Has("Awaken Fire Elementals")
                   | CanReachRegion("Raging Volcano Post-Rune")
                   | (Has("Ruby Rune Stone")
                      & Has("Salamander Shirt")))  # Raging Volcano
    world.set_rule(world.get_entrance("Raging Exit To NE"),
                   Has("Ruby Rune Stone"))  # Raging Volcano NE

    world.set_rule(world.get_entrance("Frozen Exit To Post-Rune"),
                   Has("Diamond Rune Stone"))  # Frozen Spire Post-Rune

    world.set_rule(world.get_entrance("Serpent Exit To Post-Rune"),
                   Has("Obsidian Rune Stone"))  # Serpent Stacks Post-Rune


    world.set_rule(world.get_entrance("Star West Exit"),
                   CanReachRegion("Lost Sea"))  # Lost Sea | Gen Failures
    world.set_rule(world.get_entrance("Star East Exit"),
                   Has("Ancient Rune Stone"))  # Lost Sea
    world.set_rule(world.get_entrance("Star East Entrance"),
                   Has("Ancient Rune Stone")
                   & CanReachRegion("Lost Sea"))  # Star Tropic

    world.set_rule(world.get_entrance("Rolling Exit To Post-Rune"),
                   Has("Ancient Rune Stone"))  # Rolling Rocks Post-Rune

    world.set_rule(world.get_entrance("Shoal Entrance"),
                   Has("Ancient Rune Stone"))  # Shoal

    world.set_rule(world.get_entrance("Locked Entrance"),
                   CanReachRegion("Ruby Sea"))

    world.set_rule(world.get_entrance("Beast Entrance"),
                   Has("Big Bell Hit - Rolling")
                   & Has("Big Bell Hit - Sunken")
                   & Has("Big Bell Hit - Aggro")
                   & Has("Big Bell Hit - Nunatak"))

    world.set_rule(world.get_entrance("Abstract Phoenix Exit"),
                   Has("Phoenix Flute",
                       options=[OptionFilter(PhoenixAnywhere, PhoenixAnywhere.option_true)]))  # Phoenix Hub
    world.set_rule(world.get_entrance("Beast Bridge Phoenix"),
                   Has("Phoenix Flute"))  # Phoenix Hub
    world.set_rule(world.get_entrance("Stony Phoenix"),
                   Has("Phoenix Flute"))  # Phoenix Hub
    world.set_rule(world.get_entrance("Tidal Phoenix"),
                   Has("Phoenix Flute"))  # Phoenix Hub
    world.set_rule(world.get_entrance("Raging Phoenix"),
                   Has("Phoenix Flute"))  # Phoenix Hub
    world.set_rule(world.get_entrance("Frozen Phoenix"),
                   Has("Phoenix Flute") & Has("Diamond Rune Stone"))  # Phoenix Hub
    world.set_rule(world.get_entrance("Lost Phoenix"),
                   Has("Phoenix Flute"))  # Phoenix Hub

    world.set_rule(world.get_entrance("Beast Bridge Phoenix Entrance"),
                   Has("Phoenix Flute")
                   & Has("Big Bell Hit - Rolling")
                   & Has("Big Bell Hit - Sunken")
                   & Has("Big Bell Hit - Aggro")
                   & Has("Big Bell Hit - Nunatak"))  # Beast Bridge
    world.set_rule(world.get_entrance("Stony Phoenix Entrance"),
                   Has("Phoenix Flute"))  # Stony Cliffs
    world.set_rule(world.get_entrance("Tidal Phoenix Entrance"),
                   Has("Phoenix Flute")
                   & (Has("Sapphire Rune Stone") | Has("Frog Flippers")))  # Tidal Reef
    world.set_rule(world.get_entrance("Raging Phoenix Entrance"),
                   Has("Phoenix Flute"))  # Raging Volcano NE
    world.set_rule(world.get_entrance("Frozen Phoenix Entrance"),
                   Has("Phoenix Flute")
                   & Has("Diamond Rune Stone"))  # Frozen Spire
    world.set_rule(world.get_entrance("Lost Phoenix Entrance"),
                   Has("Phoenix Flute")
                   & Has("Star Piece", 30))  # Lost Landing


    if world.options.enable_locksanity:
        world.set_rule(world.get_location("Overworld - Star Lock 3"),
                       Has("Star Piece", 3))
        world.set_rule(world.get_location("Overworld - Star Lock 15"),
                       Has("Star Piece", 15))
        world.set_rule(world.get_location("Overworld - Star Lock 30"),
                       Has("Star Piece", 30))
        world.set_rule(world.get_location("Overworld - Star Lock 45"),
                       Has("Star Piece", 45))


    ### Locations

    # Legendary Item Locations
    world.set_rule(world.get_location("Stone Dungeon C1 - Gopher Gloves"),
                   (Has("Topaz Rune Stone")
                    & Has("Awaken Earth Elementals"))
                   | Has("Gopher Gloves"))

    world.set_rule(world.get_location("Water A4 - Frog Flippers"),
                   Has("Sapphire Rune Stone"))

    world.set_rule(world.get_location("Fire E0 - Salamander Shirt"),
                   Has("Fire Key", 3))

    world.set_rule(world.get_location("Wind A0 - Kite Cloak"),
                   Has("Diamond Rune Stone")
                   & (Has("Awaken Wind Elementals")
                      | Has("Kite Cloak")))  # since Eggs and Wind key are broken, don't include

    # world.set_rule(world.get_location("Serpent A5 - Serpent Circlet"), # TODO
    #                Has("Topaz Rune Stone")
    #                & Has("Sapphire Rune Stone")
    #                & Has("Ruby Rune Stone")
    #                & Has("Diamond Rune Stone")
    #                & Has("Obsidian Rune Stone")
    #                & Has("Obsidian", 9))

    # Quests
    world.set_rule(world.get_location("Stone C0 - Topaz Quest Complete"),
                   Has("Topaz", 6))

    world.set_rule(world.get_location("Water C0 - Sapphire Quest Complete"),
                   Has("Sapphire", 6))

    world.set_rule(world.get_location("Fire C0 - Ruby Quest Complete"),
                   Has("Ruby", 6))

    world.set_rule(world.get_location("Wind C2 - Diamond Quest Complete"),
                   Has("Diamond", 6))
    
    world.set_rule(world.get_location("Serpent A1 - Obsidian Quest Complete"),
                   Has("Topaz Rune Stone")
                   & Has("Sapphire Rune Stone")
                   & Has("Ruby Rune Stone")
                   & Has("Diamond Rune Stone")
                   & Has("Obsidian Rune Stone")
                   & Has("Obsidian", 9))

    # Islands and their Locations
    set_ancient_isle(world)
    set_rolling_rocks(world)
    set_sunken_island(world)
    set_aggro_crag(world)
    set_sea_nunatak(world)
    set_locked(world)
    set_star_tropic(world)
    set_shoal(world)
    set_lost_landing(world)


    set_stony_cliffs(world)
    set_tidal_reef(world)
    set_raging_volcano(world)
    set_frozen_spire(world)
    set_serpent_stacks(world)
    set_beast_bridge(world)
    set_sanctum(world)


def set_ancient_isle(world: "IslesOfSeaAndSkyWorld"):

    # Collectables
    world.set_rule(world.get_location("Ancient A1 - Star Piece"),
                   (CanReachRegion("Ruby Sea")
                    | CanReachRegion("Sapphire Sea"))
                   & Has("Ancient Key", 17))

    world.set_rule(world.get_location("Ancient B1 - Star Piece"),
                   (CanReachRegion("Ruby Sea")
                    | CanReachRegion("Sapphire Sea"))
                   & Has("Ancient Rune Stone")
                   & Has("Ancient Key", 17))

    world.set_rule(world.get_location("Ancient A2 - NW - Ancient Key"),
                   Has("Awaken Earth Elementals"))  # and CanReachRegion("Topaz Sea")

    '''world.set_rule(world.get_location("Ancient A1 - Ancient Key"),
                   Has("Ancient Key"))

    world.set_rule(world.get_location("Ancient A2 - SE - Ancient Key"),
                   Has("Ancient Key"))

    world.set_rule(world.get_location("Ancient A3 - N - Ancient Key"),
                   Has("Ancient Key", 2))
    world.set_rule(world.get_location("Ancient A3 - S - Ancient Key"),
                   Has("Ancient Key"))
    world.set_rule(world.get_location("Ancient A3 - E - Ancient Key"),
                   Has("Ancient Key", 2))

    world.set_rule(world.get_location("Ancient C2 - Ancient Key"),
                   Has("Ancient Key", 3))
    world.set_rule(world.get_location("Ancient C3 - Ancient Key"),
                   Has("Ancient Key", 3))
    world.set_rule(world.get_location("Ancient C1 - Ancient Key"),
                   Has("Star Piece")
                   & Has("Ancient Key", 6))

    world.set_rule(world.get_location("Ancient C0 - Star Piece"),
                   Has("Ancient Key", 6))'''

    # Locksanity
    if world.options.enable_locksanity:

        world.set_rule(world.get_location("Ancient A1 - 3x Lock"),
                       (CanReachRegion("Ruby Sea")
                        | CanReachRegion("Sapphire Sea"))
                       & Has("Ancient Key", 17))

        world.set_rule(world.get_location("Ancient B3 - Lock"),
                       Has("Ancient Key", 1))

        world.set_rule(world.get_location("Ancient A3 - Lock"),
                       Has("Ancient Key", 2))

        world.set_rule(world.get_location("Ancient B2 - Lock"),
                       Has("Ancient Key", 3))

        world.set_rule(world.get_location("Ancient C2 - 3x Lock"),
                       Has("Ancient Key", 6))

        world.set_rule(world.get_location("Ancient C1 - Star Lock 1"),
                       Has("Star Piece")
                       & Has("Ancient Key", 6))

        world.set_rule(world.get_location("Ancient B1 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

    if world.options.enable_snakesanity:
        world.set_rule(world.get_location("Ancient B3 - Snakeblock"),
                       Has("Ancient Key"))

        world.set_rule(world.get_location("Ancient B2 - W - Snakeblock"),
                       Has("Ancient Key"))

        world.set_rule(world.get_location("Ancient A3 - Snakeblock"),
                       Has("Ancient Key", 2))

        world.set_rule(world.get_location("Ancient B2 - E - Snakeblock"),
                       Has("Ancient Key", 3))
        world.set_rule(world.get_location("Ancient C2 - E - Snakeblock"),
                       Has("Ancient Key", 3))
        world.set_rule(world.get_location("Ancient C2 - S - Snakeblock"),
                       Has("Ancient Key", 3))
        world.set_rule(world.get_location("Ancient C2 - W - Snakeblock"),
                       Has("Ancient Key", 3))
        world.set_rule(world.get_location("Ancient C3 - Snakeblock"),
                       Has("Ancient Key", 3))

        world.set_rule(world.get_location("Ancient A1 - Snakeblock"),
                       CanReachRegion("Obsidian Sea"))

    # Secretsanity
    if world.options.secretsanity:
        world.set_rule(world.get_location("Ancient A1 - Discover Secret"),
                       (CanReachRegion("Ruby Sea")
                        | CanReachRegion("Sapphire Sea"))
                       & Has("Ancient Key", 17))


def set_rolling_rocks(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Rolling A0 - Topaz"),
                   Has("Star Piece", 7)
                   & Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Rolling A1 - Obsidian"),
                   Has("Star Piece", 7)
                   & Has("Gopher Gloves")
                   & Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Rolling A0 - Star Piece"),
                   Has("Star Piece", 7)
                   & (Has("Awaken Earth Elementals") | Has("Frog Flippers")))


    world.set_rule(world.get_location("Rolling B1 - Star Piece"),
                   Has("Ancient Key", 14))

    world.set_rule(world.get_location("Rolling B0 - Star Piece"),
                   Has("Gopher Gloves"))
    
    world.set_rule(world.get_location("Rolling B0 - Big Bell Star Piece"),
                   Has("Big Bell Hit - Rolling"))



    # Locksanity
    if world.options.enable_locksanity:

        world.set_rule(world.get_location("Rolling B1 - 3x Lock"),
                       Has("Ancient Key", 14))

        world.set_rule(world.get_location("Rolling A0 - Star Lock 7"),
                       Has("Star Piece", 7))


    if world.options.enable_snakesanity:
        pass

    # Secretsanity
    if world.options.secretsanity:
        world.set_rule(world.get_location("Rolling A0 - Discover Secret"),
                       Has("Star Piece", 7)
                       & Has("Gopher Gloves"))


def set_sunken_island(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Sunken B1 - Big Bell Rung"),
                   Has("Ancient Rune Stone"))

    world.set_rule(world.get_location("Sunken B0 - Sapphire"),
                   Has("Star Piece", 21)
                   & Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Sunken B0 - Star Piece"),
                   Has("Star Piece", 21)
                   & Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Sunken A1 - Star Piece"),
                   Has("Ancient Key", 34)
                   & Has("Ancient Rune Stone"))

    world.set_rule(world.get_location("Sunken A0 - Obsidian"),
                   Has("Frog Flippers"))
    
    world.set_rule(world.get_location("Sunken B1 - Big Bell Star Piece"),
                   Has("Big Bell Hit - Sunken"))

    # Locksanity
    if world.options.enable_locksanity:
        world.set_rule(world.get_location("Sunken A1 - 3x Lock"),
                       Has("Ancient Key", 34)
                       & Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Sunken B0 - Star Lock 21"),
                       Has("Star Piece", 21))

        world.set_rule(world.get_location("Sunken A0 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Sunken B1 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))


def set_aggro_crag(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Aggro A1 - Big Bell Rung"),
                   Has("Ancient Rune Stone"))

    world.set_rule(world.get_location("Aggro B1 - Ruby"),
                   Has("Star Piece", 35)
                   & Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Aggro B1 - Star Piece"),
                   Has("Star Piece", 35)
                   & Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Aggro B0 - Obsidian"),
                   Has("Ancient Rune Stone")
                   & Has("Star Piece", 35)
                   & Has("Awaken Fire Elementals")
                   & Has("Salamander Shirt"))

    world.set_rule(world.get_location("Aggro A1 - Star Piece"),
                   Has("Star Piece", 35)
                   & Has("Awaken Fire Elementals")
                   & Has("Ancient Rune Stone"))
    
    world.set_rule(world.get_location("Aggro A1 - Big Bell Star Piece"),
                   Has("Big Bell Hit - Aggro"))

    # Locksanity
    if world.options.enable_locksanity:

        world.set_rule(world.get_location("Aggro A1 - 3x Lock"),
                       Has("Star Piece", 35)
                       & Has("Awaken Fire Elementals")
                       & Has("Ancient Rune Stone")
                       & Has("Ancient Key", 42))

        world.set_rule(world.get_location("Aggro B0 - Star Lock 35"),
                       Has("Star Piece", 35))

        world.set_rule(world.get_location("Aggro B1 - Ancient Rune Lock"),
                       Has("Star Piece", 35)
                       & Has("Awaken Fire Elementals")
                       & Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Aggro A1 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

    # Snakesanity
    if world.options.enable_snakesanity:
        world.set_rule(world.get_location("Aggro B1 - E - Snakeblock"),
                       Has("Star Piece", 35))

        world.set_rule(world.get_location("Aggro B1 - W - Snakeblock"),
                       Has("Star Piece", 35)
                       & Has("Awaken Fire Elementals")
                       & Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Aggro B0 - W - Snakeblock"),
                       Has("Star Piece", 35)
                       & Has("Awaken Fire Elementals")
                       & Has("Ancient Rune Stone")
                       & Has("Salamander Shirt"))

    # Secretsanity
    if world.options.secretsanity:
        world.set_rule(world.get_location("Aggro A0 - W - Discover Secret"),
                       Has("Ancient Rune Stone")
                       & Has("Star Piece", 35)
                       & Has("Awaken Fire Elementals")
                       & Has("Salamander Shirt"))

        world.set_rule(world.get_location("Aggro A0 - E - Discover Secret"),
                       Has("Ancient Rune Stone")
                       & Has("Star Piece", 35)
                       & Has("Awaken Fire Elementals")
                       & Has("Salamander Shirt"))


def set_sea_nunatak(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Nunatak A1 - Big Bell Rung"),
                   Has("Ancient Rune Stone"))

    world.set_rule(world.get_location("Nunatak A1 - Ancient Key"),
                   Has("Ancient Rune Stone")
                   & Has("Awaken Wind Elementals")
                   & Has("Star Piece", 49))

    world.set_rule(world.get_location("Nunatak B0 - Diamond"),
                   Has("Awaken Wind Elementals")
                   & Has("Star Piece", 49))

    world.set_rule(world.get_location("Nunatak B0 - Star Piece"),
                   Has("Awaken Wind Elementals")
                   & Has("Star Piece", 49))

    world.set_rule(world.get_location("Nunatak A0 - Star Piece"),
                   Has("Ancient Rune Stone")
                   & Has("Ancient Key", 26))

    world.set_rule(world.get_location("Nunatak B1 - Obsidian"),
                   Has("Awaken Wind Elementals")
                   & Has("Star Piece", 49)
                   & Has("Kite Cloak"))
    
    world.set_rule(world.get_location("Nunatak A1 - Big Bell Star Piece"),
                   Has("Big Bell Hit - Nunatak"))

    # Locksanity
    if world.options.enable_locksanity:

        world.set_rule(world.get_location("Nunatak A0 - 3x Lock"),
                       Has("Ancient Rune Stone")
                       & Has("Ancient Key", 26))

        world.set_rule(world.get_location("Nunatak B0 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Nunatak B0 - Star Lock 49"),
                       Has("Star Piece", 49))

    # Snakesanity
    if world.options.enable_snakesanity:
        world.set_rule(world.get_location("Nunatak A1 - Snakeblock"),
                       Has("Ancient Rune Stone")
                       & Has("Awaken Wind Elementals")
                       & Has("Star Piece", 49))

    # Secretsanity
    if world.options.secretsanity:
        world.set_rule(world.get_location("Nunatak B0 - E - Discover Secret"),
                       Has("Awaken Wind Elementals")
                       & Has("Star Piece", 49)
                       & Has("Kite Cloak"))

        world.set_rule(world.get_location("Nunatak B0 - SE - Discover Secret"),
                       Has("Awaken Wind Elementals")
                       & Has("Star Piece", 49)
                       & Has("Kite Cloak"))

        world.set_rule(world.get_location("Nunatak B0 - CW - Discover Secret"),
                       Has("Ancient Rune Stone")
                       & Has("Awaken Wind Elementals")
                       & Has("Star Piece", 49))
        world.set_rule(world.get_location("Nunatak B0 - W - Discover Secret"),
                       Has("Ancient Rune Stone")
                       & Has("Awaken Wind Elementals")
                       & Has("Star Piece", 49))


def set_locked(world: "IslesOfSeaAndSkyWorld"):
    world.set_rule(world.get_location("Locked A0 - Ancient Rune Stone"),
                   (CanReachRegion("Ruby Sea")
                    | CanReachRegion("Sapphire Sea"))
                   & Has("Ancient Key", 23))  # Makes this 'unreachable'

    world.set_rule(world.get_location("Locked A0 - Star Piece"),
                   Has("Ancient Rune Stone"))

    # Locksanity
    if world.options.enable_locksanity:

        world.set_rule(world.get_location("Locked A0 - 6x Lock"),
                       (CanReachRegion("Ruby Sea")
                        | CanReachRegion("Sapphire Sea"))
                       & Has("Ancient Key", 23))

        world.set_rule(world.get_location("Locked A0 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

    # Snakesanity
    if world.options.enable_snakesanity:
        world.set_rule(world.get_location("Locked A0 - E - Snakeblock"),
                       (CanReachRegion("Ruby Sea")
                        | CanReachRegion("Sapphire Sea"))
                       & Has("Ancient Key", 23))
        world.set_rule(world.get_location("Locked A0 - C - Snakeblock"),
                       (CanReachRegion("Ruby Sea")
                        | CanReachRegion("Sapphire Sea"))
                       & Has("Ancient Key", 23))
        world.set_rule(world.get_location("Locked A0 - W - Snakeblock"),
                       (CanReachRegion("Ruby Sea")
                        | CanReachRegion("Sapphire Sea"))
                       & Has("Ancient Key", 23))


def set_star_tropic(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Tropic A1 - Ancient Key"),
                   Has("Ancient Rune Stone"))

    world.set_rule(world.get_location("Tropic A1 - Topaz"),
                   Has("Ancient Rune Stone")
                   & Has("Gopher Gloves")
                   & Has("Frog Flippers")
                   & Has("Salamander Shirt")
                   & Has("Kite Cloak"))

    world.set_rule(world.get_location("Tropic A1 - Sapphire"),
                   Has("Ancient Rune Stone")
                   & Has("Gopher Gloves")
                   & Has("Frog Flippers")
                   & Has("Salamander Shirt")
                   & Has("Kite Cloak"))

    world.set_rule(world.get_location("Tropic A1 - Ruby"),
                   Has("Ancient Rune Stone")
                   & Has("Gopher Gloves")
                   & Has("Frog Flippers")
                   & Has("Salamander Shirt")
                   & Has("Kite Cloak"))

    world.set_rule(world.get_location("Tropic A1 - Diamond"),
                   Has("Ancient Rune Stone")
                   & Has("Gopher Gloves")
                   & Has("Frog Flippers")
                   & Has("Salamander Shirt")
                   & Has("Kite Cloak"))

    world.set_rule(world.get_location("Tropic A1 - 1 - Star Piece"),
                   Has("Ancient Rune Stone")
                   & Has("Gopher Gloves"))

    world.set_rule(world.get_location("Tropic A1 - 2 - Star Piece"),
                   Has("Ancient Rune Stone")
                   & Has("Gopher Gloves")
                   & Has("Salamander Shirt"))

    world.set_rule(world.get_location("Tropic A1 - 3 - Star Piece"),
                   Has("Ancient Rune Stone")
                   & Has("Gopher Gloves")
                   & Has("Frog Flippers")
                   & Has("Salamander Shirt"))

    world.set_rule(world.get_location("Tropic A1 - 4 - Star Piece"),
                   Has("Ancient Rune Stone")
                   & Has("Gopher Gloves")
                   & Has("Frog Flippers")
                   & Has("Salamander Shirt")
                   & Has("Kite Cloak"))

    world.set_rule(world.get_location("Tropic B0 - S - Star Piece"),
                   Has("Ancient Rune Stone")
                   | (CanReachRegion("Lost Sea")
                      & Has("Kite Cloak")))

    world.set_rule(world.get_location("Tropic B0 - N - Star Piece"),
                   Has("Obsidian Rune Stone")
                   & Has("Kite Cloak"))


    # Locksanity
    if world.options.enable_locksanity:

        world.set_rule(world.get_location("Tropic A1 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Tropic B0 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Tropic B0 - Obsidian Rune Lock"),
                       Has("Obsidian Rune Stone")
                       & Has("Kite Cloak"))

    # Snakesanity
    if world.options.enable_snakesanity:
        world.set_rule(world.get_location("Tropic A0 - W - Snakeblock"),
                       Has("Kite Cloak"))
        world.set_rule(world.get_location("Tropic A0 - C - Snakeblock"),
                       Has("Kite Cloak"))
        world.set_rule(world.get_location("Tropic A0 - E - Snakeblock"),
                       Has("Kite Cloak"))
        world.set_rule(world.get_location("Tropic B0 - N - Snakeblock"),
                       Has("Kite Cloak"))
        world.set_rule(world.get_location("Tropic B0 - S - Snakeblock"),
                       Has("Kite Cloak"))

    # Secretsanity
    if world.options.secretsanity:
        world.set_rule(world.get_location("Tropic A0 - Discover Secret"),
                       Has("Kite Cloak"))


def set_shoal(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Shoal A0 - Star Viewing Orb"),
                   Has("Ancient Rune Stone"))

    world.set_rule(world.get_location("Shoal A0 - Star Piece"),
                   Has("Ancient Rune Stone")
                   & Has("Frog Flippers")
                   & Has("Kite Cloak"))

    # Locksanity
    if world.options.enable_locksanity:

        world.set_rule(world.get_location("Shoal A0 - Ancient Rune Lock"),
                       Has("Ancient Rune Stone"))

    # Snakesanity
    if world.options.enable_snakesanity:

        world.set_rule(world.get_location("Shoal A0 - Snakeblock"),
                       Has("Ancient Rune Stone")
                       & Has("Kite Cloak"))

    if world.options.secretsanity:
        world.set_rule(world.get_location("Shoal A0 - E - Discover Secret"),
                       Has("Ancient Rune Stone"))

        world.set_rule(world.get_location("Shoal A0 - SE - Discover Secret"),
                       Has("Ancient Rune Stone")
                       & Has("Frog Flippers")
                       & Has("Kite Cloak"))


def set_lost_landing(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Lost A1 - Obsidian"),
                   Has("Star Piece", 30)
                   & Has("Frog Flippers"))

    world.set_rule(world.get_location("Lost B1 - Star Piece"),
                   Has("Star Piece", 30))

    # Locksanity
    if world.options.enable_locksanity:

        world.set_rule(world.get_location("Lost A1 - Lock"),
                       CanReachRegion("Lost Sea")
                       & Has("Frog Flippers")
                       & Has("Ancient Key", 48))

        world.set_rule(world.get_location("Lost B0 - Star Lock 30"),
                       Has("Star Piece", 30))

    # Snakesanity
    if world.options.enable_snakesanity:
        world.set_rule(world.get_location("Lost B1 - Snakeblock"),
                       Has("Star Piece", 30))

    # Secretsanity
    if world.options.secretsanity:
        world.set_rule(world.get_location("Lost B1 - CS - Discover Secret"),
                       CanReachRegion("Lost Sea")
                       & Has("Frog Flippers"))

        world.set_rule(world.get_location("Lost B1 - W - Discover Secret"),
                       CanReachRegion("Lost Sea")
                       & Has("Frog Flippers"))


def set_serpent_stacks(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Serpent A1 - Obsidian Rune Stone"),
                   Has("Topaz Rune Stone")
                   & Has("Sapphire Rune Stone")
                   & Has("Ruby Rune Stone")
                   & Has("Diamond Rune Stone"))

    world.set_rule(world.get_location("Serpent A1 - Obsidian"),
                   Has("Topaz Rune Stone")
                   & Has("Sapphire Rune Stone")
                   & Has("Ruby Rune Stone")
                   & Has("Diamond Rune Stone"))

    world.set_rule(world.get_location("Serpent A1 - W - Star Piece"),
                   Has("Activate Shadow Blocks")
                   & Has("Topaz Rune Stone")
                   & Has("Sapphire Rune Stone")
                   & Has("Ruby Rune Stone")
                   & Has("Diamond Rune Stone"))

    world.set_rule(world.get_location("Serpent A1 - N - Star Piece"),
                   Has("Activate Shadow Blocks")
                   & Has("Topaz Rune Stone")
                   & Has("Sapphire Rune Stone")
                   & Has("Ruby Rune Stone")
                   & Has("Diamond Rune Stone"))

    world.set_rule(world.get_location("Serpent A2 - Star Piece"),
                   Has("Activate Shadow Blocks"))

    world.set_rule(world.get_location("Serpent A3 - Star Piece"),
                   Has("Kite Cloak"))

    world.set_rule(world.get_location("Serpent A4 - N - Star Piece"),
                   Has("Activate Shadow Blocks")
                   & Has("Awaken Earth Elementals"))
    world.set_rule(world.get_location("Serpent A4 - NW - Star Piece"),
                   Has("Activate Shadow Blocks")
                   & Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Serpent A6 - W - Star Piece"),
                   Has("Activate Shadow Blocks")
                   & Has("Awaken Earth Elementals")
                   & Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Serpent A6 - E - Star Piece"),
                   Has("Activate Shadow Blocks")
                   & Has("Awaken Earth Elementals")
                   & Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Serpent A7 - W - Star Piece"),
                   Has("Activate Shadow Blocks")
                   & Has("Awaken Earth Elementals")
                   & Has("Awaken Water Elementals")
                   & Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Serpent A7 - E - Star Piece"),
                   Has("Activate Shadow Blocks")
                   & Has("Awaken Earth Elementals")
                   & Has("Awaken Water Elementals")
                   & Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Serpent A8 - N - Star Piece"),
                   Has("Activate Shadow Blocks")
                   & Has("Awaken Earth Elementals")
                   & Has("Awaken Water Elementals")
                   & Has("Awaken Fire Elementals")
                   & Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Serpent A8 - S - Star Piece"),
                   Has("Activate Shadow Blocks")
                   & Has("Awaken Earth Elementals")
                   & Has("Awaken Water Elementals")
                   & Has("Awaken Fire Elementals")
                   & Has("Awaken Wind Elementals"))

    # Locksanity
    if world.options.enable_locksanity:

        world.set_rule(world.get_location("Serpent A2 - Elemental Rune Lock"),
                       Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone"))

        world.set_rule(world.get_location("Serpent A1 - N - Obsidian Rune Lock"),
                       Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone"))

        world.set_rule(world.get_location("Serpent A1 - W - Obsidian Rune Lock"),
                       Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone"))

        world.set_rule(world.get_location("Serpent A1 - E - Obsidian Rune Lock"),
                       Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone")
                       & Has("Activate Shadow Blocks"))

    # Snakesanity
    if world.options.enable_snakesanity:
        world.set_rule(world.get_location("Serpent A1 - C - Snakeblock"),
                       Has("Activate Shadow Blocks")
                       & Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone"))
        world.set_rule(world.get_location("Serpent A1 - CE - Snakeblock"),
                       Has("Activate Shadow Blocks")
                       & Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone"))
        world.set_rule(world.get_location("Serpent A1 - E - Snakeblock"),
                       Has("Activate Shadow Blocks")
                       & Has("Topaz Rune Stone")
                       & Has("Sapphire Rune Stone")
                       & Has("Ruby Rune Stone")
                       & Has("Diamond Rune Stone"))
        world.set_rule(world.get_location("Serpent A6 - SW - Snakeblock"),
                       Has("Activate Shadow Blocks")
                       & Has("Awaken Earth Elementals")
                       & Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Serpent A6 - NW - Snakeblock"),
                       Has("Activate Shadow Blocks")
                       & Has("Awaken Earth Elementals")
                       & Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Serpent A6 - C - Snakeblock"),
                       Has("Activate Shadow Blocks")
                       & Has("Awaken Earth Elementals")
                       & Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Serpent A6 - E - Snakeblock"),
                       Has("Activate Shadow Blocks")
                       & Has("Awaken Earth Elementals")
                       & Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Serpent A8 - Snakeblock"),
                       Has("Activate Shadow Blocks")
                       & Has("Awaken Earth Elementals")
                       & Has("Awaken Water Elementals")
                       & Has("Awaken Fire Elementals")
                       & Has("Awaken Wind Elementals"))


def set_stony_cliffs(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Stone Dungeon A1 - Gold Stone Tablet"),
                   Has("Topaz Rune Stone")
                   & Has("Star Piece", 20)
                   & Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Stone E3 - Blue Stone Tablet"),
                   Has("Star Piece", 20))

    world.set_rule(world.get_location("Stone C0 - Ancient Key"),
                   Has("Awaken Earth Elementals"))
    
    world.set_rule(world.get_location("Stone E2 - Ancient Key"),
                   Has("Ruby Rune Stone"))

    world.set_rule(world.get_location("Stone B4 - Ancient Key"),
                   Has("Awaken Earth Elementals")
                   & Has("Gopher Gloves")
                   & Has("Star Piece", 15))
    
    world.set_rule(world.get_location("Stone D3 - Ancient Key"),
                   Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Stone Dungeon C1 - Ancient Key"),
                   Has("Gopher Gloves")
                   & (CanReachRegion("Stony Cliffs NW")
                      | (CanReachRegion("Stony Cliffs Post-Rune")
                         & Has("Topaz Rune Stone"))))

    world.set_rule(world.get_location("Stone Dungeon D0 - Ancient Key"),
                   Has("Gopher Gloves"))

    world.set_rule(world.get_location("Stone Dungeon B1 - Ancient Key"),
                   Has("Gopher Gloves"))

    world.set_rule(world.get_location("Stone B0 - NW1 - Ancient Key"),
                   Has("Awaken Earth Elementals"))
    world.set_rule(world.get_location("Stone B0 - NW2 - Ancient Key"),
                   Has("Awaken Earth Elementals"))
    world.set_rule(world.get_location("Stone B0 - NW3 - Ancient Key"),
                   Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Stone Dungeon D2 - Ancient Key"),
                   Has("Awaken Earth Elementals"))


    world.set_rule(world.get_location("Stone Dungeon C1 - Topaz"),
                   Has("Gopher Gloves")
                   & (CanReachRegion("Stony Cliffs NW")
                      | (CanReachRegion("Stony Cliffs Post-Rune")
                         & Has("Topaz Rune Stone"))))

    world.set_rule(world.get_location("Stone C2 - E - Topaz"),
                   Has("Ancient Key", 7))

    world.set_rule(world.get_location("Stone C1 - Star Piece"),
                   Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Stone B2 - Star Piece"),
                   Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Stone B4 - Star Piece"),
                   Has("Awaken Earth Elementals")
                   & Has("Gopher Gloves")
                   & Has("Star Piece", 15))

    world.set_rule(world.get_location("Stone C4 - Star Piece"),
                   Has("Awaken Earth Elementals")
                   & Has("Gopher Gloves")
                   & Has("Star Piece", 15))

    world.set_rule(world.get_location("Stone C0 - Star Piece"),
                   Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Stone Dungeon E1 - Star Piece"),
                   Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Stone Dungeon E2 - Star Piece"),
                   (Has("Awaken Earth Elementals") | CanReachRegion("Stony Cliffs NW"))
                   & Has("Gopher Gloves")
                   & Has("Frog Flippers"))

    world.set_rule(world.get_location("Stone Dungeon E2 - Ancient Key"),
                   Has("Awaken Earth Elementals")
                   | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))

    world.set_rule(world.get_location("Stone Dungeon C3 - Star Piece"),
                   Has("Awaken Earth Elementals")
                   | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))

    world.set_rule(world.get_location("Stone Dungeon C1 - Star Piece"),
                   Has("Gopher Gloves")
                   & (CanReachRegion("Stony Cliffs NW")
                      | (CanReachRegion("Stony Cliffs Post-Rune")
                         & Has("Topaz Rune Stone"))))

    world.set_rule(world.get_location("Stone Dungeon B1 - Star Piece"),
                   Has("Gopher Gloves"))

    world.set_rule(world.get_location("Stone A1 - Star Piece"),
                   Has("Star Piece", 5))

    world.set_rule(world.get_location("Stone E1 - Star Piece"),
                   Has("Ancient Key", 10))
    
    world.set_rule(world.get_location("Stone D3 - N - Star Piece"),
                   Has("Star Piece", 20)
                   & Has("Awaken Earth Elementals")
                   & Has("Awaken Wind Elementals")
                   & Has("Gopher Gloves"))
    
    world.set_rule(world.get_location("Stone D3 - S - Star Piece"),
                   Has("Star Piece", 20)
                   & Has("Awaken Earth Elementals")
                   & Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Stone D1 - Music Puzzle Star Piece 1"),
                    Has("Awaken Earth Elementals")
                    & ( ([OptionFilter(EnableNotesanity, EnableNotesanity.option_false)] & Has("Topaz Rune Stone") & Has("Ancient Key", 11))
                        | ([OptionFilter(EnableNotesanity, EnableNotesanity.option_true)] & Has("Music Note", 6))))
    world.set_rule(world.get_location("Stone D1 - Music Puzzle Star Piece 2"),
                    Has("Awaken Earth Elementals")
                    & ( ([OptionFilter(EnableNotesanity, EnableNotesanity.option_false)] & Has("Topaz Rune Stone") & Has("Ancient Key", 11))
                        | ([OptionFilter(EnableNotesanity, EnableNotesanity.option_true)] & Has("Music Note", 6))))
    world.set_rule(world.get_location("Stone D1 - Music Puzzle Star Piece 3"),
                    Has("Awaken Earth Elementals")
                    & ( ([OptionFilter(EnableNotesanity, EnableNotesanity.option_false)] & Has("Topaz Rune Stone") & Has("Ancient Key", 11))
                        | ([OptionFilter(EnableNotesanity, EnableNotesanity.option_true)] & Has("Music Note", 6))))
    
    world.set_rule(world.get_location("Stone A2 - Tablet Puzzle Star Piece"),
                    Has("Blue Stone Tablet")
                    & Has("Gold Stone Tablet"))
    world.set_rule(world.get_location("Stone A2 - Ancient Key"),
                   Has("Blue Stone Tablet")
                   & Has("Gold Stone Tablet"))
    world.set_rule(world.get_location("Stone A2 - Obsidian"),
                   Has("Blue Stone Tablet")
                   & Has("Gold Stone Tablet"))

    world.set_rule(world.get_location("Stone Dungeon C2 - Open Topaz Door"),
                   Has("Awaken Earth Elementals"))

    world.set_rule(world.get_location("Stone Dungeon E1 - Tablet Puzzle Clue"),
                   (Has("Awaken Earth Elementals") & Has("Topaz Rune Stone"))
                   | Has("Kite Cloak"))

    # Notesanity
    if world.options.enable_notesanity:
        world.set_rule(world.get_location("Stone D1 - Music Note"),
                       Has("Awaken Earth Elementals"))

    # Locksanity
    if world.options.enable_locksanity:

        world.set_rule(world.get_location("Stone C2 - Lock"),
                       Has("Ancient Key", 7))

        world.set_rule(world.get_location("Stone E1 - 3x Lock"),
                       Has("Ancient Key", 10))

        world.set_rule(world.get_location("Stone B1 - Lock"),
                       Has("Ancient Key", 11))

        world.set_rule(world.get_location("Stone A1 - Star Lock 5"),
                       Has("Star Piece", 5))

        world.set_rule(world.get_location("Stone C4 - Star Lock 15"),
                       Has("Star Piece", 15)
                       & Has("Awaken Earth Elementals"))

        world.set_rule(world.get_location("Stone E3 - Star Lock 20"),
                       Has("Star Piece", 20))

        world.set_rule(world.get_location("Stone Dungeon A1 - Star Lock 20"),
                       Has("Star Piece", 20)
                       & Has("Gopher Gloves"))

    # Snakesanity
    if world.options.enable_snakesanity:
        world.set_rule(world.get_location("Stone C1 - Snakeblock"),
                       Has("Awaken Earth Elementals"))
        world.set_rule(world.get_location("Stone D1 - Snakeblock"),
                       Has("Awaken Earth Elementals"))
        world.set_rule(world.get_location("Stone E1 - E - Snakeblock"),
                       Has("Awaken Earth Elementals"))
        world.set_rule(world.get_location("Stone C4 - Snakeblock"),
                       Has("Awaken Earth Elementals"))
        world.set_rule(world.get_location("Stone Dungeon C4 - Snakeblock"),
                       Has("Awaken Earth Elementals"))
        world.set_rule(world.get_location("Stone Dungeon C3 - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon B2 - E - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D2 - E - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D2 - CE - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D2 - W - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D2 - CW - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D1 - W - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D1 - CS - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon D1 - E - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))
        world.set_rule(world.get_location("Stone Dungeon E1 - Snakeblock"),
                       Has("Awaken Earth Elementals"))
        world.set_rule(world.get_location("Stone Dungeon E2 - Snakeblock"),
                       Has("Awaken Earth Elementals")
                       | (CanReachRegion("Stony Cliffs NW") & Has("Gopher Gloves")))


        world.set_rule(world.get_location("Stone Dungeon C1 - Snakeblock"),
                       Has("Gopher Gloves")
                       & (CanReachRegion("Stony Cliffs NW")
                          | (CanReachRegion("Stony Cliffs Post-Rune")
                             & Has("Topaz Rune Stone"))))

        world.set_rule(world.get_location("Stone B4 - Snakeblock"),
                       Has("Star Piece", 15)
                       & Has("Gopher Gloves"))
        world.set_rule(world.get_location("Stone A4 - E - Snakeblock"),
                       Has("Star Piece", 15)
                       & Has("Gopher Gloves")
                       & Has("Awaken Earth Elementals"))

    # Secretsanity
    if world.options.secretsanity:
        pass


def set_tidal_reef(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Water A0 - S - Ancient Key"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water A2 - Ancient Key"),
                   Has("Frog Flippers")
                   & Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water B3 - Ancient Key"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water C3 - W - Ancient Key"),
                   Has("Diamond Rune Stone"))

    world.set_rule(world.get_location("Water C3 - NE1 - Ancient Key"),
                   Has("Frog Flippers")
                   & Has("Awaken Water Elementals"))
    world.set_rule(world.get_location("Water C3 - NE2 - Ancient Key"),
                   Has("Frog Flippers")
                   & Has("Awaken Water Elementals"))
    world.set_rule(world.get_location("Water C3 - NE3 - Ancient Key"),
                   Has("Frog Flippers")
                   & Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water D1 - Ancient Key"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water D0 - Ancient Key"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water C0 - Ancient Key"),
                   Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water D2 - Ancient Key"),
                   Has("Frog Flippers")
                   & Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water C2 - N - Sapphire"),
                   Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water A1 - Sapphire"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water C0 - Star Piece"),
                   Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water C2 - Star Piece"),
                   Has("Frog Flippers") & Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water D2 - Star Piece"),
                   Has("Frog Flippers")
                   & Has("Salamander Shirt"))

    world.set_rule(world.get_location("Water D3 - Star Piece"),
                   Has("Frog Flippers")
                   & Has("Awaken Water Elementals"))

    world.set_rule(world.get_location("Water E0 - W - Star Piece"),
                   Has("Awaken Water Elementals")
                   | Has("Kite Cloak"))

    world.set_rule(world.get_location("Water E0 - E - Star Piece"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water E2 - Star Piece"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water B1 - Star Piece"),
                   Has("Awaken Water Elementals")
                   & Has("Frog Flippers"))

    world.set_rule(world.get_location("Water A2 - N - Star Piece"),
                   Has("Awaken Water Elementals")
                   & Has("Frog Flippers")
                   & Has("Star Piece", 30))

    world.set_rule(world.get_location("Water A2 - S - Star Piece"),
                   Has("Awaken Water Elementals")
                   & Has("Frog Flippers")
                   & Has("Star Piece", 30))

    world.set_rule(world.get_location("Water A4 - Star Piece"),
                   Has("Frog Flippers"))

    world.set_rule(world.get_location("Water C1 - W - Star Piece"),
                   Has("Ancient Key", 32))
    
    world.set_rule(world.get_location("Water E3 - NE - Star Piece"),
                   Has("Awaken Water Elementals")
                   & Has("Awaken Earth Elementals"))
    world.set_rule(world.get_location("Water E3 - SW - Star Piece"),
                   Has("Awaken Water Elementals")
                   & Has("Awaken Earth Elementals"))
    
    world.set_rule(world.get_location("Water B0 - Music Puzzle Star Piece 1"),
                   Has("Awaken Water Elementals")
                   & ([OptionFilter(EnableNotesanity, EnableNotesanity.option_false)]| Has("Music Note", 12)))
    world.set_rule(world.get_location("Water B0 - Music Puzzle Star Piece 2"),
                   Has("Awaken Water Elementals")
                   & ([OptionFilter(EnableNotesanity, EnableNotesanity.option_false)]| Has("Music Note", 12)))
    world.set_rule(world.get_location("Water B0 - Music Puzzle Star Piece 3"),
                   Has("Awaken Water Elementals")
                   & ([OptionFilter(EnableNotesanity, EnableNotesanity.option_false)]| Has("Music Note", 12)))
    
    world.set_rule(world.get_location("Water C4 - Shell Puzzle Star Piece"),
                   Has("Frog Flippers"))

    # IncludeShells
    if world.options.include_seashells:

        world.set_rule(world.get_location("Water B2 - Shell"),
                       Has("Frog Flippers"))

        world.set_rule(world.get_location("Water B3 - Shell"),
                       Has("Frog Flippers")
                       | Has("Phoenix Flute")
                       | Has("Sapphire Rune Stone"))


        world.set_rule(world.get_location("Water B0 - Shell"),
                       Has("Awaken Water Elementals"))

        world.set_rule(world.get_location("Water D1 - Shell"),
                       Has("Frog Flippers"))

        world.set_rule(world.get_location("Water A4 - Shell"),
                       Has("Frog Flippers"))

        world.set_rule(world.get_location("Water D0 - Shell"),
                       Has("Frog Flippers"))

        world.set_rule(world.get_location("Water A2 - Shell"),
                       Has("Frog Flippers"))

        world.set_rule(world.get_location("Water A3 - Shell"),
                       Has("Frog Flippers")
                       | Has("Sapphire Rune Stone"))

    # Locksanity
    if world.options.enable_locksanity:
        world.set_rule(world.get_location("Water B2 - Lock"),
                       Has("Ancient Key", 29))

        world.set_rule(world.get_location("Water C1 - 3x Lock"),
                       Has("Ancient Key", 32))

        world.set_rule(world.get_location("Water D3 - Lock"),
                       Has("Ancient Key", 33))

        world.set_rule(world.get_location("Water A2 - Star Lock 30"),
                       Has("Frog Flippers")
                       & Has("Awaken Water Elementals"))

    # Snakesanity
    if world.options.enable_snakesanity:
        world.set_rule(world.get_location("Water B0 - E - Snakeblock"),
                       Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Water B0 - C - Snakeblock"),
                       Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Water B1 - C - Snakeblock"),
                       Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Water B1 - SE - Snakeblock"),
                       Has("Awaken Water Elementals") | Has("Kite Cloak"))


        world.set_rule(world.get_location("Water D2 - C - Snakeblock"),
                       Has("Frog Flippers"))
        world.set_rule(world.get_location("Water D2 - E - Snakeblock"),
                       Has("Frog Flippers"))
        world.set_rule(world.get_location("Water D3 - Snakeblock"),
                       Has("Awaken Water Elementals"))
        world.set_rule(world.get_location("Water E1 - W - Snakeblock"),
                       Has("Frog Flippers"))
        world.set_rule(world.get_location("Water E1 - E - Snakeblock"),
                       Has("Frog Flippers"))
        world.set_rule(world.get_location("Water E2 - E - Snakeblock"),
                       Has("Frog Flippers"))
        world.set_rule(world.get_location("Water A0 - S - Snakeblock"),
                       Has("Frog Flippers"))

        world.set_rule(world.get_location("Water A2 - Snakeblock"),
                       Has("Frog Flippers")
                       & Has("Awaken Water Elementals")
                       & Has("Star Piece", 30))

        world.set_rule(world.get_location("Water A3 - Snakeblock"),
                       Has("Frog Flippers")
                       & Has("Awaken Water Elementals")
                       & Has("Star Piece", 30))


def set_raging_volcano(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Fire A2 - S - Ancient Key"),
                   Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire B4 - Ancient Key"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire A1 - SW - Ancient Key"),
                   Has("Topaz Rune Stone"))
    
    world.set_rule(world.get_location("Fire A1 - SE - Ancient Key"),
                   Has("Salamander Shirt"))
    

    world.set_rule(world.get_location("Fire B1 - N1 - Ancient Key"),
                   Has("Awaken Fire Elementals"))
    world.set_rule(world.get_location("Fire B1 - N2 - Ancient Key"),
                   Has("Awaken Fire Elementals"))
    world.set_rule(world.get_location("Fire B1 - N3 - Ancient Key"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire C1 - NE - Ancient Key"),
                   Has("Salamander Shirt")
                   & Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire C1 - Star Piece"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire C0 - Ancient Key"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire C1 - SW - Ancient Key"),
                   Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire C3 - Ancient Key"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire E0 - Obsidian"),
                   Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire B4 - Star Piece"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire C0 - Star Piece"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire D1 - N - Star Piece"),
                   Has("Awaken Fire Elementals"))
    world.set_rule(world.get_location("Fire D1 - S - Star Piece"),
                   Has("Ancient Key", 38))

    world.set_rule(world.get_location("Fire D3 - S - Star Piece"),
                   Has("Awaken Fire Elementals") & Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire D3 - W - Star Piece"),
                   Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Fire D4 - Star Piece"),
                   Has("Awaken Fire Elementals")
                   & Has("Salamander Shirt")
                   & Has("Kite Cloak"));

    world.set_rule(world.get_location("Fire E1 - E - Star Piece"),
                   Has("Awaken Fire Elementals") & Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire E1 - W - Star Piece"),
                   Has("Awaken Fire Elementals") & Has("Salamander Shirt"))

    world.set_rule(world.get_location("Fire E0 - Star Piece"),
                   Has("Salamander Shirt"))
    
    world.set_rule(world.get_location("Fire E3 - S - Star Piece"),
                   Has("Awaken Fire Elementals")
                   & Has("Awaken Water Elementals"))
    world.set_rule(world.get_location("Fire E3 - SE - Star Piece"),
                   Has("Awaken Fire Elementals")
                   & Has("Awaken Water Elementals"))
    
    world.set_rule(world.get_location("Fire B3 - Music Puzzle Star Piece 1"),
                   Has("Awaken Fire Elementals")
                   & ([OptionFilter(EnableNotesanity, EnableNotesanity.option_false)]| Has("Music Note", 18)))
    world.set_rule(world.get_location("Fire B3 - Music Puzzle Star Piece 2"),
                   Has("Awaken Fire Elementals")
                   & ([OptionFilter(EnableNotesanity, EnableNotesanity.option_false)]| Has("Music Note", 18)))
    world.set_rule(world.get_location("Fire B3 - Music Puzzle Star Piece 3"),
                   Has("Awaken Fire Elementals")
                   & ([OptionFilter(EnableNotesanity, EnableNotesanity.option_false)]| Has("Music Note", 18)))

    # Locksanity
    if world.options.enable_locksanity:
        world.set_rule(world.get_location("Fire D2 - Lock"),
                       Has("Ancient Key", 35))

        world.set_rule(world.get_location("Fire D2 - 3x Lock"),
                       Has("Ancient Key", 38))

        world.set_rule(world.get_location("Fire A3 - Lock"),
                       Has("Ancient Key", 39))

        world.set_rule(world.get_location("Fire E0 - 3x Lock (Fire)"),
                       Has("Fire Key", 3))

    # Snakesanity
    if world.options.enable_snakesanity:
        world.set_rule(world.get_location("Fire B4 - W - Snakeblock"),
                       Has("Awaken Fire Elementals"))
        world.set_rule(world.get_location("Fire B4 - E - Snakeblock"),
                       Has("Awaken Fire Elementals"))
        world.set_rule(world.get_location("Fire B3 - CW - Snakeblock"),
                       Has("Awaken Fire Elementals"))
        world.set_rule(world.get_location("Fire B3 - W - Snakeblock"),
                       Has("Awaken Fire Elementals"))
        world.set_rule(world.get_location("Fire B3 - CE - Snakeblock"),
                       Has("Awaken Fire Elementals"))
        world.set_rule(world.get_location("Fire C3 - E - Snakeblock"),
                       Has("Awaken Fire Elementals"))


        world.set_rule(world.get_location("Fire D1 - SE - Snakeblock"),
                       Has("Salamander Shirt"))
        world.set_rule(world.get_location("Fire D1 - SW - Snakeblock"),
                       Has("Ancient Key", 38))
        world.set_rule(world.get_location("Fire B1 - Snakeblock"),
                       Has("Salamander Shirt"))
        world.set_rule(world.get_location("Fire D3 - W - Snakeblock"),
                       Has("Salamander Shirt"))

        world.set_rule(world.get_location("Fire D3 - E - Snakeblock"),
                       Has("Awaken Fire Elementals"))
        world.set_rule(world.get_location("Fire D3 - SW - Snakeblock"),
                       Has("Awaken Fire Elementals"))

    # Secretsanity
    if world.options.secretsanity:
        world.set_rule(world.get_location("Fire C2 - Discover Secret"),
                       Has("Salamander Shirt"))
        world.set_rule(world.get_location("Fire E1 - Discover Secret"),
                       Has("Salamander Shirt"))


def set_frozen_spire(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Wind D4 - NW1 - Ancient Key"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind D4 - NW2 - Ancient Key"),
                   Has("Awaken Wind Elementals"))
    world.set_rule(world.get_location("Wind D4 - NW3 - Ancient Key"),
                   Has("Awaken Wind Elementals"))
    
    world.set_rule(world.get_location("Wind D4 - E - Ancient Key"),
                   Has("Sapphire Rune Stone"))

    world.set_rule(world.get_location("Wind D4 - Star Piece"),
                   Has("Ancient Key", 45))

    world.set_rule(world.get_location("Wind D3 - Ancient Key"),
                   Has("Kite Cloak"))

    world.set_rule(world.get_location("Wind A3 - Ancient Key"),
                   Has("Kite Cloak") | Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Wind C2 - Ancient Key"),
                   Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Wind E2 - NE - Ancient Key"),
                   Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Wind E2 - S - Ancient Key"),
                   Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Wind E4 - E - Ancient Key"),
                   Has("Awaken Wind Elementals")
                   & Has("Kite Cloak"))

    world.set_rule(world.get_location("Wind E4 - SW - Ancient Key"),
                   Has("Awaken Wind Elementals")
                   & Has("Kite Cloak"))

    world.set_rule(world.get_location("Wind C3 - Diamond"),
                   Has("Awaken Wind Elementals")
                   & Has("Ancient Key", 46))
    world.set_rule(world.get_location("Wind D1 - E - Diamond"),
                   Has("Kite Cloak")
                   | Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Wind B3 - Star Piece"),
                   Has("Kite Cloak")
                   & Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Wind A3 - Star Piece"),
                   Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Wind B2 - N - Star Piece"),
                   Has("Awaken Wind Elementals")
                   | Has("Kite Cloak"))

    world.set_rule(world.get_location("Wind C2 - Star Piece"),
                   Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Wind D2 - Star Piece"),
                   Has("Kite Cloak"))

    world.set_rule(world.get_location("Wind E2 - Star Piece"),
                   Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Wind E4 - Star Piece"),
                   Has("Awaken Wind Elementals"))

    world.set_rule(world.get_location("Wind E1 - W - Star Piece"),
                   Has("Kite Cloak")
                   & Has("Gopher Gloves"))
    
    world.set_rule(world.get_location("Wind E1 - SE - Star Piece"),
                   Has("Awaken Wind Elementals")
                   & Has("Awaken Fire Elementals"))
    world.set_rule(world.get_location("Wind E1 - SW - Star Piece"),
                   Has("Awaken Wind Elementals")
                   & Has("Awaken Fire Elementals"))

    world.set_rule(world.get_location("Wind A0 - Star Piece"),
                   Has("Kite Cloak"))

    world.set_rule(world.get_location("Wind C3 - NE - Star Piece"),
                   Has("Awaken Wind Elementals"))
    
    world.set_rule(world.get_location("Wind B4 - Music Puzzle Star Piece 1"),
                   Has("Awaken Wind Elementals")
                   & ([OptionFilter(EnableNotesanity, EnableNotesanity.option_false)]| Has("Music Note", 24)))
    world.set_rule(world.get_location("Wind B4 - Music Puzzle Star Piece 2"),
                   Has("Awaken Wind Elementals")
                   & ([OptionFilter(EnableNotesanity, EnableNotesanity.option_false)]| Has("Music Note", 24)))
    world.set_rule(world.get_location("Wind B4 - Music Puzzle Star Piece 3"),
                   Has("Awaken Wind Elementals")
                   & ([OptionFilter(EnableNotesanity, EnableNotesanity.option_false)]| Has("Music Note", 24)))

    # Notesanity
    if world.options.enable_notesanity:
        world.set_rule(world.get_location("Wind A2 - Music Note"),
                       Has("Awaken Wind Elementals"))

        world.set_rule(world.get_location("Wind D3 - Music Note"),
                       Has("Awaken Wind Elementals"))

        world.set_rule(world.get_location("Wind E3 - Music Note"),
                       Has("Awaken Wind Elementals"))


    # Locksanity
    if world.options.enable_locksanity:
        world.set_rule(world.get_location("Wind D3 - 3x Lock"),
                       Has("Ancient Key", 45))

        world.set_rule(world.get_location("Wind C3 - Lock"),
                       Has("Ancient Key", 46)
                       & Has("Awaken Wind Elementals"))

        world.set_rule(world.get_location("Wind D1 - Lock"),
                       Has("Ancient Key", 47))

        world.set_rule(world.get_location("Wind A0 - Lock (Wind)"),
                       Has("Diamond Rune Stone"))  # Remove later when wind key item is fixed

    # Snakesanity
    if world.options.enable_snakesanity:
        world.set_rule(world.get_location("Wind A2 - SE - Snakeblock"),
                       Has("Awaken Wind Elementals"))
        world.set_rule(world.get_location("Wind E4 - Snakeblock"),
                       Has("Awaken Wind Elementals"))
        world.set_rule(world.get_location("Wind E3 - Snakeblock"),
                       Has("Awaken Wind Elementals"))
        world.set_rule(world.get_location("Wind C2 - Snakeblock"),
                       Has("Awaken Wind Elementals"))

        world.set_rule(world.get_location("Wind B3 - CE - Snakeblock"),
                       Has("Kite Cloak"))
        world.set_rule(world.get_location("Wind B3 - NE - Snakeblock"),
                       Has("Kite Cloak"))
        world.set_rule(world.get_location("Wind B2 - SW - Snakeblock"),
                       Has("Awaken Wind Elementals"))
        world.set_rule(world.get_location("Wind B4 - Snakeblock"),
                       Has("Kite Cloak"))

        world.set_rule(world.get_location("Wind E1 - Snakeblock"),
                       Has("Gopher Gloves")
                       & Has("Kite Cloak"))

        world.set_rule(world.get_location("Wind D4 - Snakeblock"),
                       Has("Ancient Key", 45))

    # Secretsanity
    if world.options.secretsanity:
        world.set_rule(world.get_location("Wind D1 - Discover Secret"),
                       Has("Kite Cloak")
                       & Has("Ancient Key", 47))


def set_beast_bridge(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Beast A0 - Phoenix Flute"),
                   CanReachRegion("Beast Bridge")
                   & Has("Big Bell Hit - Rolling")
                   & Has("Big Bell Hit - Sunken")
                   & Has("Big Bell Hit - Aggro")
                   & Has("Big Bell Hit - Nunatak"))

    world.set_rule(world.get_location("Beast A1 - Big Bell Stone"),
                   Has("Big Bell Hit - Rolling")
                   & Has("Big Bell Hit - Sunken")
                   & Has("Big Bell Hit - Aggro")
                   & Has("Big Bell Hit - Nunatak"))


def set_sanctum(world: "IslesOfSeaAndSkyWorld"):

    world.set_rule(world.get_location("Sanctum A2 - Topaz Shard Hit"),
                   Has("Ancient Key", 51))

    world.set_rule(world.get_location("Sanctum C2 - Sapphire Shard Hit"),
                   Has("Ancient Key", 54))

    world.set_rule(world.get_location("Sanctum A0 - Diamond Shard Hit"),
                   Has("Ancient Key", 57))

    world.set_rule(world.get_location("Sanctum C0 - Ruby Shard Hit"),
                   Has("Ancient Key", 60))


    # Locksanity
    if world.options.enable_locksanity:
        world.set_rule(world.get_location("Sanctum B2 - W - 3x Lock"),
                       Has("Ancient Key", 51))

        world.set_rule(world.get_location("Sanctum B2 - E - 3x Lock"),
                       Has("Ancient Key", 54))

        world.set_rule(world.get_location("Sanctum A1 - 3x Lock"),
                       Has("Ancient Key", 57))

        world.set_rule(world.get_location("Sanctum C1 - 3x Lock"),
                       Has("Ancient Key", 60))

    # Snakesanity
    if world.options.enable_snakesanity:
        world.set_rule(world.get_location("Sanctum A2 - S - Snakeblock"),
                       Has("Ancient Key", 51))
        world.set_rule(world.get_location("Sanctum A2 - C - Snakeblock"),
                       Has("Ancient Key", 51))
        world.set_rule(world.get_location("Sanctum A2 - W - Snakeblock"),
                       Has("Ancient Key", 51))

        world.set_rule(world.get_location("Sanctum C2 - E - Snakeblock"),
                       Has("Ancient Key", 54))
        world.set_rule(world.get_location("Sanctum C2 - W - Snakeblock"),
                       Has("Ancient Key", 54))

        world.set_rule(world.get_location("Sanctum A0 - E - Snakeblock"),
                       Has("Ancient Key", 57))
        world.set_rule(world.get_location("Sanctum A0 - CW - Snakeblock"),
                       Has("Ancient Key", 57))
        world.set_rule(world.get_location("Sanctum A0 - CE - Snakeblock"),
                       Has("Ancient Key", 57))
        world.set_rule(world.get_location("Sanctum A0 - W - Snakeblock"),
                       Has("Ancient Key", 57))

        world.set_rule(world.get_location("Sanctum C0 - W - Snakeblock"),
                       Has("Ancient Key", 60))
        world.set_rule(world.get_location("Sanctum C0 - CSW - Snakeblock"),
                       Has("Ancient Key", 60))
        world.set_rule(world.get_location("Sanctum C0 - CNW - Snakeblock"),
                       Has("Ancient Key", 60))
        world.set_rule(world.get_location("Sanctum C0 - CN - Snakeblock"),
                       Has("Ancient Key", 60))
        world.set_rule(world.get_location("Sanctum C0 - E - Snakeblock"),
                       Has("Ancient Key", 60))


def set_rechecks(world: "IslesOfSeaAndSkyWorld"):
    # Rechecks reachability later in the fill sweep, so that some unreachable locations can
    # be registered correctly.

    player = world.player
    multiworld = world.multiworld

    multiworld.register_indirect_condition(multiworld.get_region("Ruby Sea", player),
                                           multiworld.get_entrance("Ancient West Entrance", player))
    multiworld.register_indirect_condition(multiworld.get_region("Sapphire Sea", player),
                                           multiworld.get_entrance("Ancient West Entrance", player))

    multiworld.register_indirect_condition(multiworld.get_region("Obsidian Sea", player),
                                           multiworld.get_entrance("Ancient West Exit", player))

    multiworld.register_indirect_condition(multiworld.get_region("Ruby Sea", player),
                                           multiworld.get_entrance("Locked Entrance", player))
    multiworld.register_indirect_condition(multiworld.get_region("Sapphire Sea", player),
                                           multiworld.get_entrance("Locked Entrance", player))

    multiworld.register_indirect_condition(multiworld.get_region("Raging Volcano Post-Rune", player),
                                           multiworld.get_entrance("Raging NE Exit", player))


    multiworld.register_indirect_condition(multiworld.get_region("Lost Sea", player),
                                           multiworld.get_entrance("North Diamond Sea East Exit", player))

    multiworld.register_indirect_condition(multiworld.get_region("Lost Sea", player),
                                           multiworld.get_entrance("Star West Exit", player))

    multiworld.register_indirect_condition(multiworld.get_region("Lost Sea", player),
                                           multiworld.get_entrance("Star East Entrance", player))


    multiworld.register_indirect_condition(multiworld.get_region("Obsidian Sea", player),
                                           multiworld.get_entrance("Locked Entrance", player))
    multiworld.register_indirect_condition(multiworld.get_region("Obsidian Sea", player),
                                           multiworld.get_entrance("Ancient West Entrance", player))

    # Later ancient isle checks, and the Locked region
    multiworld.register_indirect_condition(multiworld.get_region("Frozen Spire", player),
                                           multiworld.get_entrance("Locked Entrance", player))
    multiworld.register_indirect_condition(multiworld.get_region("Frozen Spire", player),
                                           multiworld.get_entrance("Ancient West Entrance", player))

    multiworld.register_indirect_condition(multiworld.get_region("Frozen Spire", player),
                                           multiworld.get_entrance("Nunatak Entrance", player))
    multiworld.register_indirect_condition(multiworld.get_region("Frozen Spire", player),
                                           multiworld.get_entrance("Sunken Entrance", player))


def set_completion_rules(world: "IslesOfSeaAndSkyWorld"):

    route = world.options.route_required.current_key

    if route == "normal_ending":
        world.set_completion_rule(CanReachRegion("Sanctum Peak"))
    elif route == "secret_ending":
        world.set_completion_rule(CanReachRegion("Sanctum Peak")
                                  & Has("Star Piece", 109))
    elif route == "all_gems":
        world.set_completion_rule(Has("Topaz", 12)
                                  & Has("Sapphire", 12)
                                  & Has("Ruby", 12)
                                  & Has("Diamond", 12)
                                  & Has("Obsidian", 12))
