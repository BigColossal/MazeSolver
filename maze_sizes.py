from maze import Maze
from config import SCREEN_X, SCREEN_Y

def small_maze(window):
    num_rows = 8
    num_cols = 16
    margin = 50
    cell_size_x = (SCREEN_X - 2 * margin) / num_cols
    cell_size_y = (SCREEN_Y - 2 * margin) / num_rows
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)

def medium_maze(window):
    num_rows = 16
    num_cols = 32
    margin = 50
    cell_size_x = (SCREEN_X - 2 * margin) / num_cols
    cell_size_y = (SCREEN_Y - 2 * margin) / num_rows
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)

def large_maze(window):
    num_rows = 28
    num_cols = 56
    margin = 50
    cell_size_x = (SCREEN_X - 2 * margin) / num_cols
    cell_size_y = (SCREEN_Y - 2 * margin) / num_rows
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)