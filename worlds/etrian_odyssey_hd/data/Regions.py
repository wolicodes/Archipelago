from enum import Enum

class Regions(str, Enum):
    ETRIA = "Etria"
    B1F_MAIN = "B1F Main"
    B1F_CLEAR_CRYSTAL_ROOM = "B1F Clear Crystal Room"
    B1F_VIOLET_CRYSTAL_ROOM = "B1F Violet Crystal Room"
    B1F_EAST = "B1F East"
    B2F_MAIN = "B2F Main"

class Entrances(str, Enum):
    ENTER_THE_LABYRINTH = "Enter the Labyrinth"
    B1F_CLEAR_CRYSTAL_ROOM_ACCESS = "B1F Clear Crystal Room Access"
    B1F_VIOLET_CRYSTAL_ROOM_ACCESS = "B1F Violet Crystal Room Access"
    B1F_EAST_ACCESS = "B1F East Access"
    B2F_ACCESS = "B2F Access"