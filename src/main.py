from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    #open window
    win = Window(800, 600)

    #draw a cells and moves between them
    cell1 = Cell( (100, 100), (200, 200), win._canvas )
    cell1.right_wall = False

    cell2 = Cell( (200,100), (300,200), win._canvas )
    cell2.left_wall = False
    cell2.bottom_wall = False

    cell3 = Cell( (200,200), (300,300), win._canvas )
    cell3.top_wall = False

    cell1.draw()
    cell2.draw()
    cell3.draw()

    cell1.draw_move(cell2)
    cell2.draw_move(cell3, undo=True)
    



    #wait for close
    win.wait_for_close()



if __name__ == '__main__':
    main()