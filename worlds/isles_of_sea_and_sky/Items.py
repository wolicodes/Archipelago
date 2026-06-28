from BaseClasses import Item, ItemClassification as IC
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: IC


class IslesOfSeaAndSkyItem(Item):
    game: str = "Isles Of Sea And Sky"

# Item ID is set to in-game Object Index
item_table = {
    "Ancient Key":                          ItemData(125,       IC.progression_skip_balancing),
    "Topaz":                                ItemData(861,       IC.progression_skip_balancing),
    "Sapphire":                             ItemData(683,       IC.progression_skip_balancing),
    "Ruby":                                 ItemData(654,       IC.progression_skip_balancing),
    "Diamond":                              ItemData(316,       IC.progression_skip_balancing),
    "Obsidian":                             ItemData(509,       IC.progression_skip_balancing),
    "Star Piece":                           ItemData(801,       IC.progression_skip_balancing),
    "Ancient Rune Stone":                   ItemData(664,       IC.progression | IC.useful),
    "Topaz Rune Stone":                     ItemData(670,       IC.progression | IC.useful),
    "Sapphire Rune Stone":                  ItemData(669,       IC.progression | IC.useful),
    "Ruby Rune Stone":                      ItemData(668,       IC.progression | IC.useful),
    "Diamond Rune Stone":                   ItemData(665,       IC.progression | IC.useful),
    "Obsidian Rune Stone":                  ItemData(666,       IC.progression | IC.useful),
    "Gopher Gloves":                        ItemData(397,       IC.progression | IC.useful),
    "Frog Flippers":                        ItemData(386,       IC.progression | IC.useful),
    "Salamander Shirt":                     ItemData(671,       IC.progression | IC.useful),
    "Kite Cloak":                           ItemData(440,       IC.progression | IC.useful),
    "Blue Stone Tablet":                    ItemData(644,       IC.progression_skip_balancing),
    "Gold Stone Tablet":                    ItemData(645,       IC.progression_skip_balancing),
    "Seashell":                             ItemData(688,       IC.filler),
    "Fire Key":                             ItemData(372,       IC.progression_skip_balancing),
    "Music Note":                           ItemData(498,       IC.progression_skip_balancing),
    "Phoenix Flute":                        ItemData(555,       IC.progression | IC.useful),
    "Star Viewing Orb":                     ItemData(806,       IC.useful),
    # Mysterious Update
    "Serpent Lock Shard":                   ItemData(710,       IC.progression_skip_balancing),
    "Serpent Circlet":                      ItemData(707,       IC.progression | IC.useful),
    "Pyramidion":                           ItemData(625,       IC.progression_skip_balancing),
    # Cutscenes
    "Awaken Earth Elementals":              ItemData(901,       IC.progression | IC.useful),
    "Awaken Water Elementals":              ItemData(902,       IC.progression | IC.useful),
    "Awaken Fire Elementals":               ItemData(903,       IC.progression | IC.useful),
    "Awaken Wind Elementals":               ItemData(904,       IC.progression | IC.useful),
    "Activate Shadow Blocks":               ItemData(905,       IC.progression | IC.useful),
    "Big Bell Hit - Rolling":               ItemData(911,       IC.progression_skip_balancing),
    "Big Bell Hit - Sunken":                ItemData(912,       IC.progression_skip_balancing),
    "Big Bell Hit - Aggro":                 ItemData(913,       IC.progression_skip_balancing),
    "Big Bell Hit - Nunatak":               ItemData(914,       IC.progression_skip_balancing),
    "Sanctum Shard Hit - Earth":            ItemData(921,       IC.progression_skip_balancing),
    "Sanctum Shard Hit - Water":            ItemData(922,       IC.progression_skip_balancing),
    "Sanctum Shard Hit - Fire":             ItemData(923,       IC.progression_skip_balancing),
    "Sanctum Shard Hit - Wind":             ItemData(924,       IC.progression_skip_balancing),
    # Traps
    "Slow Trap":                            ItemData(7000,      IC.trap),
    "Fast Trap":                            ItemData(7001,      IC.trap),
    "Tiny Trap":                            ItemData(7002,      IC.trap),
    "Thicc Trap":                           ItemData(7003,      IC.trap),
    "Ice Trap":                             ItemData(7004,      IC.trap),
    "Magma Spirit Trap":                    ItemData(7005,      IC.trap),
    "Metal Spirit Trap":                    ItemData(7006,      IC.trap),
    "Lava Spirit Trap":                     ItemData(7007,      IC.trap),
    "Reversed Controls Trap":               ItemData(7008,      IC.trap),
    "Floor Is Lava Trap":                   ItemData(7009,      IC.trap)

}



progression_items = {

    "Ancient Rune Stone":                   1,
    "Topaz Rune Stone":                     1,
    "Sapphire Rune Stone":                  1,
    "Ruby Rune Stone":                      1,
    "Diamond Rune Stone":                   1,
    "Gopher Gloves":                        1,
    "Frog Flippers":                        1,
    "Salamander Shirt":                     1,
    "Kite Cloak":                           1,
    "Fire Key":                             3,
    "Awaken Earth Elementals":              1,
    "Awaken Water Elementals":              1,
    "Awaken Fire Elementals":               1,
    "Awaken Wind Elementals":               1,
    "Activate Shadow Blocks":               1,
    "Sanctum Shard Hit - Earth":            1,
    "Sanctum Shard Hit - Water":            1,
    "Sanctum Shard Hit - Fire":             1,
    "Sanctum Shard Hit - Wind":             1,
    "Phoenix Flute":                        1
}

key_items = {
    "Ancient Key":                          77,
    "Topaz":                                12,
    "Sapphire":                             12,
    "Ruby":                                 12,
    "Diamond":                              12,
    "Star Piece":                           120
}

note_items = {
    "Music Note":                           24
}

non_key_items = {
    "Obsidian":                             14,
    "Obsidian Rune Stone":                  1,
    "Blue Stone Tablet":                    1,
    "Gold Stone Tablet":                    1,
    "Star Viewing Orb":                     1,
    "Big Bell Hit - Rolling":               1,
    "Big Bell Hit - Sunken":                1,
    "Big Bell Hit - Aggro":                 1,
    "Big Bell Hit - Nunatak":               1
}

# 52 total
junk_weights = {
    "Seashell":                             16,
    "Ancient Key":                          10,
    "Star Piece":                           8,
    "Obsidian":                             2,
    "Topaz":                                4,
    "Sapphire":                             4,
    "Ruby":                                 4,
    "Diamond":                              4,
}

# 20 total
trap_weights = {
    "Slow Trap":                            1,
    "Fast Trap":                            1,
    "Tiny Trap":                            1,
    "Thicc Trap":                           1,
    "Ice Trap":                             2,
    "Magma Spirit Trap":                    3,
    "Lava Spirit Trap":                     3,
    "Metal Spirit Trap":                    3,
    "Reversed Controls Trap":               2,
    "Floor Is Lava Trap":                   3,
}


