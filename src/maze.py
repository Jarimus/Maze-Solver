from cell import Cell
from time import sleep
from random import seed, randint, choice
from constants import MAZE_GENERATION_SPEED, CORRECT_PATH_COLOR, WRONG_PATH_COLOR, MAZE_SOLVE_SPEED
from line import Line
from point import Point

class Maze():

    def __init__(
        self,
        maze_x: int,
        maze_y: int,
        num_rows: int,
        num_cols: int,
        cell_size,
        win =None,
        set_seed: int=None,
    ):
        self._cells = []
        self.x1 = maze_x
        self.y1 = maze_y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self._win = win
        self.seed = None if seed is None else seed(set_seed)

        self.recursion_limit_reached = False
        self.visited_cells = set()
        self._cell_count = 0

        # Create the maze
        self._create_cells()

        # break entrance and exit
        self._break_entrance_and_exit()

        # Create paths
        self._break_walls_r(0,0)
        
        print(f"visited: {len(self.visited_cells)}\ntotal: {self._cell_count}")
        while len(self.visited_cells) < self._cell_count:
            self.recursion_limit_reached = False
            i, j = choice(list(self.visited_cells))
            print("Starting new break at:", i, j)
            self._break_walls_r(i, j)

        # Reset visited status
        self._reset_visited_cells()

    
    def _create_cells(self):
        """Fills a list with lists of cells. Top-level lists are the rows in the maze.
        Once populated, calls _draw_cell() to draw the cells."""

        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self._win))
                self._cell_count += 1
        
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
        # Recursively break walls to form the maze. If recursion depth is reached, reset the stack.
        # A new recursion will be started from one of the self.visited_cells until all the cells have been visited.

        if self.recursion_limit_reached:
            return

        #1 Mark current visited
        current_cell = self._cells[i][j]
        current_cell.visited = True
        self.visited_cells.add((i,j))

        #2 Create a list of potential paths
        next_cells = []
        for (n, m) in [ (i,j+1), (i,j-1), (i-1,j), (i+1,j) ]:
            if not (0 <= n < self.num_cols and 0 <= m < self.num_rows):
                continue
            if not self._cells[n][m].visited:
                next_cells.append( (n, m) )
    
        #3 Choose one path randomly. Break, draw and enter recursively.
        while next_cells != []:
            if self.recursion_limit_reached:
                return
            
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
    
                try:
                    self._draw_cell(i, j)
                    self._break_walls_r(n, m)
                except RecursionError:
                    self.recursion_limit_reached = True
                    break    

    def _animate(self, mode=""):
        if self._win is None:
            return
        self._win.redraw()

        if mode == "solve":
            sleep_per_cell = MAZE_SOLVE_SPEED / (self.num_cols * self.num_rows)
            limit = 1 / (self.num_cols * self.num_rows)
            sleep(max(sleep_per_cell, limit))
        elif mode == "draw cells":
            sleep_per_cell = MAZE_GENERATION_SPEED / (self.num_cols * self.num_rows)
            sleep(sleep_per_cell)


    def _draw_cell(self, i:int, j:int):
        """Draws a cell according to its place in the self._cells list of lists."""
        if self._win is None:
            return
        #calculate Cell's position
        x1 = self.x1 + i * self.cell_size
        y1 = self.y1 + j * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size

        #draw the Cell
        self._cells[i][j].draw(x1, y1, x2, y2)

        #animate the cell drawing
        self._animate("draw cells")
    

    def _draw_line(self, i: int, j: int, n: int, m: int, undo=False):
        if self._win is None:
            return
        
        if undo:
            fill_color = WRONG_PATH_COLOR
        else:
            fill_color = CORRECT_PATH_COLOR

        current_cell = self._cells[i][j]
        other_cell = self._cells[n][m]

        x1 = current_cell._x1 + self.cell_size / 2
        y1 = current_cell._y1 + self.cell_size / 2
        x2 = other_cell._x1 + self.cell_size / 2
        y2 = other_cell._y1 + self.cell_size / 2

        new_line = Line( Point(x1, y1), Point(x2, y2) )
        self._win.draw_line( new_line, fill_color)

    
    def _reset_visited_cells(self):
        self.visited_cells = set()
        cell: Cell
        for row in self._cells:
            for cell in row:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i: int, j: int):

        path = [] # a list recording the current path being traced. used to back track and mark as incorrect

        while True:
            #visit the current cell
            current_cell = self._cells[i][j]
            current_cell.visited = True

            # Stop if the exit has been reached.
            if i == self.num_cols - 1 and j == self.num_rows - 1:
                    break

            # adjacent cells are all the cells orthogonally adjacent to the current cell
            adjacent_cells = [ (i,j+1), (i,j-1), (i-1,j), (i+1,j) ]
            potential_cells = []

            # Go through the adjacent cells, and pick only cells that
            # 1) Are within the maze coordinates
            # 2) Are not blocked by a wall
            # 3) Are not visited
            for next_cell in adjacent_cells:
                n, m = next_cell
                if not (0 <= n < self.num_cols and 0 <= m < self.num_rows):
                    continue
                elif n == i - 1 and current_cell.left_wall == True:
                    continue
                elif n == i + 1 and current_cell.right_wall == True:
                    continue
                elif m == j - 1 and current_cell.top_wall == True:
                    continue
                elif m == j + 1 and current_cell.bottom_wall == True:
                    continue
                elif self._cells[n][m].visited:
                    continue
                else:
                    potential_cells.append( (n, m) )
                
            # If there were no new cells to visit, this is a dead-end.
            # Backtrack to the previous cell, until there are potential cells.
            if len(potential_cells) == 0:
                i, j, n, m = path.pop()
                self._draw_line(i, j, n, m, undo=True)
                self._animate("solve")
                continue
            # If there are potential cells, pick one to traverse to.
            elif len(potential_cells) > 0:
                n, m = choice(potential_cells)
                path.append( (i, j, n, m) )
                print("Drawing:", i, j, n, m)
                self._draw_line( i, j, n, m )
                self._animate("solve")
                i, j = n, m
                continue