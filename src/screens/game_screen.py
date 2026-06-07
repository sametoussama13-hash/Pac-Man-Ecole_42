from ..parsing_conf import Config
from ..play_game import Screen
from ..logic import LogicGameScreen, LogicDisplayScreen
from ..box import Box
from .menu_screen import MenuScreen
from ..animation import PacmanIcone
from ..mazedisplay import DisplayMaze
from mazegenerator import MazeGenerator
from ..direction import Direction
from ..animation.menu_icone import MenuIcone
from ..score import ScorePlayer


from .game_over_screen import GameOverScreen
import pygame
import asyncio


class GameScreen(Screen):
    """Display Screen play."""

    def __init__(self, config: Config,
                 screen_size: tuple[int] = (800, 800)) -> None:
        """Init Game screen"""
        # self.font = pygame.font.SysFont("arial", 20)
        self.next_screen = None
        self.config = config
        self.config_levels = config.levels
        self.maze: list[list[Box]] = self.generate_maze()
        self.x, self.y = LogicDisplayScreen.position_pacman(self.maze)
        self.speed = 6  # pour l'instan
        self.cell_size = LogicGameScreen.get_cell_size(screen_size,
                                                       self.maze)
        self.maze_x = self.get_start_x_maze(screen_size)
        self.player_x, self.player_y = self.get_pacman_start()
        self.next_dir: tuple[int] | None = (0, 0)
        self.direction: tuple[int] = (0, 0)
        self.pacman_img: pygame.Surface = PacmanIcone.dir_pacman()
        self.timer = 0
        self.index = 0

    def get_start_x_maze(self, screen_size: tuple[int]) -> int:
        """Get start x maze."""
        return LogicDisplayScreen.get_center_maze(screen_size,
                                                  self.maze, self.cell_size)

    def get_pacman_start(self) -> tuple[int]:
        """Get pacman start posiotion."""
        return LogicGameScreen.convert_cell_to_px(self.x, self.y,
                                                  self.cell_size, self.maze_x)

    def generate_maze(self) -> DisplayMaze:
        """Generate maze."""
        width = self.config_levels[0].width
        height = self.config_levels[0].height
        size = (width, height)
        maze = MazeGenerator(size=size)
        maze_display = DisplayMaze(maze)
        return maze_display.grid_display

    def handle_event(self, event: pygame.event.Event) -> None:
        """Handel event."""
        if event.key == pygame.K_LEFT:
            self.next_dir = (-1, 0)
        elif event.key == pygame.K_RIGHT:
            self.next_dir = (1, 0)
        elif event.key == pygame.K_UP:
            self.next_dir = (0, -1)
        elif event.key == pygame.K_DOWN:
            self.next_dir = (0, 1)
        elif event.key == pygame.K_ESCAPE:
            self.next_screen = MenuScreen(self.config)
        else:
            self.next_dir = (0, 0)

    def update(self, dt) -> None:
        """Update timer."""
        self.timer += dt

        if self.timer > 5:
            self.next_screen = GameOverScreen()

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((0, 0, 50))

        self.display_maze(screen)
        self.display_pacman(screen)

        logo_img = MenuIcone.logo_pacman(300)
        x_position = LogicDisplayScreen.get_center_position(800, 300)

        screen.blit(logo_img, (x_position, 30))

    def display_pacman(self, screen: pygame.Surface):
        """display pacman"""
        self.x, self.y = LogicGameScreen.convert_px_to_cel(self.player_x, self.player_y, self.cell_size, self.maze_x)

        current_x = (self.player_x - self.maze_x) % self.cell_size < self.speed
        current_y = (self.player_y - 100) % self.cell_size < self.speed

        if current_x and current_y:
            if LogicGameScreen.can_move(self.x, self.y, self.next_dir, self.maze):
                self.direction = self.next_dir
                if self.next_dir:
                    try:
                        self.pacman_img = PacmanIcone.dir_pacman(Direction.get_dir(self.next_dir))
                    except KeyError:
                        pass

            if not LogicGameScreen.can_move(self.x, self.y, self.direction, self.maze):
                self.direction = (0, 0)

        self.player_x += self.direction[0] * self.speed
        self.player_y += self.direction[1] * self.speed

        if self.index >= len(self.pacman_img):
            self.index = 0

        screen.blit(self.pacman_img[self.index], (self.player_x, self.player_y))

        if self.maze[self.y][self.x].super_pacgum:
            self.maze[self.y][self.x].super_pacgum = False

        if self.maze[self.y][self.x].pacgum:
            self.maze[self.y][self.x].pacgum = False

        self.index += 1

    def display_maze(self, screen: pygame.Surface) -> None:
        cell_size = self.cell_size
        grid = self.maze

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
                elif grid[col][row].super_pacgum:
                    s_pacgum, cell_spacgum = PacmanIcone.super_pacgum()
                    s_pacgum_position = (LogicDisplayScreen.get_center_position
                                         (cell_size, cell_spacgum))
                    screen.blit(s_pacgum, (x + s_pacgum_position,
                                           y + s_pacgum_position,
                                           cell_size, cell_size))
                elif grid[col][row].pacgum:
                    pacgum, cell_pacgum = PacmanIcone.pacgum()
                    pacgum_position = (LogicDisplayScreen.get_center_position
                                       (cell_size, cell_pacgum))
                    screen.blit(pacgum, (x + pacgum_position,
                                         y + pacgum_position,
                                         cell_size, cell_size))
                else:
                    color = (0, 0, 0)
                    pygame.draw.rect(screen, color, (x, y, cell_size,
                                                     cell_size))





















    # def play_screen(self) -> None:
    #     pygame.init()
    #     clock = pygame.time.Clock()
    #     screen = pygame.display.set_mode(self.screen_size)

    #     small_font = pygame.font.SysFont("arial", 20)
    #     cell_size = self.cell_size
    #     print("cell_size", cell_size)
    #     player = ScorePlayer("oussama")

        
    #     pacman_img: pygame.Surface = PacmanIcone.dir_pacman()

    #     grid_x, grid_y = self.position_pacman()

    #     player_px = (grid_x * cell_size) + self.x_maze_center
    #     player_py = (grid_y * cell_size) + 100

    #     speed = 4

    #     direction: tuple[int] = (0, 0)
    #     next_dir: tuple[int] = (0, 0)

    #     runing = True
    #     index: int = 0

    #     while runing:

    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 runing = False
    #             if event.type == pygame.KEYDOWN:
    #                 result = self.key_direction(event)
    #                 if result:
    #                     next_dir = result

    #         grid_x = (player_px - self.x_maze_center) // cell_size
    #         grid_y = (player_py - 100) // cell_size

    #         current_x = (player_px - self.x_maze_center) % cell_size == 0
    #         current_y = (player_py - 100) % cell_size == 0

    #         if current_x and current_y:

    #             if self.can_move(grid_x, grid_y, next_dir, grid):
    #                 try:
    #                     pacman_img = PacmanIcone.dir_pacman(Direction.
    #                                                         get_dir(next_dir))
    #                 except KeyError:
    #                     pass
    #                 direction = next_dir

    #             if not self.can_move(grid_x, grid_y, direction, grid):
    #                 direction = (0, 0)
        
    #         player_px += direction[0] * speed
    #         player_py += direction[1] * speed

    #         # score display
    #         # name = small_font.render(str(player.name), True, (255, 255, 0))
    #         # score = small_font.render(str(player.score), True, (255, 255, 0))

    #         screen.fill((0, 0, 0))

    #         # logo_x = self.get_center_menu_screen(size_logo)
    #         # screen.blit(logo_img, (logo_x, 10))
    #         # screen.blit(name, (self.x_display_center, 20))
    #         # screen.blit(score, (self.x_display_center, 40))

    #         self.display_maze(screen)

    #         if index >= len(pacman_img):
    #             index = 0
            
    #         # player_x_center = player_x + self.x_display_center
    #         screen.blit(pacman_img[index], (player_px, player_py))

    #         # if self.grid[player_y][player_x].super_pacgum:
    #         #     self.grid[player_y][player_x].super_pacgum = False
    #         #     player.add_s_pacgum_score()

    #         # if self.grid[player_y][player_x].pacgum:
    #         #     self.grid[player_y][player_x].pacgum = False
    #         #     player.add_pacgum_score()

    #         index += 1

    #         pygame.display.update()
    #         clock.tick(60)

    # pygame.quit()
