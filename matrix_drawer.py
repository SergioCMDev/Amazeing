from Cell import Cell
from constants import CELL_SIZE_HEIGHT, CELL_SIZE_WIDHT

corner_character = "*"
floor_character = "-"

def print_matrix(
        matrix: list[list[Cell]],
        total_height_size: int,
        total_width_size: int, solution: list) -> None:
    top_line: str = (
        f"{corner_character}"
        f"{total_width_size * floor_character * CELL_SIZE_WIDHT}"
        f"{corner_character}"
    )
    bottom_line: str = (
        f"{corner_character}"
        f"{total_width_size * floor_character * CELL_SIZE_WIDHT}"
        f"{corner_character}"
    )

    print(top_line)

    for heigth_it in range(0, total_height_size):
        top_line = ""
        mid_line = ""
        bot_line = ""
        for cell in range(0, total_width_size):
            # print(f"{heigth_it} {cell}")
            cell_lines = matrix[heigth_it][cell].draw()

            top_line += cell_lines[0]
            mid_line += cell_lines[1]
            bot_line += cell_lines[2]

        print("|" + mid_line + "|")
        if (heigth_it != total_height_size - 1):
            print("|" + bot_line + "|")

    print(bottom_line)
    print(solution)
