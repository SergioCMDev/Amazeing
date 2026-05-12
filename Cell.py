from constants import WallPosition


class Cell:
    def __init__(self,
                 right_border: bool = False, left_border: bool = False,
                 top_border: bool = False, bot_border: bool = False
                 ) -> None:
        self.walls: list[bool] = [False if top_border else True,
                                  False if right_border else True,
                                  False if bot_border else True,
                                  False if left_border else True]
        # self.right_border = right_border
        # self.left_border = left_border
        # self.top_border = top_border
        # self.bot_border = bot_border

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
        top = "---" if self.walls[0] else "   "
        mid = (("|" if self.walls[3] else " ")
               + "  " + ("|" if self.walls[1] else " "))
        bot = "---" if self.walls[2] else "   "

        return [top, mid, bot]
