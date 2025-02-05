from tkinter import Tk, BOTH, Canvas
from line import Line

class Window():

    def __init__(self, width, height):
        # Window size
        self.__width = str(width)
        self.__height = str(height)
        
        # Tk widget
        self.__tk = Tk()
        self.__tk.geometry(self.__width + "x" + self.__height + "+" + "100" + "+" + "100")
        self.__tk.title = "Maze Solver"

        # canvas
        self._canvas = Canvas()
        self._canvas.config( width=self.__width, height=self.__height, bg="#d9d9d9")
        self._canvas.pack()

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
        line.draw(self._canvas, fill_color)