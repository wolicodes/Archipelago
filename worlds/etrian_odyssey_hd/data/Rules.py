from BaseClasses import CollectionState
from worlds.etrian_odyssey_hd import world
from worlds.etrian_odyssey_hd.data import Items

def has_clear_key(state: CollectionState) -> bool:
    return state.has(Items.CLEAR_KEY, world.player)