from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, Range, Toggle

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

class PriceMode(Choice):
    """
    Determines if the shop prices are handled in percentage or as flat values.
    """
    display_name = "Price mode"
    option_percent = 0
    option_flat = 1
    default = option_percent

class PricePercentValue(Range):
    """
    Set the prices of the shop items, in percent relative to their vanilla price.
    0 means all shop items will free, 100 means vanilla price, 200 means double the vanilla price.
    Only does something if you enabled percent price mode.
    """
    display_name = "Price percent value"
    range_start = 0
    range_end = 200
    default = 100

class PriceFlatValue(Range):
    """
    Set the prices of the shop items. Every shop items will have the value you set here as a fixed price.
    Only does something if you enabled flat price mode.
    """
    display_name = "Price flat value"
    range_start = 0
    range_end = 250000
    default = 100

@dataclass
class EOHDOptions(PerGameCommonOptions):
    starting_money: StartingMoney
    shop_sanity: ShopSanity
    price_mode: PriceMode
    price_percent_value: PricePercentValue
    price_flat_value: PriceFlatValue
