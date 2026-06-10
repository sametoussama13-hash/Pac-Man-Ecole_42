from .algo import Solver
from ..box import Box


class BFS(Solver):
    def __init__(self, grid: list[list[Box]]) -> None:
        super().__init__(grid)

    def algo(self) -> None:
        pass
