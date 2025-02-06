from window import Window
from maze import Maze
from constants import MAZE_TOP_X, MAZE_TOP_Y, MAZE_COLS, MAZE_ROWS, CELL_SIZE, RANDOM_SEED, SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    #open window either full screen size or custom size
    
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    #draw the maze
    Maze(MAZE_TOP_X, MAZE_TOP_Y, MAZE_ROWS, MAZE_COLS, CELL_SIZE, win, RANDOM_SEED)

    #wait for close
    win.wait_for_close()

if __name__ == '__main__':
    main()