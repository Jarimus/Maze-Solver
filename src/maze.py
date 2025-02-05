from cell import Cell
from time import sleep
from window import Window

class Maze():

    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size,
        win: Window=None,
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self._win = win

        self._create_cells()
    
    def _create_cells(self):
        """Fills a list with lists of cells. Top-level lists are the rows in the maze.
        Once populated, calls _draw_cell() to draw the cells."""

        self._cells: list[list[Cell]]
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self._win))
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        
        #break entrance and exit
        self._break_entrance_and_exit()
    
    def _break_entrance_and_exit(self):
        self._cells: list[list[Cell]]

        #entrance
        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0)

        #exit
        exit = self._cells[self.num_cols - 1][self.num_rows - 1]
        exit.bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

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
        sleep(0.01)