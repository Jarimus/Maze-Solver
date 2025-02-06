import unittest
from maze import Maze
from constants import *
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_entrance_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, set_seed=1)
        self.assertEqual(
            m1._cells[0][0].top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].bottom_wall,
            False,
        )
    
    def test_visited_status_reset(self):
        m1 = Maze(MAZE_TOP_X, MAZE_TOP_Y, MAZE_ROWS, MAZE_COLS, CELL_SIZE, set_seed=1)
        
        cell: Cell
        for col in m1._cells:
            for cell in col:
                self.assertEqual( cell.visited, False)

if __name__ == "__main__":
    unittest.main()