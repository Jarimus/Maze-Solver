from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    #open window
    win = Window(800, 600)

    #draw a few cells
    which_walls = []
    for i in range(16):
        binary = bin(i)[2:][::-1]
        binary = "0" * (4 - len(binary)) + binary[::-1]
        which_walls.append( binary )
    
    for i, permutation in enumerate(which_walls):
        if i % 2 == 0:
            cell = Cell( (20 * (i + 1), 10), (20 * (i + 2), 30), win._canvas)
            
            if permutation[0] == "0":
                cell.top_wall = False
            if permutation[1] == "0":
                cell.bottom_wall = False
            if permutation[2] == "0":
                cell.left_wall = False
            if permutation[3] == "0":
                cell.right_wall = False

            cell.draw()
            
        else:
            cell = Cell( (10, 20 * (i + 1) ), (30, 20 * (i + 2) ), win._canvas)
            walls = [cell.top_wall, cell.bottom_wall, cell.right_wall, cell.left_wall]
            
            if permutation[0] == "0":
                cell.top_wall = False
            if permutation[1] == "0":
                cell.bottom_wall = False
            if permutation[2] == "0":
                cell.left_wall = False
            if permutation[3] == "0":
                cell.right_wall = False

            cell.draw()



    #wait for close
    win.wait_for_close()



if __name__ == '__main__':
    main()