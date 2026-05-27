from typing import Any
from constants import WallPosition


def get_coord_value(value: Any) -> tuple[int, int] | None:
    coords: str = str(value)
    positions: list[str] = coords.split(",")
    if (len(positions) != 2):
        return None
    try:
        return (int(positions[0]), int(positions[1]))
    except ValueError:
        return None

def get_value_of_positions(positions : list[WallPosition]) -> int:
    value: int = 0
    for pos in positions:
        if (pos == WallPosition.NORTH):
            value -= 1
        if (pos == WallPosition.EAST):
            value -= 2
        if (pos == WallPosition.SOUTH):
            value -= 4
        if (pos == WallPosition.WEST):
            value -= 8
    return value