from typing import Any
valid_keys: set[str] = {"WIDTH", "HEIGTH", "ENTRY", "EXIT", "OUTPUT_FILE",
                        "PERFECT"}


class Dictionary:
    _dictionary: dict[str, Any] = {}

    def __init__(self):
        pass

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
        x, y = self._dictionary["ENTRY"]
        return tuple(1, 2)

    def get_output_file(self) -> str | None:
        key_size: int = len(self._dictionary.keys())
        if key_size == 0 or self._dictionary["OUTPUT_FILE"] is None:
            return None
        return self._dictionary["OUTPUT_FILE"]
  
    def get_is_perfect(self) -> bool | None:
        key_size: int = len(self._dictionary.keys())
        if key_size == 0 or self._dictionary["PERFECT"] is None:
            return None
        return self._dictionary["PERFECT"]

# WIDTH Maze width (number of cells) WIDTH=20
# HEIGHT Maze height HEIGHT=15
# ENTRY Entry coordinates (x,y) ENTRY=0,0
# EXIT Exit coordinates (x,y) EXIT=19,14
# OUTPUT_FILE Output filename OUTPUT_FILE=maze.txt
# PERFECT Is the maze perfect? PERFECT=True