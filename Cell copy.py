from constants import WallPosition


class Cell:
    def __init__(self,
                 starting_value: int
                 ) -> None:
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
        top = "---" if self.value % 2 == 0 else "   "
        mid = "| " if self.value - 8 >= 0 else "   "
            #   else " "               + " " + ("|" if self.walls[1] else " "))
        bot = "---" if self.value - 4 >= 0 else "   "

        return [top, mid, bot]