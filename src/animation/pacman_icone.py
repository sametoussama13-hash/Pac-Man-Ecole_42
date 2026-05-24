"""Get Pacman image for animation."""
import pygame


class PacmanIcone:
    """Get Pacman image for animation."""

    CELL_SIZE: int = 0

    @classmethod
    def dir_pacman(cls, dir: int | None = None) -> list[pygame.Surface]:
        if dir == pygame.K_RIGHT or not dir:
            pacman_img = cls.img_surface_pacman(cls.CELL_SIZE, "est")
        elif dir == pygame.K_LEFT:
            pacman_img = cls.img_surface_pacman(cls.CELL_SIZE, "west")
        elif dir == pygame.K_DOWN:
            pacman_img = cls.img_surface_pacman(cls.CELL_SIZE, "south")
        elif dir == pygame.K_UP:
            pacman_img = cls.img_surface_pacman(cls.CELL_SIZE, "north")
        return pacman_img

    @classmethod
    def img_surface_pacman(cls, size_cell: int,
                           dir: str) -> list[pygame.Surface]:
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
            pygame.transform.scale(img, (size_cell, size_cell)) for
            img in pacman_img
        ]
        return pacman_img

    @classmethod
    def super_pacgum(cls) -> tuple[pygame.Surface, int]:
        cell_size: int = (cls.CELL_SIZE * 70) // 100
        s_pacgum: pygame.Surface = pygame.image.load("./images/s_pacgum/s_pacgum.png").convert_alpha()
        s_pacgum: pygame.Surface = pygame.transform.scale(s_pacgum, (cell_size, cell_size))
        return s_pacgum, cell_size

    @classmethod
    def pacgum(cls) -> tuple[pygame.Surface, int]:
        cell_size: int = (cls.CELL_SIZE * 20) // 100
        s_pacgum: pygame.Surface = pygame.image.load("./images/s_pacgum/s_pacgum.png").convert_alpha()
        s_pacgum: pygame.Surface = pygame.transform.scale(s_pacgum, (cell_size, cell_size))
        return s_pacgum, cell_size
