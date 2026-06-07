"""Get Pacman image for animation."""
import pygame


class MenuIcone:
    """Get Pacman image for animation."""

    @classmethod
    def logo_pacman(cls, size: int) -> pygame.Surface:
        """Get image logo pacman."""
        width: int = size
        height: int = width * (20 / 100)
        logo_img = pygame.image.load("./images/pacman-logo/logo.png").convert_alpha()
        logo_img = pygame.transform.scale(logo_img, (width, height))
        return logo_img
    
    @classmethod
    def cursor_pacman(cls, size: int) -> pygame.Surface:
        """Get icone cursor pacman."""
        cursor_img = pygame.image.load("./images/cursor/cursor.png").convert_alpha()
        cursor_img = pygame.transform.scale(cursor_img, (size, size))
        return cursor_img
    
    @classmethod
    def background_menu(cls, size: int) -> pygame.Surface:
        """Get background menu."""
        bg_menu = pygame.image.load("./images/background_menu/background_menu.png").convert_alpha()
        bg_menu = pygame.transform.scale(bg_menu, (size, size))
        return bg_menu

