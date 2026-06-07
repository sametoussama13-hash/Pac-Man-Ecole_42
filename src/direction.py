from enum import Enum


class Direction(Enum):
    """Class direction."""

    NORTH = (0, -1)
    EST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    @staticmethod
    def get_dir(direction: tuple[int]) -> str:
        return {
            Direction.NORTH.value: "north",
            Direction.EST.value: "est",
            Direction.SOUTH.value: "south",
            Direction.WEST.value: "west",
        }[direction]
