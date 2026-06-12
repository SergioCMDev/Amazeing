from sys import stdin
from parser import parse_file
from mazagen.dictionary import Dictionary
from mazagen.Cell import Cell
from mazagen.laberithm_maker import MazeGenerator

from matrix_drawer import print_matrix
import sys


def main() -> None:
    input_list: list[str] = sys.argv
    if (len(input_list) != 2):
        print("Configuration file is required")
        return
    if (not input_list[1].endswith(".txt")):
        print("Configuration file is not valid")
        return
    filename: str = input_list[1]

    data_parsed: Dictionary | None
    try:
        with open(filename, "r") as file:
            data_parsed = parse_file(file)
    except FileNotFoundError:
        print(f"There is no file with name: {filename}")
        return
    if (data_parsed is None
            or not data_parsed.check_mandatory_keys_are_in_dict()
            or data_parsed.get_entry() == data_parsed.get_exit()
            or not data_parsed.initial_positions_inside_matrix()):
        print("There is no valid file")
        return

    height: int | None = data_parsed.get_height()
    width: int | None = data_parsed.get_width()
    if (height is None or width is None):
        return
    generator = MazeGenerator(data_parsed, seed=42)
    matrix, solution, movements = generator.generate()
    print_matrix(matrix, height, width, solution, False)
    matrix, solution, movements = get_input_response(
        matrix, data_parsed, height,
        width, solution, movements)
    the_txt(matrix, data_parsed, movements)


def get_input_response(matrix: list[list[Cell]],
                       data_parsed: Dictionary, total_height_size: int,
                       total_width_size: int,
                       solution: list, movements: list
                       ) -> tuple[list[list[Cell]], list, list]:
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
                generator = MazeGenerator(data_parsed)
                matrix, solution, movements = generator.generate()
                print_matrix(
                    matrix, total_height_size,
                    total_width_size, solution, show_path)
            if input == 2:
                show_path = not show_path
                print_matrix(
                    matrix, total_height_size,
                    total_width_size, solution, show_path)
            if input == 3:
                Cell.change_color()
                print_matrix(
                    matrix, total_height_size,
                    total_width_size, solution, show_path)
            if input == 4:
                return matrix, solution, movements
        except ValueError:
            print(f"'{readed}' is not a valid option.")


def the_txt(matrix: list[list[Cell]],
            data_parsed: Dictionary, solution: list) -> None:
    new_file = data_parsed.get_output_file()
    if not new_file:
        return None
    try:
        with open(new_file, "w") as f:
            for row in matrix:
                row_hex: str = ""
                for cell in row:
                    row_hex += f"{cell.value:X}"
                f.write(row_hex + "\n")
            f.write(f"Entry: {data_parsed.get_entry()}\n")
            f.write(f"Exit: {data_parsed.get_exit()}\n")
            the_solution: str = ""
            for i in solution:
                the_solution += i
            f.write(the_solution)
    except (OSError, ValueError) as e:
        sys.stderr.write(
            f"[STDERR] Error opening file "
            f"'{new_file}': {e}\nData not saved.\n")


if __name__ == "__main__":
    main()
