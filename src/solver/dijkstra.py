from .algo import Solver
from ..box import Box


class Dijkstra(Solver):
    def __init__(self, grid: list[list[Box]]) -> None:
        super().__init__(grid)

    def algo(self, entry: tuple[int, int], exit: tuple[int, int]) -> dict[tuple[int, int], int]:
        start: tuple[int, int] = entry
        frontier: list[tuple[int, int]] = [start]
        distances: dict[tuple[int, int], int] = {start: 0}
        while frontier:
            new_frontier: list[tuple[int, int]] = []
            for pos in frontier:
                for neighbor_pos in self.get_neighbors(pos):
                    if neighbor_pos not in distances:
                        distances[neighbor_pos] = distances[pos] + 1
                        new_frontier.append(neighbor_pos)
            frontier = new_frontier
        self.distance = distances
        # self.debug_grid(self.grid)
        return distances