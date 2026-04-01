from sys import argv
from typing import Any
from FileNotFoundException import FileNotFoundException
from io import TextIOWrapper


def main() -> None:
    input_list: list[str] = argv
    if (len(input_list) != 2):
        print("No se ha introducido nombre de archivo")
        return
    filename: str = input_list[1]
    try:
        with open(filename, "r") as file:
            parse_file(file)

    except FileNotFoundError:
        print(f"No existe archivo con nombre: {filename}")
        return
    print("")


def parse_file(file: TextIOWrapper) -> dict[str, Any] | None:
    counter: int = 0
    for line in file.readlines():
        if (line[0] == "#"):
            continue
        counter += 1
        line_parts: list[str] = line.split("=")
        if (len(line_parts) != 2):
            print(f"Line {counter} is not formatted correctly")
            continue
        for parts in line_parts if(len(parts) <= 0) print(f"Line {counter} is not formatted correctly")
            

        print(line_parts, end="\n")


if __name__ == "__main__":
    main()
