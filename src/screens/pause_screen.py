"""Display menu."""
from ..parsing_conf import LevelConfig
from ..play_game import Screen
from ..logic import LogicDisplayScreen
from ..animation.menu_icone import MenuIcone
import pygame


class PauseScreen(Screen):
    """Display menu."""

    def __init__(self, level_config: LevelConfig | None = None) -> None:
        """Init Game screen"""
        self.font = pygame.font.Font("./font/PressStart2P.ttf", 30)
        self.config_level = level_config
        self.next_screen = None
        self.size_logo: int = 500
        self.size_cursor: int = 30
        self.list_choice = []
        self.index: int = 0
        self.timer = 0

    def handle_event(self, event: pygame.event.Event) -> None:
        """Handel event."""
        from .game_screen import Screen
        if event.key == pygame.K_SPACE:
            if self.index == 0:
                self.next_screen = Screen.screens_list[-2]
                return
            if self.index == 1:
                self.next_screen = Screen.screens_list[0]
                return
        if event.key == pygame.K_DOWN:
            if self.index < (len(self.list_choice) - 1):
                self.index += 1
        if event.key == pygame.K_UP:
            if self.index > 0:
                self.index -= 1

    def update(self, dt) -> None:
        """Update timer."""
        pass

    def draw(self, screen: pygame.Surface) -> None:
        """Draw screen."""

        # Overlay screen
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 50, 120))
        screen.blit(overlay, (0, 0))

        # Name pacman
        logo_img = MenuIcone.logo_pacman(self.size_logo)
        logo_x = LogicDisplayScreen.get_center_position(screen.get_width(), self.size_logo)
        logo_y = 70
        screen.blit(logo_img, (logo_x, logo_y))

        menu_list: list[str] = ["CONTINUE", "EXIT"]
        self.display_choice(screen, menu_list, 300)

        # cursor
        cursor_img = MenuIcone.cursor_pacman(self.size_cursor)
        cursor_x, cursor_y = self.list_choice[self.index]
        screen.blit(cursor_img, (cursor_x - 60, cursor_y))

    def display_choice(self, screen: pygame.Surface, menu_list: list[str], y: int) -> None:
        choice_y = y
        for menu in menu_list:
            choice = self.font.render(menu, True, (255, 234, 0))
            choice_x = LogicDisplayScreen.get_center_position(screen.get_width(), choice.get_width())
            choice_y = choice_y + (choice.get_height() * 2)
            screen.blit(choice, (choice_x, choice_y))
            if (choice_x, choice_y) not in self.list_choice:
                self.list_choice.append((choice_x, choice_y))