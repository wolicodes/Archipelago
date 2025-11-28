from dataclasses import dataclass, fields
from Options import PerGameCommonOptions, Range, Toggle

SHOP_SANITY = "shop_sanity"

class StartingMoney(Range):
    """
    How much money will you start the seed with.
    """
    display_name = "Starting money"
    range_start = 0
    range_end = 99999999
    default = 1000

class ShopSanity(Toggle):
    """
    If enabled, each item you buy for the first time in Shilleka's Goods or the Apothecary will be a check.
    """
    display_name = "Shop sanity"


@dataclass
class EOHDOptions(PerGameCommonOptions):
    starting_money: StartingMoney
    shop_sanity: ShopSanity
