from sys import stdin
from parser import parse_file
from dictionary import Dictionary
from Cell import Cell
from laberithm_maker import make_the_maze, create_matrix
from matrix_drawer import print_matrix
from utils import get_value_of_positions
from constants import WallPosition, CELL_INITIAL_VALUE


def main() -> None:
    # input_list: list[str] = argv
    # if (len(input_list) != 2):
    #     print("No se ha introducido nombre de archivo")
    #     return
    # filename: str = input_list[1]
    filename: str = "config.txt"

    data_parsed: Dictionary | None
    try:
        with open(filename, "r") as file:
            data_parsed = parse_file(file)
    except FileNotFoundError:
        print(f"There is no file with name: {filename}")
        return
    if (data_parsed is None
            or not data_parsed.check_mandatory_keys_are_in_dict()
            or data_parsed.get_entry() == data_parsed.get_exit()):
        print("There is no valid file")
        return

    # for key, value in data_parsed.items():
    #     print(f"Key {key}-{value}", end="")

    heigth: int | None = data_parsed.get_heigth()
    width: int | None = data_parsed.get_width()
    if (heigth is None or width is None):
        return
    print()
    create_matrix(heigth, width, data_parsed)


def get_input_response(matrix: list[list[Cell]], total_height_size: int, total_width_size: int, solution: list) -> int:
    input: int = 4
    show_path: bool = False
    while (True):
        print("== A-Maze-ing ==")
        print("1. Regenerate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")
        readed: str = stdin.readline()
        if (readed == "\n"):
            print("You must choose one of the options above.")
            continue
        readed = readed.strip()
        try:
            input = int(readed)
            if (input not in (1, 2, 3, 4)):
                print(f"'{readed}' is not a valid option.")
                continue
            if input == 1:
                print_matrix(matrix, total_height_size, total_width_size, solution, show_path)
            if input == 2:
                show_path = -show_path
                print_matrix(matrix, total_height_size, total_width_size, solution, show_path)
            if input == 3:
               # WALL_COLOR = random.choice(colors.COL_LIST) #ARREGLAR
                print_matrix(matrix, total_height_size, total_width_size, solution, show_path)
            if input == 4:
                pass
            return input
        except ValueError:
            print(f"'{readed}' is not a valid option.")


#def create_matrix(heigth: int, width: int, dict: Dictionary) -> list[str]:
#    matrix: list[list[Cell]] = []

#    print(f"Total height {heigth} | Total width {width}")
#    value = CELL_INITIAL_VALUE
#    for heigth_it in range(0, heigth):
#        row: list[Cell] = []
#        for widht_it in range(0, width):
#            if(widht_it == 0):
#                value += get_value_of_positions(WallPosition.EAST)
#            row.append(Cell(value))
#        matrix.append(row) 
#    solution: list = []
#    solution = make_the_maze(matrix, heigth, width, dict)
#    print_matrix(matrix, heigth, width, solution)


def draw_cell_lines(lines: list[Cell]) -> list[str]:
    cells: list[str] = []
    for line in lines:
        cells.append(line.draw())
    return cells


if __name__ == "__main__":
    # print(get_input_response())
    main()
