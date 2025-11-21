from dataclasses import dataclass
from Options import PerGameCommonOptions, Range

class StartingMoney(Range):
    """
    How much money will you start the seed with.
    """
    display_name = "Starting money"
    range_start = 0
    range_end = 99999999
    default = 1000


@dataclass
class EOHDOptions(PerGameCommonOptions):
    starting_money: StartingMoney
