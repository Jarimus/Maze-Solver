from point import Point
from line import Line

class Cell():
    """A class for the individual cells in the maze"""

    def __init__(self, coord1: tuple[int, int], coord2: tuple[int, int], canvas):
        """Creates a Cell instance with coordinates for the top-left and bottom-right corners and the canvas for drawing."""
        self._x1 = coord1[0]
        self._y1 = coord1[1]
        self._x2 = coord2[0]
        self._y2 = coord2[1]
        self.top_wall = True
        self.bottom_wall = True
        self.left_wall = True
        self.right_wall = True
        self._canvas = canvas
    
    def draw(self):
        """Draws the cell on the canvas.
        x1y1 --- x2y1
        |        |
        |        |
        x1y2 --- x2y2"""

        #Draw walls as Lines
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        lines = []
        if self.top_wall:
            lines.append( Line(top_left, top_right) )
        if self.right_wall:
            lines.append( Line(top_right, bottom_right) )
        if self.bottom_wall:
            lines.append( Line(bottom_left, bottom_right) )
        if self.left_wall:
            lines.append( Line(top_left, bottom_left) )

        line: Line
        for line in lines:
            line.draw(self._canvas, "black")