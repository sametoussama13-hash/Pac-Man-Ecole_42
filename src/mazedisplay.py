from mazegenerator import MazeGenerator
from .box import Box


class DisplayMaze:

    def __init__(self, maze: MazeGenerator) -> None:
        self.maze: MazeGenerator = maze
        self.maze_grid: list[list[int]] = maze.maze
        self.grid_display: list[list[Box]] = self.generate_display_maze()
        self.entry: tuple[int] = self.converte_position(maze.maze_entry)

    def converte_position(self, position: tuple[int]) -> tuple[int]:
        x, y = position
        a = 0
        b = 0
        for _ in range(x + 1):
            a += 1
        for _ in range(y + 1):
            b += 1
        return x + a, y + b

    def generate_display_maze(self) -> list[list[Box]]:
        """Generate display maze."""
        maze_display: list[list[Box]] = []

        for y in range(len(self.maze_grid)):

            top, midel = self.generate_row(y)
            top.append(Box(1))
            midel.append(Box(1))

            maze_display.extend([top, midel])
        maze_display = (maze_display +
                        [[Box(1) for _ in range(len(maze_display[0]))]])
        maze_display = self.add_pattern(maze_display)
        return self.add_pacgum(maze_display)

    def generate_row(self, y: int) -> tuple[list, list]:
        """Generate row of the grid maze."""
        north_row: list[Box] = []
        east_row: list[Box] = []

        for x in range(len(self.maze_grid[0])):
            if self.maze_grid[y][x] & 1:
                north_row.extend([Box(1), Box(1)])
            elif not self.maze_grid[y][x] & 1:
                north_row.extend([Box(1), Box(0)])
            if self.maze_grid[y][x] & 8:
                east_row.extend([Box(1), Box(0)])
            elif not self.maze_grid[y][x] & 8:
                east_row.extend([Box(0), Box(0)])

        return (north_row, east_row)

    def add_pattern(self, maze: list[list[Box]]) -> list[list[Box]]:
        """Add the patern in grid."""
        for y in range(len(maze)):
            for x in range(len(maze[0])):
                if maze[y][x].type_box == 0:
                    if (maze[y-1][x].type_box and maze[y+1][x].type_box
                        and maze[y][x-1].type_box and maze[y][x+1].type_box):
                        maze[y][x].type_box = 2
        return maze

    def add_pacgum(self, maze: list[list[Box]]) -> list[list[Box]]:
        """Add pacgum in the maze display."""
        maze = self.add_super_pacgum(maze)
        for y in range(len(maze)):
            for x in range(len(maze[0])):
                if not maze[y][x].type_box and not maze[y][x].super_pacgum:
                    maze[y][x].pacgum = True
        return maze

    def add_super_pacgum(self, maze: list[list[Box]]) -> list[list[Box]]:
        """Add super pacgum in the maze display."""
        maze[1][1].super_pacgum = True
        maze[1][len(maze[0]) - 2].super_pacgum = True
        maze[len(maze) - 2][1].super_pacgum = True
        maze[len(maze) - 2][len(maze[0]) - 2].super_pacgum = True
        return maze


if __name__ == "__main__":
    maze = MazeGenerator()
    display = DisplayMaze(maze)
    print(display.converte_position((6, 5)))
