from enum import Enum
import os

MIN_SIZE_WIDTH = 8
MIN_SIZE_HEIGHT = 8
MAX_SIZE = os.get_terminal_size
CELL_SIZE_HEIGHT = 4
CELL_SIZE_WIDHT = 4
CELL_INITIAL_VALUE = 15


class WallPosition(str, Enum):
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"
