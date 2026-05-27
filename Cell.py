from constants import WallPosition, CELL_SIZE_HEIGHT, CELL_SIZE_WIDHT, CELL_INITIAL_VALUE
import colors
import random

class Cell:
    def __init__(self,
                 starting_value: int = CELL_INITIAL_VALUE
                 ) -> None:
        self.starting_value: int = starting_value
        self.value: int = starting_value
        self.solution_path: bool = False
    
    WALL_COLOR = random.choice(colors.COL_LIST)
    SOLUTTION = random.choice(colors.COL_LIST)
    RES_COLORS = colors.RESET


    def open_wall(self, position: WallPosition) -> None:
        if (position == WallPosition.NORTH):
            self.walls[0] = False
        elif (position == WallPosition.EAST):
            self.walls[1] = False
        elif (position == WallPosition.SOUTH):
            self.walls[2] = False
        elif (position == WallPosition.WEST):
            self.walls[3] = False

    def open_all_walls(self) -> None:
        for wall_it in range(0, 4):
            self.walls[wall_it] = False

    def draw(self) -> list[str]:
        solution_char: str = "·" if self.solution_path else " "
        top = f"{self.WALL_COLOR}-{self.RES_COLORS}" * CELL_SIZE_WIDHT if not self.value % 2 else " " * CELL_SIZE_WIDHT 
        print_west: bool = False
        print_south: bool = False

        if( self.value + 8 >= 0):
            print_west = True
            self.value += 8 
        if( self.value + 4 >= 0):
            print_south = True
            self.value += 4 
        mid = ((f"{self.WALL_COLOR}|{self.RES_COLORS}" if not print_west else " ") + solution_char * (CELL_SIZE_WIDHT - 1))
            #   + " " * (CELL_SIZE_WIDHT - 2) + ("|" if self.walls[1] else " "))
        bot = f"{self.WALL_COLOR}-{self.RES_COLORS}" * CELL_SIZE_WIDHT if not print_south else " " * CELL_SIZE_WIDHT

        return [top, mid, bot]
