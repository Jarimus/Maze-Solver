from tkinter import Tk, Button, Canvas, font
from line import Line
from constants import BACKGROUND_COLOR, MAZE_V_PADDING, MAZE_H_PADDING, MAZE_COLS, MAZE_ROWS, CELL_SIZE, RANDOM_SEED
from maze import Maze


class Window():

    def __init__(self, width, height):
        self.__tk = Tk()

        # Customizable cell size from the constant value
        self.cell_size = CELL_SIZE

        # Font
        self.button_font = font.Font(size=28)

        # Window size
        if width == 0 and height == 0:
            new_width, new_height = self.__tk.winfo_screenwidth() - 10, self.__tk.winfo_screenheight() - 10
            self.__width = new_width
            self.__height = new_height
        else:
            self.__width = width
            self.__height = height
        
        # Tk widget
        self.__tk.configure(background=BACKGROUND_COLOR)
        self.__tk.geometry(str(self.__width) + "x" + str(self.__height) + "+0+0")
        self.__tk.title = "Maze Solver"

        # canvas
        self._canvas = Canvas()

        # If CELL_SIZE is set, the canvas' size is calculated accordingly to minimize empty space
        if self.cell_size != 0:
            canvas_width = self.maze_x * 2 + self.cell_size * MAZE_COLS if width != 0 else new_width
            canvas_height = self.maze_y * 2 + self.cell_size * MAZE_ROWS if height != 0 else new_height - 200

        # If CELL_SIZE == 0, the canvas' size is calculated to fill the screen with a CELL_SIZE that fills the canvas.
        elif self.cell_size == 0:
            canvas_width, canvas_height = self.__width, self.__height - 200
            self.cell_size = min( (canvas_width - MAZE_H_PADDING) // MAZE_COLS, (canvas_height - MAZE_V_PADDING) // MAZE_ROWS )
        
        self._canvas.config( width=canvas_width, height=canvas_height, bg=BACKGROUND_COLOR)
        self._canvas.grid( column=0, columnspan=2,row=0 )

        # Adjust maze to the center of the canvas when in full screen
        self.maze_x = (new_width - (self.cell_size * MAZE_COLS)) // 2
        self.maze_y = ((new_height - 200) - (self.cell_size * MAZE_ROWS)) // 2

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
        self.maze = Maze(self.maze_x, self.maze_y, MAZE_ROWS, MAZE_COLS, self.cell_size, self, RANDOM_SEED)
        # Reactivate the button, activate solve button
        self.create_maze_btn["state"] = "normal"
        self.solve_maze_btn["state"] = "normal"

    
    def solve_maze(self):
        self.solve_maze_btn["state"] = "disabled"
        self.maze.solve()