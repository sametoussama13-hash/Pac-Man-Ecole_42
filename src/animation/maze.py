from ..box import Box
from ..logic import LogicDisplayScreen
from ..parsing_conf import LevelConfig
from ..mazedisplay import DisplayMaze
from mazegenerator import MazeGenerator
import pygame


class Maze:
    """Class Maze."""

    def __init__(self, config_level: LevelConfig, screen_size: int):
        """Init Maze."""
        self.config_level = config_level
        self.screen_size = screen_size
        self.grid: list[list[Box]] = self.generate_maze()
        self.cell_size = LogicDisplayScreen.get_cell_size(screen_size,
                                                          self.grid)
        self.maze_x = self.get_start_x_maze()

    def get_start_x_maze(self) -> int:
        """Get start x maze."""
        from ..logic import LogicDisplayScreen
        return LogicDisplayScreen.get_center_maze(self.screen_size,
                                                  self.grid, self.cell_size)

    def generate_maze(self) -> MazeGenerator:
        """Generate maze."""
        width = self.config_level.width
        height = self.config_level.height
        size = (width, height)
        maze = MazeGenerator(size=size)
        maze_display = DisplayMaze(maze)
        return maze_display.grid_display

    def draw_maze(self, screen: pygame.Surface) -> None:
        """Draw Maze."""
        cell_size = self.cell_size
        grid = self.grid
        for col in range(len(grid)):
            for row in range(len(grid[0])):
                x = (row * cell_size) + self.maze_x
                y = (col * cell_size) + 100
                if grid[col][row].type_box == 1:
                    color = (0, 0, 255)
                    pygame.draw.rect(screen, color, (x, y, cell_size,
                                                     cell_size))
                elif grid[col][row].type_box == 2:
                    color = (255, 255, 0)
                    pygame.draw.rect(screen, color, (x, y, cell_size,
                                                     cell_size))
