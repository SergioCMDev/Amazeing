from typing import Any
from utils import get_coord_value


class Dictionary:
    _dictionary: dict[str, Any] = {}

    def __init__(self) -> None:
        pass

    def keys(self):
        return self._dictionary.keys()

    def items(self):
        return self._dictionary.items()

    def add(self, data: list[str]) -> bool:
        if (self._dictionary.get(data[0]) is not None):
            return False
        self._dictionary[data[0]] = data[1]
        return True

    def get_width(self) -> int | None:
        key_size: int = len(self._dictionary.keys())
        if key_size == 0 or self._dictionary["WIDTH"] is None:
            return None
        return int(self._dictionary["WIDTH"])

    def get_heigth(self) -> int | None:
        key_size: int = len(self._dictionary.keys())
        if key_size == 0 or self._dictionary["HEIGHT"] is None:
            return None
        return int(self._dictionary["HEIGHT"])

    def get_entry(self) -> tuple[int, int] | None:
        key_size: int = len(self._dictionary.keys())
        if key_size == 0 or self._dictionary["ENTRY"] is None:
            return None
        tuple_coords = get_coord_value(self._dictionary["ENTRY"])
        return tuple_coords

    def get_output_file(self) -> str | None:
        key_size: int = len(self._dictionary.keys())
        if key_size == 0 or self._dictionary["OUTPUT_FILE"] is None:
            return None
        return str(self._dictionary["OUTPUT_FILE"])

    def get_is_perfect(self) -> bool | None:
        key_size: int = len(self._dictionary.keys())
        if key_size == 0 or self._dictionary["PERFECT"] is None:
            return None
        return bool(self._dictionary["PERFECT"])
