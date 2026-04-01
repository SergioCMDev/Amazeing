from io import TextIOWrapper
from typing import Any
from dictionary import Dictionary

valid_keys: set[str] = {"WIDTH", "HEIGTH", "ENTRY", "EXIT", "OUTPUT_FILE",
                        "PERFECT"}


# def add_to_dict(data: list[str], dictionary: dict[str, Any]) -> bool:
#     if (dictionary.get(data[0]) is not None):
#         return False
#     dictionary[data[0]] = data[1]
#     return True


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
            except ValueError:
                return False
        case "ENTRY":
        case "EXIT":
        case "OUTPUT_FILE":
            try:
                str(line_parts[1])
            except ValueError:
                return False
        case "PERFECT":
            try:
                bool(line_parts[1])
            except ValueError:
                return False

def parse_file(file: TextIOWrapper) -> dict[str, Any] | None:
    counter: int = 0
    data: dict[str, Any] = {}
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

    return data if len(data.keys()) > 0 else None
