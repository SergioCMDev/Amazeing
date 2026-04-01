from io import TextIOWrapper
from dictionary import Dictionary
from utils import get_coord_value
from keys import valid_keys


def line_has_two_parts(line_parts: list[str]) -> bool:
    return len(line_parts) == 2


def line_has_valid_values_parts(line_parts: list[str]) -> bool:
    for part in line_parts:
        if (part == '\n'):
            return False
    return True


def key_is_valid(key_name: str) -> bool:
    return key_name in valid_keys


def data_for_key_valid(line_parts: list[str]) -> bool:
    key: str = line_parts[0]
    match key:
        case "WIDTH" | "HEIGTH":
            try:
                int(line_parts[1])
                return True
            except ValueError:
                return False
        case "ENTRY" | "EXIT":
            tuple_coords = get_coord_value(line_parts[1])
            return True if tuple_coords is not None else False
        case "OUTPUT_FILE":
            try:
                filename: str = str(line_parts[1])
                if (filename.endswith("\n")):
                    filename = filename.removesuffix("\n")
                open(filename)
                return True
            except (ValueError, FileNotFoundError):
                return False
        case "PERFECT":
            try:
                bool(line_parts[1])
                return True
            except ValueError:
                return False
        case _:
            return False


def parse_file(file: TextIOWrapper) -> Dictionary | None:
    counter: int = 0
    dictionary = Dictionary()
    for line in file.readlines():
        counter += 1
        if (line[0] == "#"):
            continue
        line_parts: list[str] = line.split("=")
        if (not line_has_two_parts(line_parts)):
            print(f"Line {counter} is not formatted correctly")
            continue
        if (not line_has_valid_values_parts(line_parts)):
            print(f"Line {counter} is not formatted correctly")
            continue
        if (not key_is_valid(line_parts[0])):
            print(f"Line {counter} has invalid key")
            continue
        if (not data_for_key_valid(line_parts)):
            print(f"Line {counter} has invalid data for key")
            continue
        if (not dictionary.add(line_parts)):
            print(f"Line {counter} has a key added previously")
            continue
        print(f"Line {counter} added correctly")
    return dictionary if len(dictionary.keys()) > 0 else None
