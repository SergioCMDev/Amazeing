from sys import stdin
from parser import parse_file
from dictionary import Dictionary
from Cell import Cell
from constants import CELL_SIZE_HEIGHT, CELL_SIZE_WIDHT






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
    #cells => 4 walls
    print()
    dictio: dict [tuple[int, int], Cell] = {}
    # for heigth_it in range(0, heigth):
    #     # for width_it in range(0, width):
    #         cell: Cell = Cell()
    #         cell.draw()
    #         dictio[heigth_it] = cell
            #Crear celdas asociandole height y widht
            #Luego cada celda se dibuja teniendo en cuenta unos valores que podemos modificar para darles su tamaño
            #Hay que tener en cuenta tambien que si ocupa 3 de ancho, la proxima celda debe empezar en la posicion +3
            #Debemos comprobar sus vecinos para no poner doble barrera a sus adyacentes al igual que si abrimos un lado de x, y abrir el lado contrario en x+1, y (los vecinos ya sea arriba, abajo etc)
            # print(f"({heigth_it}:{width_it})", end="")
    create_maze(heigth, width)

        # print()


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

def create_maze(heigth: int, width: int) -> list[str]:
    matrix: list[str] = []
    total_height_size = CELL_SIZE_HEIGHT* heigth
    total_width_size = CELL_SIZE_WIDHT* width

    print(f"Total height {total_height_size} | Total width {total_width_size}")
    matrix = [" " for _ in range(0, total_height_size)]

    for heigth_it in range(0, total_height_size):
        matrix[heigth_it] = [" " for _ in range(0, total_width_size)]

    for heigth_it in range(0, total_height_size):
        print(heigth_it)
        for width_it in range(0, total_width_size):
            if(heigth_it == 0):
                if(width_it == 0):
                    matrix[heigth_it][width_it] = "*"
                if (width_it > 0 and width_it < total_width_size):
                    matrix[heigth_it][width_it] = "-"
                if(width_it == total_width_size-1):
                     matrix[heigth_it][width_it]= "*"

            elif(heigth_it > 0 and heigth_it < total_height_size - 1):
                if (width_it == 0):
                     matrix[heigth_it][width_it] = "!"
                if (width_it > 0 and width_it < total_width_size):
                    matrix[heigth_it][width_it] = "+"
                if(width_it == total_width_size-1):
                    matrix[heigth_it][width_it] = "!"
            elif (heigth_it == total_height_size - 1):
                print("LAST")
                if(width_it == 0):
                    matrix[heigth_it][width_it] = "$"
                if (width_it > 0 and width_it < total_width_size):
                    matrix[heigth_it][width_it] = "-"
                if(width_it == total_width_size-1):
                    matrix[heigth_it][width_it] = "$"

    for heigth_it in range(0, total_height_size):
        for width_it in range(0, total_width_size):
            print(matrix[heigth_it][width_it], end=" ")
        print()
    # print(matrix)



if __name__ == "__main__":
    # print(get_input_response())
    main()
