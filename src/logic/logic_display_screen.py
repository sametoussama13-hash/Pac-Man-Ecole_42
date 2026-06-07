"""Get screen parameters."""
from ..box import Box
# from ..mazedisplay import DisplayMaze
from ..animation.pacman_icone import PacmanIcone
import pygame

class LogicDisplayScreen:
    """Get screen parameters."""

    @staticmethod
    def get_center_position(size: int, size_object: int) -> int:
        """Get position objetc."""
        return (size - size_object) // 2

    @staticmethod
    def position_pacman(grid: list[list[Box]]) -> tuple[int]:
        """Get center position start of pacman."""
        x = len(grid[0]) // 2
        y = len(grid) // 2

        for x in range(x, len(grid[0])):
            if grid[y][x].type_box == 0:
                break
        return x, y
    
    @staticmethod
    def get_center_maze(screen_size: tuple[int], maze: list[list[Box]],
                        cell_size: int) -> int:
        """Centre maze screen."""
        return ((screen_size[0] - (len(maze[0]) * cell_size)) // 2)

