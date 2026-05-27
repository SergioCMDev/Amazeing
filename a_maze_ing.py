from sys import stdin
from parser import parse_file
from dictionary import Dictionary
from Cell import Cell
from constants import CELL_SIZE_HEIGHT, CELL_SIZE_WIDHT
from laberithm_maker import make_the_maze
from matrix_drawer import print_matrix


def main() -> None:
    # input_list: list[str] = argv
    # if (len(input_list) != 2):
    #     print("No se ha introducido nombre de archivo")
    #     return
    # filename: str = input_list[1]
    filename: str = "ee"

    data_parsed: Dictionary | None
    try:
        with open(filename, "r") as file:
            data_parsed = parse_file(file)
    except FileNotFoundError:
        print(f"No existe archivo con nombre: {filename}")
        return
    if (data_parsed is None
            or not data_parsed.check_mandatory_keys_are_in_dict()
            or data_parsed.get_entry() == data_parsed.get_exit()):
        print("No se ha añadido un archivo de configuracion válido")
        return

    # for key, value in data_parsed.items():
    #     print(f"Key {key}-{value}", end="")

    heigth: int | None = data_parsed.get_heigth()
    width: int | None = data_parsed.get_width()
    if (heigth is None or width is None):
        return
    print()
    create_matrix(heigth, width)


def get_input_response() -> int:
    input: int = 4
    while (True):
        print("== A-Maze-ing ==")
        print("1. Regenerate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")
        readed: str = stdin.readline()
        if (readed == "\n"):
            print("Debes introducir una opción")
            continue
        readed = readed.strip()
        try:
            input = int(readed)
            if (input not in (1, 2, 3, 4)):
                print(f"'{readed}' no es una opción valida")
                continue
            return input
        except ValueError:
            print(f"'{readed}' no es una opción valida")


def create_matrix(heigth: int, width: int) -> list[str]:
    matrix: list[list[Cell]] = []
    total_height_size = CELL_SIZE_HEIGHT * heigth
    total_width_size = CELL_SIZE_WIDHT * width

    print(f"Total height {total_height_size} | Total width {total_width_size}")

    for heigth_it in range(0, total_height_size):
        row: list[Cell] = []
        top_border_empty: bool = True if heigth_it == 0 else False
        bot_border_empty: bool = True if (
            heigth_it == total_height_size - 1) else False
        for widht_it in range(0, total_width_size):
            left_border_empty: bool = True if widht_it == 0 else False
            right_border_empty: bool = True if (
                widht_it == total_width_size-1) else False

            row.append(Cell())
        matrix.append(row) 
    solution: list = []
    matrix2, solution = make_the_maze(total_height_size, total_height_size)
    print_matrix(matrix2, total_height_size, total_width_size, solution)


def draw_cell_lines(lines: list[Cell]) -> list[str]:
    cells: list[str] = []
    for line in lines:
        cells.append(line.draw())
    return cells





if __name__ == "__main__":
    # print(get_input_response())
    main()
