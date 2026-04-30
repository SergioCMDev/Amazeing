from enum import Enum

MIN_SIZE = 4
MAX_SIZE = 100
CELL_SIZE_HEIGHT = 4
CELL_SIZE_WIDHT = 4

class WallPosition(str, Enum):
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"
