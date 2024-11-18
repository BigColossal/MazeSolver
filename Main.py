from graphics import Window
from config import SCREEN_X, SCREEN_Y, BACKGROUND_COLOR

def main():
    WIN = Window(SCREEN_X, SCREEN_Y, BACKGROUND_COLOR)
    WIN.wait_for_close()

main()