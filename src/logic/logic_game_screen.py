"""Play game."""
from ..mazedisplay import DisplayMaze
from ..box import Box
from ..animation.pacman_icone import PacmanIcone


class LogicGameScreen:
    """Play game."""


    def __init__(self, maze_display: DisplayMaze,) -> None:
        """Init PlayGame."""
        self.maze: DisplayMaze = maze_display
        self.grid: list[list[Box]] = maze_display.grid_display
        self.cell_size: int = self.get_cell_size()

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
    def convert_cell_to_px(x: int, y: int, cell_size: int, x_center_maze: int) -> tuple[int]:
        """Convert x_grid to player_px pixel of pacman."""
        player_px: int = (x * cell_size) + x_center_maze
        player_py: int = (y * cell_size) + 100
        return player_px, player_py
    
    @staticmethod
    def convert_px_to_cel(px: int, py: int, cell_size: int, x_center_maze: int) -> tuple[int]:
        """Convert player_px of pacman to x_grid."""
        x: int = (px - x_center_maze) // cell_size
        y: int = (py - 100) // cell_size
        return x, y



    # def play_screen(self) -> None:
    #     pygame.init()
    #     clock = pygame.time.Clock()
    #     screen = pygame.display.set_mode(self.screen_size)

    #     small_font = pygame.font.SysFont("arial", 20)
    #     cell_size = self.cell_size
    #     player = ScorePlayer("oussama")

    #     logo_img, size_logo = MenuIcone.logo_pacman(300)
    #     pacman_img: pygame.Surface = PacmanIcone.dir_pacman()

    #     grid_x, grid_y = self.position_pacman()

    #     player_px = (grid_x * cell_size) + self.x_maze_center
    #     player_py = (grid_y * cell_size) + 100

    #     for speed in range(3, 4):
    #         if cell_size % speed == 0:
    #             break

    #     direction: tuple[int] = (0, 0)
    #     next_dir: tuple[int] = (0, 0)

    #     # while runing:

    #         grid_x = (player_px - self.x_maze_center) // cell_size
    #         grid_y = (player_py - 100) // cell_size

    #         current_x = (player_px - self.x_maze_center) % cell_size == 0
    #         current_y = (player_py - 100) % cell_size == 0

    #         if next_dir:
    #             try:
    #                 pacman_img = PacmanIcone.dir_pacman(Direction.get_dir(next_dir))
    #             except KeyError:
    #                 pass

    #         if current_x and current_y:
    #             if self.can_move(grid_x, grid_y, next_dir, self.grid):
    #                 direction = next_dir

    #             if not self.can_move(grid_x, grid_y, direction, self.grid):
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