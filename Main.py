from maze_sizes import large_maze, medium_maze, small_maze
from graphics import Window
from time import sleep

SCREEN_X = 1300
SCREEN_Y = 600
WINDOW = Window(SCREEN_X, SCREEN_Y)

def main():
    large_maze()


    WINDOW.wait_for_close()


main()