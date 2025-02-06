from point import Point
from line import Line
from window import Window
from constants import WALL_COLOR, BACKGROUND_COLOR, CORRECT_PATH_COLOR, WRONG_PATH_COLOR

class Cell():
    """A class for the individual cells in the maze"""

    def __init__(self, win: Window):
        """Creates a Cell instance without any coordinates. Coordinates are set when the cell is drawn."""
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.top_wall = True
        self.bottom_wall = True
        self.left_wall = True
        self.right_wall = True
        self.win = win
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        """Draws the cell on the canvas. Also updates the coordinates of the cell.
        x1y1 --- x2y1
        |        |
        |        |
        x1y2 --- x2y2"""

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        #Draw walls as Lines
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        lines = []
        passage = []
        if self.top_wall:
            lines.append( Line(top_left, top_right) )
        else:
            passage.append( Line(top_left, top_right) )
        if self.right_wall:
            lines.append( Line(top_right, bottom_right) )
        else:
            passage.append( Line(top_right, bottom_right) )
        if self.bottom_wall:
            lines.append( Line(bottom_left, bottom_right) )
        else:
            passage.append( Line(bottom_left, bottom_right) )
        if self.left_wall:
            lines.append( Line(top_left, bottom_left) )
        else:
            passage.append( Line(top_left, bottom_left) )

        line: Line
        for line in lines:
            self.win.draw_line(line, WALL_COLOR)
        for line in passage:
            self.win.draw_line(line, BACKGROUND_COLOR)
    
    def draw_move(self, other_cell: "Cell", undo=False):
        center_self = Point( (self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        center_other = Point( (other_cell._x1 + other_cell._x2) / 2, (other_cell._y1 + other_cell._y2) / 2)
        line = Line( center_self, center_other )
        color = CORRECT_PATH_COLOR if not undo else WRONG_PATH_COLOR
        self.win.draw_line( line, fill_color=color)