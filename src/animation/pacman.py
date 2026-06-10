"""Get Pacman image for animation."""
from ..box import Box
from ..direction import Direction
import pygame


class Pacman:
    """Get Pacman image for animation."""

    dict_img: dict[pygame.Surface] = {}

    def __init__(self, speed, cell_size: int,
                 maze_x: int, maze: list[list[Box]]) -> None:
        from ..logic import LogicDisplayScreen

        Pacman.dir_pacman()
        self.x, self.y = LogicDisplayScreen.position_pacman(maze)
        self.speed = speed
        self.cell_size = cell_size
        self.maze_x = maze_x
        self.player_x, self.player_y = self.get_pacman_start()
        self.next_dir: tuple[int] | None = (0, 0)
        self.direction: tuple[int] = (0, 0)
        self.maze = maze
        self.pacman_img: pygame.Surface = Pacman.dict_img["est"]
        self.index: int = 0

    def get_pacman_start(self) -> tuple[int]:
        """Get pacman start posiotion."""
        from ..logic import LogicGameScreen
        return LogicGameScreen.convert_cell_to_px(self.x, self.y,
                                                  self.cell_size, self.maze_x)
    
    def update_pacman(self) -> None:
        """Update pacman."""
        from ..logic import LogicGameScreen
        self.x, self.y = LogicGameScreen.convert_px_to_cel(self.player_x,
                                                           self.player_y,
                                                           self.cell_size,
                                                           self.maze_x,)

        current_x = (self.player_x - self.maze_x) % self.cell_size < self.speed
        current_y = (self.player_y - 100) % self.cell_size < self.speed

        if current_x and current_y:
            if LogicGameScreen.can_move(self.x, self.y, self.next_dir,
                                        self.maze):
                self.direction = self.next_dir
                if self.next_dir:
                    try:
                        self.pacman_img = Pacman.dict_img[
                            Direction.get_dir(self.next_dir)]
                    except KeyError:
                        pass

            if not LogicGameScreen.can_move(self.x, self.y, self.direction,
                                            self.maze):
                self.direction = (0, 0)

        self.player_x += self.direction[0] * self.speed
        self.player_y += self.direction[1] * self.speed

    def draw_pacman(self, screen: pygame.Surface):
        """display pacman"""

        if self.index >= len(self.pacman_img):
            self.index = 0

        screen.blit(self.pacman_img[self.index],
                    (self.player_x, self.player_y))

        self.index += 1

    @classmethod
    def dir_pacman(cls) -> None:
        """Get ani;"""
        from ..logic import LogicDisplayScreen
        list_direction: list[str] = ["north", "est", "south", "west"]
        for dir in list_direction:
            pacman_img: list[pygame.Surface] = [
                        pygame.image.load(f"./images/pacman/{dir}/pac-man_1.png").
                        convert_alpha(),
                        pygame.image.load(f"./images/pacman/{dir}/pac-man_2.png").
                        convert_alpha(),
                        pygame.image.load(f"./images/pacman/{dir}/pac-man_3.png").
                        convert_alpha(),
                        pygame.image.load(f"./images/pacman/{dir}/pac-man_3.png").
                        convert_alpha(),
                        pygame.image.load(f"./images/pacman/{dir}/pac-man_2.png").
                        convert_alpha()
                    ]
            pacman_img: list[pygame.Surface] = [
                pygame.transform.scale(img, (LogicDisplayScreen.CELL_SIZE,
                                             LogicDisplayScreen.CELL_SIZE)) for
                img in pacman_img
            ]
            cls.dict_img[dir] = pacman_img
