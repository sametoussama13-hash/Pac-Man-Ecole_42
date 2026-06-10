import pygame
from .ghost import Ghost
from ..logic import LogicDisplayScreen, LogicGameScreen
from ..box import Box
from ..solver import Glouton
from math import sqrt

# je dois faire une class pour pouvoir creer mes icone de ghost plus facilement
# je pouurrais ensuite verifier mes algo et commencer a tester
# mes ghost vers mon pacman


class Blinky(Ghost):

    def __init__(self, grid: list[list[Box]], cell_size: int, maze_x: int):
        super().__init__(grid, cell_size)
        self.speed = 2
        self.maze_x = maze_x
        self.is_speeded = False
        self.cell_pos: tuple[int, int] = self.find_spawn(grid)
        self.px, self.py = LogicGameScreen.convert_cell_to_px(
            self.pos[0], self.pos[1], cell_size, maze_x)
        self.target_px, self.target_py = self.px, self.py
        self.target_cell: tuple[int, int] = self.cell_pos
        self.algo: Glouton = Glouton(grid)
        self.ghost_img: pygame.Surface = self.dir_ghost("blinky")[0]

    def update_blinky(self, pacman_pos) -> int:

        dx = self.target_px - self.px
        dy = self.target_py - self.py
        dist = sqrt(dx * dx + dy * dy)

        if dist <= self.speed:
            self.px, self.py = float(self.target_px), float(self.target_py)
            self.cell_pos = self.target_cell

            if self.cell_pos == pacman_pos:
                self.eaten()
                return -1

            direction = self.algo.algo(pacman_pos, self.cell_pos)
            next_col = self.cell_pos[0] + direction[0]
            next_row = self.cell_pos[1] + direction[1]
            self.target_cell = (next_col, next_row)
            self.target_px, self.target_py = LogicGameScreen.convert_cell_to_px(
                next_col, next_row, self.cell_size, self.maze_x,)
        else:
            self.px += (dx / dist) * self.speed
            self.py += (dy / dist) * self.speed

    def draw_blinky(self, screen: pygame.Surface) -> None:
        """Draw linky."""
        screen.blit(self.ghost_img, (self.px, self.py))
        print(f"Blinky at pos: x: {self.px}, {self.py}")

    def dir_ghost(self, name: str) -> list[pygame.Surface]:
        ghost_img = self.img_surface_ghost(name, LogicDisplayScreen.CELL_SIZE)
        return ghost_img

    def img_surface_ghost(self,  name: str, size_cell: int,
                           ) -> list[pygame.Surface]:
        print(f"name {name}")
        ghost_img: list[pygame.Surface] = [
                    pygame.image.load(f"./images/ghosts/{name}.png")
                ]
        ghost_img: list[pygame.Surface] = [
            pygame.transform.scale(img, (size_cell, size_cell)) for
            img in ghost_img
        ]
        return ghost_img
