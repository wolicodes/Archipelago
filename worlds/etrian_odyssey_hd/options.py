from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, Range, Toggle


class ExpModifier(Range):
    """
    Percentage to apply to the received exp.
    """
    display_name = "Exp. Modifier"
    internal_name = "exp_modifier"
    range_start = 50
    range_end = 1000
    default = 100


class StartingMoney(Range):
    """
    How much money will you start the seed with.
    """
    display_name = "Starting money"
    internal_name = "starting_money"
    range_start = 0
    range_end = 99999999
    default = 1000


class EventItems(Toggle):
    """
    If enabled, the items that you find on the labyrinth events will be randomized.
    The item will be given no matter which choice you make in the event.
    """
    display_name = "Event items"
    internal_name = "event_items"
    default = True


# class EventSanity(Toggle):
#     """
#     If enabled, each labyrinth event that you clear will give you a check, and will add a filler to the pool.
#     This is independent of the items the events might give you.
#     """
#     display_name = "Event sanity"
#     internal_name = "event_sanity"
#     default = False


class ShopSanity(Toggle):
    """
    If enabled, each item you buy for the first time in Shilleka's Goods or the Apothecary will be a check.
    """
    display_name = "Shop sanity"
    internal_name = "shop_sanity"
    default = False


class PriceMode(Choice):
    """
    Determines if the shop prices are handled in percentage or as flat values.
    """
    display_name = "Price mode"
    internal_name = "price_mode"
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
    internal_name = "price_percent_value"
    range_start = 0
    range_end = 200
    default = 100


class PriceFlatValue(Range):
    """
    Set the prices of the shop items. Every shop items will have the value you set here as a fixed price.
    Only does something if you enabled flat price mode.
    """
    display_name = "Price flat value"
    internal_name = "price_flat_value"
    range_start = 0
    range_end = 250000
    default = 100


@dataclass
class EOHDOptions(PerGameCommonOptions):
    starting_money: StartingMoney
    exp_modifier: ExpModifier
    event_items: EventItems
    # event_sanity: EventSanity
    shop_sanity: ShopSanity
    price_mode: PriceMode
    price_percent_value: PricePercentValue
    price_flat_value: PriceFlatValue
