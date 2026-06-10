from ..parsing_conf import LevelConfig
from ..play_game import Screen
from ..logic import LogicDisplayScreen
from ..animation.menu_icone import MenuIcone
from ..animation import Pacman, Maze, PacGum
from ..score import ScorePlayer
from ..ghosts import Blinky

from .game_over_screen import GameOverScreen
from .pause_screen import PauseScreen
import pygame


class GameScreen(Screen):
    """Display Screen play."""

    def __init__(self, config_level: list[LevelConfig],
                 screen_size: tuple[int] = (800, 800)) -> None:
        """Init Game screen"""
        self.index_level: int = 0
        self.next_screen = None
        self.screen_size = screen_size
        self.list_level: list[LevelConfig] = config_level

        self.config_level: LevelConfig = config_level[self.index_level]
        self.speed: int = self.config_level.speed
        self.maze: Maze = self.get_maze_object()
        self.cell_size = LogicDisplayScreen.CELL_SIZE
        self.maze_x = self.maze.maze_x
        self.pacman: Pacman = self.get_pacman_object()
        self.pacgum: PacGum = self.get_pacgum_object()
        self.blinky: Blinky = self.get_blinky_object()
        self.timer = 0

    def get_blinky_object(self) -> Blinky:
        """Get blinky object."""
        return Blinky(self.maze.grid, self.cell_size, self.maze_x)

    def get_pacgum_object(self) -> PacGum:
        """Get PacGum object."""
        return PacGum(self.maze.grid, self.cell_size, self.maze_x)

    def get_pacman_object(self) -> Pacman:
        """Get pacman object."""
        return Pacman(self.speed, self.cell_size, self.maze_x, self.maze.grid)

    def get_maze_object(self):
        """Get maze object."""
        from ..animation import Maze
        return Maze(self.config_level, self.screen_size)

    def next_level(self) -> None:
        """Get next level."""
        self.index_level += 1
        self.config_level = self.list_level[self.index_level]
        self.speed = self.config_level.speed
        self.maze = self.get_maze_object()
        self.cell_size = LogicDisplayScreen.get_cell_size(self.screen_size, self.maze.grid)
        self.maze_x = self.maze.maze_x
        self.pacman = self.get_pacman_object()
        self.pacgum = self.get_pacgum_object()
        self.blinky: Blinky = self.get_blinky_object()
        self.timer = 0
        # self.linky= Linky(self.config_level.linky)

    def handle_event(self, event: pygame.event.Event) -> None:
        """Handel event."""
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_LEFT:
            self.pacman.next_dir = (-1, 0)
        elif event.key == pygame.K_RIGHT:
            self.pacman.next_dir = (1, 0)
        elif event.key == pygame.K_UP:
            self.pacman.next_dir = (0, -1)
        elif event.key == pygame.K_DOWN:
            self.pacman.next_dir = (0, 1)
        elif event.key == pygame.K_ESCAPE:
            screen_pause = [screen for screen in Screen.screens_list if isinstance(screen, PauseScreen)]
            if screen_pause:
                self.next_screen = screen_pause[-1]
            else:
                self.next_screen = PauseScreen()

    def update(self, dt) -> None:
        """Update timer."""
        self.timer += dt

        self.pacman.update_pacman()
        self.pacgum.update_pacgum(self.pacman.x, self.pacman.y)
        self.blinky.update_blinky((self.pacman.x, self.pacman.y))
        if self.timer > 100000:
            self.next_screen = GameOverScreen(self.config_level)
        if self.pacgum.total_pacgum == 0:
            self.next_level()

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((0, 0, 50))

        self.maze.draw_maze(screen)
        self.pacgum.draw_pacgum(screen)
        self.pacman.draw_pacman(screen)
        self.blinky.draw_blinky(screen)

        logo_img = MenuIcone.logo_pacman(300)
        x_position = LogicDisplayScreen.get_center_position(800, 300)

        screen.blit(logo_img, (x_position, 30))
