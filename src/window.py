from tkinter import Tk, BOTH, Canvas
from line import Line

class Window():

    def __init__(self, width, height):
        # Window size
        self.__width = width
        self.__height = height
        
        # Tk widget
        self.__tk = Tk()
        self.__tk.title = "Maze Solver"

        # canvas
        self.__canvas = Canvas()
        self.__canvas.pack()

        # window running?
        self.__running = False

        # Close when the window is closed
        self.__tk.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__tk.update_idletasks()
        self.__tk.update()
    
    def wait_for_close(self):

        self.__running = True

        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False
    
    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)