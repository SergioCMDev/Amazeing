from constants import WallPosition, CELL_SIZE_HEIGHT, CELL_SIZE_WIDHT
import colors
import random

class Cell:
    def __init__(self,
                 starting_value: int = 15
                 ) -> None:
        self.editable: bool = True
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
        
        # NORTE: si bit 0 (valor 1) está presente, dibuja pared
        top = f"{self.WALL_COLOR}-{self.RES_COLORS}" * CELL_SIZE_WIDHT if (self.value & 1) else " " * CELL_SIZE_WIDHT
        
        # OESTE: si bit 3 (valor 8) está presente, dibuja pared
        print_west = True if (self.value & 8) else False
        
        # SUR: si bit 2 (valor 4) está presente, dibuja pared
        print_south = True if (self.value & 4) else False
        
        mid = ((f"{self.WALL_COLOR}|{self.RES_COLORS}" if print_west else " ") + solution_char * (CELL_SIZE_WIDHT - 1))
        bot = f"{self.WALL_COLOR}-{self.RES_COLORS}" * CELL_SIZE_WIDHT if print_south else " " * CELL_SIZE_WIDHT

        return [top, mid, bot]
