from abc import ABC, abstractmethod
from ..logic import LogicGameScreen
from typing import Optional
# from ..screen import PlayGame
from ..box import Box

DIRECTIONS: list[tuple[int, int]] = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # up, down, left, right


class Solver(ABC):
    def __init__(self, grid: list[list[Box]]) -> None:
        self.grid: list[list[Box]] = grid
        self.distance: dict[tuple[int, int], int] = {}

    @abstractmethod
    def algo(self) -> None:
        pass

    def debug_grid(self, grid: list[list[Box]]) -> None:
        for y, row in enumerate(grid):
            line: str = ""
            for box in row:
                line += "#" if box.type_box == 1 else "."
            print(f"{y:2d} {line}")

    # def can_move(self, x: int, y: int,
    #              d: tuple[int, int], grid: list[list[Box]]) -> bool:
    #     nx, ny = x + d[0], y + d[1]
    #     if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
    #         return grid[ny][nx].type_box != 1
    #     return False


    # TODO this function will be usefull for founding a position in front of pacman
    def get_after_pacman_pos(self, cell: tuple[int, int], direction: tuple[int , int], closseness: int) -> Optional[tuple[int, int]]:
        x, y = cell
        curr_cell = x, y 
        next = self.get_neighbor(self, cell, direction)
        pass


    # TODO this function will get the pos at the left down of the grid
    def get_left_down_pos(self):
        pass


    def get_neighbor(self, cell: tuple[int, int], direction: tuple[int, int]) -> Optional[tuple[int, int]]:
        x, y = cell
        if LogicGameScreen.can_move(x, y, direction, self.grid):
            return True
        return False
    
    def get_after_pos(self, cell: tuple[int, int], direction: tuple[int, int]) -> Optional[tuple[tuple[int, int]]]:
        x, y = cell
        output: list

    def get_neighbors(self, cell: tuple[int, int]) -> list[tuple[int, int]]:
        output: list[tuple[int, int]] = []
        for direction in DIRECTIONS:
            if self.get_neighbor(cell, direction):
                output.append(direction)
        return output

    def path_to(self, start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
        curr: tuple[int, int] = end
        output: list[tuple[int, int]] = [end]
        visited: set[tuple[int, int]] = {end}
        while curr != start:
            x, y = curr
            moved: bool = False
            for neighbor_pos in self.get_neighbors((x, y)):
                if neighbor_pos not in visited and \
                        self.distance.get(neighbor_pos) == self.distance.get(curr, 0) - 1:
                    output.append(neighbor_pos)
                    visited.add(neighbor_pos)
                    curr = neighbor_pos
                    moved = True
                    break
            if not moved:
                print(f"path_to blocked at {curr}, no neighbor found toward start")
                break
        output.reverse()
        return output
