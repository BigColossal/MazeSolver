from time import sleep
from graphics import Window
from config import SCREEN_X, SCREEN_Y

def main():
    WIN = Window(SCREEN_X, SCREEN_Y)
    WIN.wait_for_close()

main()