from sys import argv
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
    if (data_parsed is None):
        print("No se ha añadido un archivo de configuracion válido")
        return

    for key, value in data_parsed.items():
        print(f"Key {key}-{value}", end="")

    print("")


if __name__ == "__main__":
    main()
