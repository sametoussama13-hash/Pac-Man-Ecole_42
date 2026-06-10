"""Play game."""
from ..box import Box


class LogicGameScreen:
    """Play game."""

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
