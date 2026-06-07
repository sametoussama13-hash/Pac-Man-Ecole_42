"""Play game."""
from ..box import Box
from ..animation.pacman_icone import PacmanIcone


class LogicGameScreen:
    """Play game."""

    @staticmethod
    def get_cell_size(size_screen: tuple[int], grid: list[list[Box]]) -> int:
        """Adapte cell size withe screen size."""
        width = len(grid[0])
        width_screen = size_screen[0]
        cell_size = int((45 * ((width_screen - 200) / width)) /
                        ((width_screen - 200) / 15))
        PacmanIcone.CELL_SIZE = cell_size
        return PacmanIcone.CELL_SIZE

    @staticmethod
    def can_move(x: int, y: int,
                 d: tuple[int], grid: list[list[Box]]) -> bool:
        """Check if pacman can move."""
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            return grid[ny][nx].type_box != 1
        return False

    @staticmethod
    def convert_cell_to_px(x: int, y: int, cell_size: int,
                           x_center_maze: int) -> tuple[int]:
        """Convert x_grid to player_px pixel of pacman."""
        player_px: int = (x * cell_size) + x_center_maze
        player_py: int = (y * cell_size) + 100
        return player_px, player_py

    @staticmethod
    def convert_px_to_cel(px: int, py: int, cell_size: int,
                          x_center_maze: int) -> tuple[int]:
        """Convert player_px of pacman to x_grid."""
        x: int = (px - x_center_maze) // cell_size
        y: int = (py - 100) // cell_size
        return x, y
