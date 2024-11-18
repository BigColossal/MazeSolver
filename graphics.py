from tkinter import Tk, BOTH, Canvas, Button
from time import sleep
import webbrowser

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.main_menu_creation()



    # Menu creation and interactivity methods
    def main_menu_creation(self):
        mainMenuTitleText = UIText((650, 100), "Main Menu", self.__canvas)
        referenceText = UIText((200, 540), "Main Menu", self.__canvas)
        referenceButton = GameButton((200, 565), self.bootdev_reference, 
                                   "Main Menu", "Reference Button", self.__canvas)
        startButton = GameButton((650, 300), self.move_to_selection_menu,
                                  "Main Menu", "Start Button", self.__canvas)
        
        mainMenuTitleText.text_draw("Maze Solver", 50)
        referenceText.text_draw("Special thanks to boot.dev for guidance in this project", 16)
        referenceButton.button_draw("Link to boot.dev", 16, "underline", "blue")
        startButton.button_draw("Start", 20)


    def selection_menu_creation(self):
        SelectionMenuTitleText = UIText((650, 100), "Selection Menu", self.__canvas)
        SelectionMenuTitleText.text_draw("Selection", 50)

        smallMazeButton = GameButton((650, 200), self._create_small_maze,
                                    "Selection Menu", "Small Maze Button", self.__canvas)
        smallMazeButton.button_draw("Small Maze", 20)

        MediumMazeButton = GameButton((650, 350), self._create_medium_maze,
                                    "Selection Menu", "Medium Maze Button", self.__canvas)
        MediumMazeButton.button_draw("Medium Maze", 20)

        LargeMazeButton = GameButton((650, 500), self._create_large_maze,
                                    "Selection Menu", "Large Maze Button", self.__canvas)
        LargeMazeButton.button_draw("Large Maze", 20)



    # button actions
    def move_to_selection_menu(self):
        self.__canvas.delete("Main Menu")
        self.selection_menu_creation()

    def bootdev_reference(self):
        url = "https://www.boot.dev"
        webbrowser.open(url)
    

    # creation of mazes
    def _create_small_maze(self):
        from maze_sizes import small_maze
        self.__canvas.delete("Selection Menu")
        small_maze(self)

    def _create_medium_maze(self):
        from maze_sizes import medium_maze
        self.__canvas.delete("Selection Menu")
        medium_maze(self)

    def _create_large_maze(self):
        from maze_sizes import large_maze
        self.__canvas.delete("Selection Menu")
        large_maze(self)




    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.x1 = point1.x
        self.x2 = point2.x
        self.y1 = point1.y
        self.y2 = point2.y

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2)

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._window = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._window is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line, "white")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line, "white")

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._window.draw_line(line, fill_color)

class GameButton:
    def __init__(self, center_of_button, callback, general_tag_input, tag_input, canvas):
        self._center = center_of_button
        self.callback = callback
        self._button_id = None
        self._general_tag = general_tag_input
        self._tag = tag_input
        self._canvas = canvas

    def button_draw(self, textInput, fontSize, uniqueTextFont="", textColor="black"):
        self._button_id = self._canvas.create_rectangle(self._center[0] - 65, self._center[1] - 15,
                                self._center[0] + 65, self._center[1] + 15,
                                fill="white", outline="white", tags=(self._general_tag, self._tag))
        
        self._canvas.create_text(self._center[0], self._center[1], text=textInput, fill=textColor,
                            font=("Arial", fontSize, uniqueTextFont), tags=(self._general_tag, self._tag))
        self._canvas.tag_bind(self._tag, "<Button-1>", self.on_click)

    def on_click(self, event):
        self.callback()

class UIText:
    def __init__(self, center_of_text, general_tag_input, canvas):
        self._center = center_of_text
        self._tag = general_tag_input
        self._canvas = canvas

    def text_draw(self, textInput, fontSize):
        self._canvas.create_text(self._center[0], self._center[1], text=textInput, fill="black",
                                 font=("Arial", fontSize), tags=(self._tag,))
    