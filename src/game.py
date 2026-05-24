import pygame
from .mazedisplay import DisplayMaze
from .box import Box
from .animation.pacman_icone import PacmanIcone
from .score import ScoreGamer, ScorePlayer


class ErrorGamePlay(Exception):
    """Raise Error Game play."""
    pass


class PlayGame:

    def __init__(
            self, maze_display: DisplayMaze,
            screen_size: tuple[int] = (800, 800)) -> None:
        """Init PlayGame."""
        self.screen_size = screen_size
        self.maze = maze_display
        self.grid = maze_display.grid_display
        self.cell_size = self.get_cell_size()
        self.x_display_center = self.get_center_screen()

    def get_cell_size(self) -> int:
        """Adapte cell size withe screen size."""
        width = len(self.grid[0])
        width_screen = self.screen_size[0]
        PacmanIcone.CELL_SIZE = int((50 * ((width_screen - 200) / width)) /
                                    ((width_screen - 200) / 15))
        return PacmanIcone.CELL_SIZE

    def get_cell_position(self, size_object: int) -> int:
        """get position objetc."""
        return (self.cell_size - size_object) // 2
    
    def get_center_screen(self) -> int:
        """centre maze screen."""
        return (self.screen_size[0] - (len(self.grid[0]) * self.cell_size)) // 2

    def position_pacman(self) -> tuple[int]:
        """Get center position start of pacman."""
        x = len(self.grid[0]) // 2
        y = len(self.grid) // 2

        for x in range(x, len(self.grid[0])):
            if self.grid[y][x].type_box == 0:
                break
        return x, y

    def can_move(self, x: int, y: int,
                 d: tuple[int], grid: list[list[Box]]) -> bool:
        """Check if pacman can move."""
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            return grid[ny][nx].type_box != 1
        return False

    def display_screen(self, screen: pygame.Surface) -> None:
        cell_size = self.cell_size
        for col in range(len(self.grid)):
            for row in range(len(self.grid[0])):
                x = (row * cell_size) + self.x_display_center
                y = (col * cell_size) + 70

                if self.grid[col][row].type_box == 1:
                    color = (0, 0, 255)
                    pygame.draw.rect(screen, color, (x, y, cell_size,
                                                     cell_size))

                elif self.grid[col][row].type_box == 2:
                    color = (255, 255, 0)
                    pygame.draw.rect(screen, color, (x, y, cell_size,
                                                     cell_size))

                elif self.grid[col][row].super_pacgum:
                    s_pacgum, cell_spacgum = PacmanIcone.super_pacgum()
                    s_pacgum_position = self.get_cell_position(cell_spacgum)
                    screen.blit(s_pacgum, (x + s_pacgum_position,
                                           y + s_pacgum_position,
                                           cell_size, cell_size))

                elif self.grid[col][row].pacgum:
                    pacgum, cell_pacgum = PacmanIcone.pacgum()
                    pacgum_position = self.get_cell_position(cell_pacgum)
                    screen.blit(pacgum, (x + pacgum_position,
                                         y + pacgum_position,
                                         cell_size, cell_size))

                else:
                    color = (0, 0, 0)
                    pygame.draw.rect(screen, color, (x, y, cell_size,
                                                     cell_size))

    def key_direction(self, event: pygame.event.Event,
                      next_direction: tuple[int, int]
                      ) -> tuple[tuple[int, int], pygame.Surface]:
        """Get next direction and animation pacman."""
        if event.key == pygame.K_LEFT:
            next_direction = (-1, 0)
            pacman_img = PacmanIcone.dir_pacman(event.key)
        elif event.key == pygame.K_RIGHT:
            next_direction = (1, 0)
            pacman_img = PacmanIcone.dir_pacman(event.key)
        elif event.key == pygame.K_UP:
            next_direction = (0, -1)
            pacman_img = PacmanIcone.dir_pacman(event.key)
        elif event.key == pygame.K_DOWN:
            next_direction = (0, 1)
            pacman_img = PacmanIcone.dir_pacman(event.key)
        else:
            return None
        return next_direction, pacman_img

    def play_screen(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(self.screen_size)
        font = pygame.font.Font(None, 60)
        small_font = pygame.font.SysFont("arial", 20)
        cell_size = self.cell_size
        player = ScorePlayer("oussama")
        pacman_img: pygame.Surface = PacmanIcone.dir_pacman()

        player_x, player_y = self.position_pacman()
        direction: tuple[int] = (0, 0)
        next_dir: tuple[int] = (0, 0)

        runing = True
        index: int = 0

        while runing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runing = False
                if event.type == pygame.KEYDOWN:
                    if self.key_direction(event, next_dir):
                        next_dir, pacman_img = self.key_direction(event,
                                                                  next_dir)

            if self.can_move(player_x, player_y, next_dir, self.grid):
                direction = next_dir

            if self.can_move(player_x, player_y, next_dir, self.grid):
                player_x += direction[0]
                player_y += direction[1]

            

            #score display
            title = font.render("PAC-MAN", True, (255, 255, 0)) 
            name = small_font.render(str(player.name), True, (255, 255, 0))
            score = small_font.render(str(player.score), True, (255, 255, 0))

            screen.fill((0, 0, 0))

            screen.blit(title, (300, 10))
            screen.blit(name, (self.x_display_center, 20))
            screen.blit(score, (self.x_display_center, 40))

            self.display_screen(screen)

            if index >= len(pacman_img):
                index = 0
            player_x_center = (player_x * cell_size) + self.x_display_center
            screen.blit(pacman_img[index],
                        (player_x_center, (player_y * cell_size) + 70))

            if self.grid[player_y][player_x].super_pacgum:
                self.grid[player_y][player_x].super_pacgum = False
                player.add_s_pacgum_score()

            if self.grid[player_y][player_x].pacgum:
                self.grid[player_y][player_x].pacgum = False
                player.add_pacgum_score()

            index += 1

            pygame.display.update()
            clock.tick(10)

    pygame.quit()


def play_game(maze_display: DisplayMaze) -> int:
    try:
        play_game = PlayGame(maze_display)
        play_game.play_screen()
    except ErrorGamePlay as e:
        print(e)
        return 1
    return 0
