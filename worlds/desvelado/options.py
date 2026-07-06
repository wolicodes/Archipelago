from dataclasses import dataclass

from Options import Choice, OptionGroup, OptionSet, PerGameCommonOptions, Range, Toggle, DefaultOnToggle


class Goal(OptionSet):
    """
    The goal is generally to reach Bonnie's room, those are extra conditions you can stack on top of it.

    complete_bonnie: Need to collect all 15 Bonnie's bones
    map_clear: Need complete all the stages
    """
    display_name = "Goal"

    valid_keys = {"complete_bonnie", "map_clear"}
    default = frozenset()


class ShuffleBonniesBones(DefaultOnToggle):
    """
    Shuffle the bonus stage rewards in the item pool.
    """
    display_name = "Shuffle Bonnie's Bones"


# class RoomSanity(Toggle):
#     """
#     Completing any room for the first time will send an item.
#     This adds 160 locations, and that much filler.
#     """
#     display_name = "Room Sanity"


# class LocalFillers(Range):
#     """
#     Define the percentage of filler items that are guaranteed to be in your world.
#     """
#     display_name = "Local Fillers"
#
#     range_start = 0
#     range_end = 100
#     default = 0


@dataclass
class DesveladoOptions(PerGameCommonOptions):
    goal: Goal
    shuffle_bonnies_bones: ShuffleBonniesBones
    # room_sanity: RoomSanity
    # local_fillers: LocalFillers


option_groups = [
    OptionGroup(
        "Game Options",
        [Goal, ShuffleBonniesBones],
    ),
    # OptionGroup(
    #     "Extra checks",
    #     [RoomSanity, LocalFillers],
    # ),
]
