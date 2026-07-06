from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups


class DesveladoWebWorld(WebWorld):
    game = "Desvelado"

    # Options are dirt, grass, grassFlowers, ice, jungle, ocean, partyTime, and stone.
    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Desvelado for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Woli"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
