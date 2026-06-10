import pygame
from ..box import Box


class PacGum:
    """Class PacGum."""
    dict_img_pac: dict[pygame.Surface] = {}

    def __init__(self, grid: list[list[Box]],
                 cell_size: int,
                 maze_x: int) -> None:
        """Init PacGum."""
        self.save_pacgum_img_in_dict()
        self.grid = grid
        self.cell_size = cell_size
        self.maze_x = maze_x
        self.total_pacgum: int = self.count_pacgum()

    def count_pacgum(self) -> None:
        """Count all pacgum."""
        total_pacgum: int = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x].pacgum or self.grid[y][x].super_pacgum:
                    total_pacgum += 1
        return total_pacgum

    def save_pacgum_img_in_dict(self) -> None:
        """Update dict img pacgum."""
        list_pacgum: list[str] = ["super_pacgum", "pacgum"]
        for pacgum in list_pacgum:
            if pacgum == "super_pacgum":
                PacGum.dict_img_pac[pacgum] = PacGum.img_pacgum(70)
            elif pacgum == "pacgum":
                PacGum.dict_img_pac[pacgum] = PacGum.img_pacgum(20)

    @classmethod
    def img_pacgum(cls, ratio: int) -> tuple[pygame.Surface, int]:
        from ..logic import LogicDisplayScreen
        cell_size: int = LogicDisplayScreen.CELL_SIZE
        size: int = (cell_size * ratio) // 100
        s_pacgum: pygame.Surface = pygame.image.load(
            "./images/s_pacgum/s_pacgum.png").convert_alpha()
        s_pacgum: pygame.Surface = pygame.transform.scale(s_pacgum,
                                                          (size,
                                                           size))
        position: int = LogicDisplayScreen.get_center_position(cell_size, size)
        return s_pacgum, position

    def update_pacgum(self, x: int, y: int) -> None:
        """Update pacgum."""
        if self.grid[y][x].super_pacgum:
            self.grid[y][x].super_pacgum = False
            self.total_pacgum -= 1

        if self.grid[y][x].pacgum:
            self.grid[y][x].pacgum = False
            self.total_pacgum -= 1

    def draw_pacgum(self, screen: pygame.Surface) -> None:
        """Draw PacGum."""
        grid: list[list[Box]] = self.grid
        cell_size: int = self.cell_size
        for col in range(len(grid)):
            for row in range(len(grid[0])):
                x = (row * cell_size) + self.maze_x
                y = (col * cell_size) + 100
                if grid[col][row].super_pacgum:
                    s_pcg, s_pcg_pos = PacGum.dict_img_pac["super_pacgum"]
                    screen.blit(s_pcg, (x + s_pcg_pos, y + s_pcg_pos,
                                        cell_size, cell_size))
                elif grid[col][row].pacgum:
                    s_pcg, s_pcg_pos = PacGum.dict_img_pac["pacgum"]
                    screen.blit(s_pcg, (x + s_pcg_pos, y + s_pcg_pos,
                                        cell_size, cell_size))

