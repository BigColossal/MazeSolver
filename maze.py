from graphics import Cell
from time import sleep
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []
        self._win = win
        if seed:
            random.seed(seed)
        
        self._user_position = None

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self.user_solve(self._win.get_canvas())
    
    def _create_cells(self):
        for column in range(self._num_cols):
            columnList = [Cell(self._win) for row in range(self._num_rows)]
            self._cells.append(columnList)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j, breaking_walls=False):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        if breaking_walls:
            pass

    def _animate(self, animation_time):
        if self._win is None:
            return
        self._win.redraw()
        sleep(animation_time)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_right_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j, True)
                return
            direction_index = random.randrange(len(to_visit))
            direction = to_visit[direction_index]

            if direction[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if direction[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            if direction[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            if direction[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False
    
    def user_solve(self, canvas):
        self._user_position = [0, 0]
        canvas.focus_set()
        canvas.bind("<Up>", self.handle_key_press)
        canvas.bind("<Down>", self.handle_key_press)
        canvas.bind("<Right>", self.handle_key_press)
        canvas.bind("<Left>", self.handle_key_press)
        canvas.bind("<a>", self.handle_key_press)
        canvas.bind("<s>", self.handle_key_press)
        canvas.bind("<w>", self.handle_key_press)
        canvas.bind("<d>", self.handle_key_press)

    def handle_key_press(self, event):
        print(f"Key pressed: {event.keysym}, Current position: {self._user_position}")
        if event.keysym == "Up" or event.keysym == "w":
            if self._user_position[1] > 0 and not self._cells[self._user_position[0]][self._user_position[1]].has_top_wall:
                self._user_position[1] -= 1
                self._cells[self._user_position[0]][self._user_position[1] + 1].draw_move(self._cells[self._user_position[0]][self._user_position[1]])

        elif event.keysym == "Down" or event.keysym == "s":
            if self._user_position[1] < self._num_rows and not self._cells[self._user_position[0]][self._user_position[1]].has_bottom_wall:
                self._user_position[1] += 1
                self._cells[self._user_position[0]][self._user_position[1] - 1].draw_move(self._cells[self._user_position[0]][self._user_position[1]])
        elif event.keysym == "Left" or event.keysym == "a":
            pass
        elif event.keysym == "Right" or event.keysym == "d":
            pass

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate(0.01)
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[-1][-1]:
            return True
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if j < self._num_rows and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False


