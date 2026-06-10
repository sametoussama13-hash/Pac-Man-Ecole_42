from .screen import ScreenMenu, ScreenPlay, ErrorGamePlay, PlayGame
from .mazedisplay import DisplayMaze
from .user_interface import UserInterface
from .score import ScorePlayer
from .gamelogic import GameLogic

def play_game(maze_display: DisplayMaze, config) -> int:
    try:
        # screen_menu_game = ScreenMenu(maze_display)
        # screen_menu_game.play_screen() # Main menu
        # screen_play_game = ScreenPlay(maze_display)
        # screen_play_game.play_screen() # 
        game = Game()
        game.init()

    except ErrorGamePlay as e:
        print(e)
        return 1
    return 0


class Game():

    def __init__(self, config) -> None:
        # all menu are invisible by default
        self.player = ScorePlayer("player 1")
        self.cfg = config
        self.interface = UserInterface(self.cfg, self.player)
        self.game_logic = GameLogic(self.cfg, self.player, self.interface)
        self.win = False
        pass


    def init_game(self) -> None:
        pass

    def set_level(self) -> None:
        # gen new maze base on the seed on randomly if not level 0
        # this where we will update the level they move to the next level
        # .
        pass


    def check_score(self) -> None:
        # here we can check if we need to upgrade level
        # if thhe level is complete , they move to the next level
        pass

    def check_life(self) -> None:
        # here we can check if we still have life
        # if the players loses all lives 
        # the game ends
        pass

    def end(self) -> None:
        # when the game end win or lose 
        # when the game ends (win or lose), the final score
        # is displayed , and the player can enter their name 
        # to save the highscore
        if self.win:
            print("Victory!")
            # show menu victory with the help of the interface
        else: 
            print("Game Over!")
            # show menu game over with the help of the interface
        pass

    def play(self) -> None:
        while True:
            # tant que le jeu est lancer
            # show inGmae menu
            # play_game.display() show the game
            # check the score to see if we need to level up
            pass
        # after the game end the player is return to the main menu



    



        

    
