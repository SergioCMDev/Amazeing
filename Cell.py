from constants import WallPosition, CELL_SIZE_HEIGHT, CELL_SIZE_WIDHT


class Cell:
    def __init__(self,
                 starting_value: int = 0, editable: bool = True
                 ) -> None:
        self.starting_value: int = starting_value
        self.value: int = starting_value


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
        top = "-" * CELL_SIZE_WIDHT if self.value % 2 else " " * CELL_SIZE_WIDHT
        mid = (("|" if self.value - 8 >= 0 else " ") + " " * (CELL_SIZE_WIDHT - 1))
            #   + " " * (CELL_SIZE_WIDHT - 2) + ("|" if self.walls[1] else " "))
        bot = "-" * CELL_SIZE_WIDHT if self.value - 4 >= 0 else " " * CELL_SIZE_WIDHT

        return [top, mid, bot]
