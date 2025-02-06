from window import Window
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    #open window either full screen size or custom size
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)

    #wait for close
    win.wait_for_close()

if __name__ == '__main__':
    main()