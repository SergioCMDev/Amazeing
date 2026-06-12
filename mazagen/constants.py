from enum import Enum

MIN_SIZE_WIDTH = 3
MIN_SIZE_HEIGHT = 3
MAX_SIZE = 50
CELL_SIZE_HEIGHT = 4
CELL_SIZE_WIDHT = 4
CELL_INITIAL_VALUE = 15
MIN_SIZE_42 = 8


class WallPosition(str, Enum):
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"
