from enum import Enum

MIN_SIZE_WIDTH = 8
MIN_SIZE_HEIGHT = 8
MAX_SIZE = 100
CELL_SIZE_HEIGHT = 4
CELL_SIZE_WIDHT = 4
CELL_INITIAL_VALUE = 15

class WallPosition(str, Enum):
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"
