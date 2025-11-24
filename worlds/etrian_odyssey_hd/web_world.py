from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

class EOHDWebWorld(WebWorld):
    game = "Etrian Odyssey HD"
    theme = "ocean"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Etrian Odyssey HD for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Woli"],
    )
    tutorials = [setup_en]
