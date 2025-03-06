from point import Point
from constants import WALL_LINE_THICKNESS, PATH_LINE_THICKNESS, CORRECT_PATH_COLOR, WRONG_PATH_COLOR, WALL_COLOR, BACKGROUND_COLOR, EXIT_COLOR
from tkinter import Canvas

class Line():
    """A class for the lines that show the path traversed through the maze."""

    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas: Canvas, fill_color: str):
        """Draws a line from point1 to point2 on the canvas."""
        if fill_color in [CORRECT_PATH_COLOR, WRONG_PATH_COLOR, EXIT_COLOR]:
            canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=PATH_LINE_THICKNESS)
        elif fill_color in [WALL_COLOR, BACKGROUND_COLOR]:
            canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=WALL_LINE_THICKNESS)