
from .parsing_conf import Config
import pygame


class ErrorGamePlay(Exception):
    pass


class Screen:
    """Class screen."""
    screens_list = []

    @classmethod
    def add_screen(cls, screen) -> None:
        """Add screens."""
        cls.screens_list.append(screen)

    @classmethod
    def remove_screen(cls) -> None:
        """Remove the end screen of the list."""
        if len(cls.screens_list) > 0:
            cls.screens_list.pop()


class GamePlay:
    """Play game."""

    def __init__(self, config: Config, screen_size: tuple[int] = (800, 800)) -> None:
        """Init PlayGame."""
        self.screen_size = screen_size
        self.config = config
        self.levels = config.levels

    def run(self) -> int:
        from .screens import MenuScreen
        try:
            pygame.init()
            clock = pygame.time.Clock()
            screen = pygame.display.set_mode(self.screen_size)
            current_screen = MenuScreen(self.levels[0])
            Screen.add_screen(current_screen)

            runing = True

            while runing:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        runing = False
                    if event.type == pygame.KEYDOWN:
                        current_screen.handle_event(event)
                        if current_screen.next_screen:
                            current_screen = current_screen.next_screen
                            if current_screen not in Screen.screens_list:
                                Screen.add_screen(current_screen)

                screen.fill((0, 0, 0))

                current_screen.draw(screen)
                print("list_screen", Screen.screens_list)

                pygame.display.update()
                clock.tick(60)

            pygame.quit()

        except ErrorGamePlay as e:
            print(e)
            return 1
        return 0

