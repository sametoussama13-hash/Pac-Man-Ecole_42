from .mazedisplay import DisplayMaze
from .parsing_conf import parsing_conf
from .play_game import GamePlay
from mazegenerator import MazeGenerator


class ErrorGenerationMaze(Exception):
    pass


class DisplayGameError(Exception):
    pass


class MazeDisplayError(Exception):
    pass


def run(config_path: str) -> int:
    config = parsing_conf(config_path)
    if not config:
        print("the config file not supported")
        return 1

    try:
        play_game = GamePlay(config)
        play_game.run()
    except DisplayGameError:
        print("Error Display in Paygame.")
        return 1

    # print(maze)
    # for row in maze.maze:
    #     print(row)
    # print(config)
