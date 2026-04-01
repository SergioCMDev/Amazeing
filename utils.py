from typing import Any


def get_coord_value(value: Any) -> tuple[int, int] | None:
    coords: str = str(value)
    positions: list[str] = coords.split(",")
    if (len(positions) != 2):
        return None
    try:
        return (int(positions[0]), int(positions[1]))
    except ValueError:
        return None
