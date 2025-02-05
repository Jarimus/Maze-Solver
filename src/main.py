from window import Window
from maze import Maze
def main():
    #open window
    win = Window(800, 600)

    #draw the maze: topleft corner coords, num of cols and rows, cell size, window
    Maze(200, 50, 10, 10, 40, win)

    #wait for close
    win.wait_for_close()



if __name__ == '__main__':
    main()