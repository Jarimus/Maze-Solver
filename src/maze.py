from cell import Cell
from time import sleep
from window import Window
from random import seed, randint
from constants import MAZE_GENERATION_SPEED

class Maze():

    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size,
        win: Window=None,
        set_seed: int=None,
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self._win = win
        self.seed = None if seed is None else seed(set_seed)

        # Create the maze
        self._create_cells()

        # break entrance and exit
        self._break_entrance_and_exit()

        # Create paths
        self._break_walls_r(0,0)

        # Reset visited status
        self._reset_visited_cells()


    
    def _create_cells(self):
        """Fills a list with lists of cells. Top-level lists are the rows in the maze.
        Once populated, calls _draw_cell() to draw the cells."""

        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self._win))
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    
    def _break_entrance_and_exit(self):
        self._cells: list[list[Cell]]

        #entrance
        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0)

        #exit
        exit = self._cells[self.num_cols - 1][self.num_rows - 1]
        exit.bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def _break_walls_r(self, i: int, j: int):
        """Depth first recursion to break walls when initializing the maze.
        Process:
        1) Initiate in the entrance cell.
        2) Mark the current Cell as visited.
        3) List non-visited Cells to enter.
        4) While list is non-empty, pick one Cell randomly from the list and pop it.
        5) Break the wall to it.
        6) Call recursively from that Cell.
        7) Loop back to 4 until the list is empty.
        8) Return
        """

        #2
        current_cell = self._cells[i][j]
        current_cell.visited = True

        #3 Create a list of potential paths
        next_cells = []
        for (n, m) in [ (i,j+1), (i,j-1), (i-1,j), (i+1,j) ]:
            if not (0 <= n < self.num_cols and 0 <= m < self.num_rows):
                continue
            if not self._cells[n][m].visited:
                next_cells.append( (n, m) )
    
        #4 Choose one path randomly. Break, draw and enter recursively.
        while next_cells != []:
            n, m = next_cells.pop( randint(0, len(next_cells) - 1 ) )
            next_cell = self._cells[n][m]
            next_cell: Cell
            if not next_cell.visited:
                if n == i + 1:
                    current_cell.right_wall = False
                    next_cell.left_wall = False
                elif n == i - 1:
                    current_cell.left_wall = False
                    next_cell.right_wall = False
                elif m == j + 1:
                    current_cell.bottom_wall = False
                    next_cell.top_wall = False
                elif m == j - 1:
                    current_cell.top_wall = False
                    next_cell.bottom_wall = False
                
                self._draw_cell(i, j)
                self._break_walls_r(n, m)
        


    def _draw_cell(self, i:int, j:int):
        if self._win is None:
            return
        """Draws a cell according to its place in the self._cells list of lists."""
        #calculate Cell's position
        x1 = self.x1 + i * self.cell_size
        y1 = self.y1 + j * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size

        #draw the Cell
        self._cells[i][j].draw(x1, y1, x2, y2)

        #animate the maze
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(MAZE_GENERATION_SPEED)
    
    def _reset_visited_cells(self):
        cell: Cell
        for row in self._cells:
            for cell in row:
                cell.visited = False