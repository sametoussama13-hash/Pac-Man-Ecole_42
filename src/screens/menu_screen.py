"""Display menu."""
from ..parsing_conf import Config
from ..play_game import Screen
from ..logic import LogicDisplayScreen
from ..animation.menu_icone import MenuIcone
import pygame


class MenuScreen(Screen):
    """Display menu."""

    def __init__(self, config: Config | None = None) -> None:
        """Init Game screen"""
        self.font = pygame.font.Font("./font/PressStart2P.ttf", 30)
        self.overlay = pygame.Surface(config.size_screen, pygame.SRCALPHA)
        self.config = config
        self.next_screen = None
        self.size_logo: int = 500
        self.size_cursor: int = 30
        self.cursor_x = 0
        self.cursor_y = 0
        self.timer = 0

    def handle_event(self, event: pygame.event.Event) -> None:
        """Handel event."""
        from .game_screen import GameScreen
        if event.key == pygame.K_SPACE:
            self.next_screen = GameScreen(self.config)
            Screen.add_screen(self.next_screen)
        if event.key == pygame.K_DOWN:
            self.y += 40

    def update(self, dt) -> None:
        """Update timer."""
        pass

    def draw(self, screen: pygame.Surface) -> None:
        """Draw screen."""
        # Backgroun
        bg_menu = MenuIcone.background_menu(screen.get_size()[0])
        screen.blit(bg_menu, (0, 0))

        # Overlay screen
        self.overlay.fill((0, 0, 50, 120))
        screen.blit(self.overlay, (0, 0))

        # Name pacman
        logo_img = MenuIcone.logo_pacman(self.size_logo)
        logo_x = LogicDisplayScreen.get_center_position(screen.get_width(), self.size_logo)
        logo_y = 70
        screen.blit(logo_img, (logo_x, logo_y))

        # Play
        play = self.font.render("PLAY", True, (255, 234, 0))
        play_x = LogicDisplayScreen.get_center_position(screen.get_width(), play.get_width())
        play_y = logo_y + logo_img.get_height() + 70
        screen.blit(play, (play_x, play_y))

        # cursor
        cursor_img = MenuIcone.cursor_pacman(self.size_cursor)
        cursor_x = play_x - 60
        cursor_y = play_y
        screen.blit(cursor_img, (cursor_x, cursor_y))

        # classement
        classments = self.font.render("CLASSEMENT", True, (255, 234, 0))
        classments_x = LogicDisplayScreen.get_center_position(screen.get_width(), classments.get_width())
        classments_y = play_y + play.get_height() + 30
        screen.blit(classments, (classments_x, classments_y))

        # Instructions
        instructions = self.font.render("INSTRUCTIONS", True, (255, 234, 0))
        instructions_x = LogicDisplayScreen.get_center_position(screen.get_width(), instructions.get_width())
        instructions_y = classments_y + classments.get_height() + 30
        screen.blit(instructions, (instructions_x, instructions_y))

        # Options
        options = self.font.render("OPTIONS", True, (255, 234, 0))
        options_x = LogicDisplayScreen.get_center_position(screen.get_width(), options.get_width())
        options_y = instructions_y + instructions.get_height() + 30
        screen.blit(options, (options_x, options_y))

        # Exit
        exit = self.font.render("EXIT", True, (255, 234, 0))
        exit_x = LogicDisplayScreen.get_center_position(screen.get_width(), exit.get_width())
        exit_y = options_y + options.get_height() + 30
        screen.blit(exit, (exit_x, exit_y))




    # def play_screen(self) -> None:
    #     """Play screen menu."""
    #     pygame.init()
    #     clock = pygame.time.Clock()
    #     screen = pygame.display.set_mode(self.screen_size)

    #     small_font = pygame.font.SysFont("arial", 35)
    #     cell_size = self.cell_size

    #     logo_img, size_logo = MenuIcone.logo_pacman(500)


    #     runing = True
    #     index: int = 0

    #     while runing:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 runing = False
    #             if event.type == pygame.KEYDOWN:
    #                 if self.key_direction(event):
    #                     next_dir = self.key_direction(event)

    #         name = small_font.render("Play", True, (255, 255, 0))
    #         score = small_font.render("Best Score", True, (255, 255, 0))

    #         screen.fill((0, 0, 0))

    #         # display logo Pac-Man
    #         logo_x = self.get_center_position(self.screen_size[0],
    #                                              size_logo[0])
    #         screen.blit(logo_img, (logo_x, 50))

    #         screen.blit(name, (350, size_logo[1] + 100 + 20))
    #         screen.blit(score, (300, size_logo[1] + 100 + 70))

    #         index += 1

    #         pygame.display.update()
    #         clock.tick(160)

    #     pygame.quit()