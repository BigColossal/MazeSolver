from maze import Maze
from Main import SCREEN_X, SCREEN_Y, WINDOW

def small_maze():
    num_rows = 10
    num_cols = 20
    margin = 50
    cell_size_x = (SCREEN_X - 2 * margin) / num_cols
    cell_size_y = (SCREEN_Y - 2 * margin) / num_rows
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, WINDOW)

def medium_maze():
    num_rows = 18
    num_cols = 36
    margin = 50
    cell_size_x = (SCREEN_X - 2 * margin) / num_cols
    cell_size_y = (SCREEN_Y - 2 * margin) / num_rows
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, WINDOW)

def large_maze():
    num_rows = 28
    num_cols = 56
    margin = 50
    cell_size_x = (SCREEN_X - 2 * margin) / num_cols
    cell_size_y = (SCREEN_Y - 2 * margin) / num_rows
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, WINDOW)