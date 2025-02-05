from tkinter import Tk, Button, Canvas, font
from line import Line
from constants import BACKGROUND_COLOR, MAZE_TOP_X, MAZE_TOP_Y, MAZE_COLS, MAZE_ROWS, CELL_SIZE, RANDOM_SEED
from maze import Maze


class Window():

    def __init__(self, width, height):
        self.__tk = Tk()

        # Font
        self.button_font = font.Font(size=28)

        # Window size
        if width == 0 and height == 0:
            width, height = self.__tk.winfo_screenwidth() - 10, self.__tk.winfo_screenheight() - 10
        self.__width = str(width)
        self.__height = str(height)
        
        # Tk widget
        self.__tk.geometry(self.__width + "x" + self.__height + "+0+0")
        self.__tk.title = "Maze Solver"

        # canvas
        self._canvas = Canvas()
        canvas_width = MAZE_TOP_X * 2 + CELL_SIZE * MAZE_COLS
        canvas_height = MAZE_TOP_Y * 2 + CELL_SIZE * MAZE_ROWS
        self._canvas.config( width=canvas_width, height=canvas_height, bg=BACKGROUND_COLOR)
        self._canvas.grid( column=0, columnspan=2,row=0 )

        # 'Create Maze' button
        self.create_maze_btn = Button(self.__tk, text="Create a maze", command=self.start_maze, font=self.button_font)
        self.create_maze_btn.grid( column=0, row=1 )
        

        # 'Solve Maze' button
        self.solve_maze_btn = Button(self.__tk, text="Solve the maze", state="disabled", command=self.solve_maze, font=self.button_font)
        self.solve_maze_btn.grid( column=1, row=1 )

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

    def start_maze(self):
        # disable the create button
        self.create_maze_btn["state"] = "disabled"
        # Clear canvas
        self._canvas.delete("all")
        # Initiate the maze
        self.maze = Maze(MAZE_TOP_X, MAZE_TOP_Y, MAZE_ROWS, MAZE_COLS, CELL_SIZE, self, RANDOM_SEED)
        # Reactivate the button, activate solve button
        self.create_maze_btn["state"] = "normal"
        self.solve_maze_btn["state"] = "normal"

    
    def solve_maze(self):
        self.solve_maze_btn["state"] = "disabled"
        self.maze.solve()