from sys import stdin
from parser import parse_file
from dictionary import Dictionary
from enum import Enum
from constants import CELL_SIZE_HEIGHT, CELL_SIZE_WIDHT

class WallPosition(str, Enum):
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"

class Cell:
    def __init__(self, heigth: int, width: int) -> None:
        self.heigth: int = heigth
        self.width: int = width
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
    for heigth_it in range(0, heigth):
        for width_it in range(0, width):
            cell: Cell = Cell(CELL_SIZE_HEIGHT, CELL_SIZE_WIDHT)
            cell.draw()
            dictio[heigth_it, width_it] = cell
            #Crear celdas asociandole height y widht
            #Luego cada celda se dibuja teniendo en cuenta unos valores que podemos modificar para darles su tamaño
            #Hay que tener en cuenta tambien que si ocupa 3 de ancho, la proxima celda debe empezar en la posicion +3
            #Debemos comprobar sus vecinos para no poner doble barrera a sus adyacentes al igual que si abrimos un lado de x, y abrir el lado contrario en x+1, y (los vecinos ya sea arriba, abajo etc)
            # print(f"({heigth_it}:{width_it})", end="")

            # if (heigth_it == 0):
            #     if (width_it == 0 or width_it == width-1):
            #         print("+", end="")
            #     else:
            #         print("-", end="")
            # if (heigth_it == heigth-1):
            #     if (width_it == 0 or width_it == width-1):
            #         print("+", end="")
            #     else:
            #         print("-", end="")
            # elif (heigth_it > 0 and heigth_it < heigth):
            #     if (width_it == 0 or width_it == width-1):
            #         print("|", end="")
            #     else:
            #         print("*", end="")

        print()


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


if __name__ == "__main__":
    # print(get_input_response())
    main()
