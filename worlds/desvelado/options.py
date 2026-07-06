from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle


class Goal(Choice):
    """
    reach_bonnie_room: Reach Bonnie's room
    complete_bonnie: Reach Bonnie's room after collecting all 15 Bonnie's bones
    map_clear: Reach Bonnie's room after completing all the zones
    """
    display_name = "Goal"

    option_reach_bonnie_room = 0
    option_complete_bonnie = 1
    option_map_clear = 2

    default = option_reach_bonnie_room


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
