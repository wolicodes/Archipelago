from BaseClasses import CollectionState
from worlds.etrian_odyssey_hd import world
from worlds.etrian_odyssey_hd.data.Items import Items


class Rules():
    def has_clear_key(state: CollectionState) -> bool:
        return state.has(Items.CLEAR_KEY.value, world.player)