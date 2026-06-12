from mazagen.constants import (
    CELL_SIZE_WIDHT, CELL_INITIAL_VALUE)
import colors
import random


class Cell:
    def __init__(self,
                 starting_value: int = CELL_INITIAL_VALUE
                 ) -> None:
        self.starting_value: int = starting_value
        self.value: int = starting_value
        self.solution_path: bool = False
        self.is_entry: bool = False
        self.is_exit: bool = False

    WALL_COLOR = random.choice(colors.COL_LIST)
    SOLUTTION = random.choice(colors.COL_LIST)
    RES_COLORS = colors.RESET

    @classmethod
    def change_color(cls) -> None:
        cls.WALL_COLOR = random.choice(colors.COL_LIST)
        cls.SOLUTTION = random.choice(colors.COL_LIST)

    def draw(self, show_path: bool) -> list[str]:
        solution_char: str
        if show_path and self.solution_path:
            icon: str = ""
            if self.is_entry:
                icon = " ☻ "
            elif self.is_exit:
                icon = " ♨ "
            else:
                icon = ' ✈ '
            solution_char = f"{self.SOLUTTION}{icon}{self.RES_COLORS}"
        else:
            solution_char = " " * (CELL_SIZE_WIDHT - 1)
        top = (
            f"{self.WALL_COLOR}-{self.RES_COLORS}" * CELL_SIZE_WIDHT
            if not self.value % 2
            else " " * CELL_SIZE_WIDHT)
        print_west: bool = False
        print_south: bool = False
        temp_value: int = self.value
        if (temp_value + 8 <= 15):
            print_west = True
            temp_value += 8
        if (temp_value + 4 <= 15):
            print_south = True
            temp_value += 4
        mid = (
            f"{self.WALL_COLOR}|{self.RES_COLORS}"
            if not print_west
            else " ") + solution_char
        bot = (
            f"{self.WALL_COLOR}-{self.RES_COLORS}" * CELL_SIZE_WIDHT
            if not print_south
            else " " * CELL_SIZE_WIDHT)

        return [top, mid, bot]
