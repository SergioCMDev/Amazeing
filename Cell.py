from constants import CELL_SIZE_HEIGHT, CELL_SIZE_WIDHT
from constants import WallPosition

class Cell:
    def __init__(self, position_x: int, position_y: int) -> None:
        self.position_x: int = position_x
        self.position_y: int = position_y
        self.walls: list[bool] = [True, True, True, True]

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
        lines: list[str] = []
        for heigth_it in range(0, CELL_SIZE_HEIGHT+1):
            current_line= ""
            for width_it in range(0, CELL_SIZE_WIDHT+1):
                if(heigth_it == 0):
                    if(width_it == 0):
                        current_line += "*"
                        # print("*", end="")
                    if (width_it > 0 and width_it < CELL_SIZE_WIDHT):
                        # print("-", end="")
                        current_line += "-"
                    if(width_it == CELL_SIZE_WIDHT-1):
                        current_line += "*"
                        # print("*")

                elif(heigth_it > 0 and heigth_it < CELL_SIZE_HEIGHT):
                    if (width_it == 0):
                        # print("!", end="")
                        current_line += "!"
                    if (width_it > 0 and width_it < CELL_SIZE_WIDHT):
                        # print(" ", end="")
                        current_line += " "
                    if(width_it == CELL_SIZE_WIDHT-1):
                        current_line += "!"
                        # print("!")
                elif (heigth_it == CELL_SIZE_HEIGHT):
                    if(width_it == 0):
                        # print("$", end="")
                        current_line += "$"
                    if (width_it > 0 and width_it < CELL_SIZE_WIDHT):
                        current_line += "-"
                        # print("-", end="")
                    if(width_it == CELL_SIZE_WIDHT-1):
                        current_line += "$"
                        # print("$")
                    lines.append(current_line)
        print(lines)
