ENTER_THE_LABYRINTH = "Enter the Labyrinth"
B1F_CLEAR_CRYSTAL_ROOM_ACCESS = "B1F Clear Crystal Room Access"
B1F_VIOLET_CRYSTAL_ROOM_ACCESS = "B1F Violet Crystal Room Access"
B1F_EAST_ACCESS = "B1F East Access"
B2F_ACCESS = "B2F Access"
B2F_SOUTH_ACCESS = "B2F South Access"

MAIN_FLOORS = 5
FLOOR_ACCESS = []

for i in range(MAIN_FLOORS-1):
    FLOOR_ACCESS.append("B"+str(i+2)+"F Access")