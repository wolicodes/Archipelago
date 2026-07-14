from dataclasses import dataclass

from Options import OptionGroup, OptionSet, PerGameCommonOptions, DefaultOnToggle


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


@dataclass
class DesveladoOptions(PerGameCommonOptions):
    goal: Goal
    shuffle_bonnies_bones: ShuffleBonniesBones


option_groups = [
    OptionGroup(
        "Game Options",
        [Goal, ShuffleBonniesBones],
    ),
]
