from sys import argv, stdin
from parser import parse_file
from dictionary import Dictionary


def main() -> None:
    input_list: list[str] = argv
    if (len(input_list) != 2):
        print("No se ha introducido nombre de archivo")
        return
    filename: str = input_list[1]
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

    for key, value in data_parsed.items():
        print(f"Key {key}-{value}", end="")

    print("")


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
    print(get_input_response())
    # main()
