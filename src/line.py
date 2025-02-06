from point import Point
from constants import LINE_THICKNESS
from tkinter import Canvas

class Line():
    """A class for the lines that show the path traversed through the maze."""

    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas: Canvas, fill_color: str):
        """Draws a line from point1 to point2 on the canvas."""
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=LINE_THICKNESS)