from .mazedisplay import DisplayMaze
from .parsing_conf import parsing_conf
from .game import play_game
from mazegenerator import MazeGenerator


class ErrorGenerationMaze(Exception):
    pass


class DisplayGameError(Exception):
    pass


class MazeDisplayError(Exception):
    pass


def run(config_path: str) -> None:
    config = parsing_conf(config_path)
    if not config:
        print("the config file not supported")
        return 1
    try:
        maze = MazeGenerator()
        # for row in maze._path:
        #     print(row)
    except ErrorGenerationMaze:
        print("Error: we cant generate maze.")
        return 1

    try:
        maze_display = DisplayMaze(maze)
        # for row in maze_display.display:
        #     print(row)
    except MazeDisplayError:
        print("Error: we cant generate maze for display")
        return 1

    try:
        play_game(maze_display)
    except DisplayGameError:
        print("Error Display in Paygame.")
        return 1

    # print(maze)
    # for row in maze.maze:
    #     print(row)
    # print(config)
