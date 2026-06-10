from .algo import Solver
from ..box import Box
from math import sqrt 


class Glouton(Solver):
    """Class Glouton."""

    def __init__(self, grid: list[list[Box]]) -> None:
        super().__init__(grid)

    def algo(self, pacman_pos: tuple[int, int],
             blinky_pos: tuple[int, int]) -> tuple[int, int]:
        self
        list_directions: list[int, int] = self.get_neighbors(blinky_pos)
        list_distance: list[float] = []
        dict_d = {}
        x, y = blinky_pos
        px, py = pacman_pos
        for direction in list_directions:
            dx, dy = direction
            d = sqrt(((x + dx) - px)**2 + ((y + dy) - py)**2)
            print("direction", direction)
            list_distance.append(d)
            dict_d[d] = direction
        min_d = dict_d[min(list_distance)]
        print("min_d", min_d)

        return min_d

