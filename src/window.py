from tkinter import Tk, Button, Canvas, font, Entry, Label
from line import Line
from constants import BACKGROUND_COLOR, MAZE_V_PADDING, MAZE_H_PADDING, MAZE_COLS, MAZE_ROWS, CELL_SIZE, RANDOM_SEED, SPACE_FOR_UI, ELEMENT_PADDING
from maze import Maze


class Window():

    def __init__(self, width, height):
        self.__tk = Tk()
        self._canvas = None

        # Customizable cell size from the constant value
        self.cell_size = CELL_SIZE

        # Font
        self.button_font = font.Font(size=28)

        # Window size
        self.__tk.attributes("-fullscreen", True)

        if width == 0 or height == 0:
            self.__width, self.__height = min(self.__tk.winfo_screenwidth(), 1920), min(self.__tk.winfo_screenheight(), 1080) 
        else:
            self.__width = width
            self.__height = height
        
        # Tk widget
        self.__tk.configure(background=BACKGROUND_COLOR)
        self.__tk.geometry(str(self.__width) + "x" + str(self.__height) + "+0+0")
        self.__tk.title = "Maze Solver"

        # 'Create Maze' button
        self.create_maze_btn = Button(self.__tk, text="Create a maze", command=self.start_maze, font=self.button_font)
        self.create_maze_btn.grid( column=0, row=0, pady=ELEMENT_PADDING )

        # 'Solve Maze' button
        self.solve_maze_btn = Button(self.__tk, text="Solve", state="disabled", command=self.solve_maze("normal"), font=self.button_font)
        self.solve_maze_btn.grid( column=1, row=0, pady=ELEMENT_PADDING )

        # 'Solve Maze Quickly' button
        self.solve_maze_quickly_btn = Button(self.__tk, text="Solve (only correct path)", state="disabled", command=self.solve_maze("quickly"), font=self.button_font)
        self.solve_maze_quickly_btn.grid( column=2, row=0, pady=ELEMENT_PADDING )

        # 'Exit' button
        self.exit_btn = Button(self.__tk, text="Exit", state="normal", command=self.close, font=self.button_font)
        self.exit_btn.grid( column=3, row=0, pady=ELEMENT_PADDING )

        # Labels and Entries for rows and columns
        self.rows_label = Label(self.__tk, text=f"Rows (Default {MAZE_ROWS}):", font=self.button_font)
        self.rows_label.grid(column=0, row=1, pady=ELEMENT_PADDING)
        self.rows_entry = Entry(self.__tk, font=self.button_font)
        self.rows_entry.grid(column=1, row=1, pady=ELEMENT_PADDING)

        self.cols_label = Label(self.__tk, text=f"Columns(Default {MAZE_COLS}):", font=self.button_font)
        self.cols_label.grid(column=2, row=1, pady=ELEMENT_PADDING)
        self.cols_entry = Entry(self.__tk, font=self.button_font)
        self.cols_entry.grid(column=3, row=1, pady=ELEMENT_PADDING)

        # Create canvas
        self.create_canvas()

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
        self.create_canvas()

        # disable the buttons
        self.solve_maze_btn["state"] = "disabled"
        self.create_maze_btn["state"] = "disabled"
        # Clear canvas
        self._canvas.delete("all")


        # Initiate the maze
        self.maze = Maze(self.maze_x, self.maze_y, self.rows, self.cols, self.cell_size, self, RANDOM_SEED)
        # Reactivate the button, activate solve button
        self.create_maze_btn["state"] = "normal"
        self.solve_maze_btn["state"] = "normal"
        self.solve_maze_quickly_btn["state"] = "normal"
        self.exit_btn["state"] = "normal"

    
    def solve_maze(self, style="normal"):
        def solve():
            self.solve_maze_btn["state"] = "disabled"
            self.solve_maze_quickly_btn["state"] = "disabled"
            self.create_maze_btn["state"] = "disabled"
            self.exit_btn["state"] = "disabled"
            if style == "quickly":
                self.maze._solve_r_quickly()
            elif style == "normal":
                self.maze.solve()
            self.create_maze_btn["state"] = "normal"
            self.exit_btn["state"] = "normal"
        return solve

    def create_canvas(self):
        # canvas
        if self._canvas:
            self._canvas.delete()
        self._canvas = Canvas()

        #Get dimensions for the canvas
        canvas_width = self.__width * 0.999
        canvas_height = self.__height - SPACE_FOR_UI

        # Get rows and columns from entries
        try:
            self.rows = int(self.rows_entry.get())
            self.cols = int(self.cols_entry.get())
        except ValueError:
            self.rows = MAZE_ROWS
            self.cols = MAZE_COLS

        #Apply UI
        self._canvas.config( width=canvas_width, height=canvas_height, bg=BACKGROUND_COLOR)
        self._canvas.grid( column=0, columnspan=4,row=2 )

        # If CELL_SIZE == 0, the canvas' size is calculated to fill the screen with a CELL_SIZE that fills the canvas.
        #if self.cell_size == 0:
        self.cell_size = min( (canvas_width - MAZE_H_PADDING) // self.cols, (canvas_height - MAZE_V_PADDING) // self.rows )

        # Adjust maze to the center of the canvas
        self.maze_x = (self.__width - (self.cell_size * self.cols)) // 2
        self.maze_y = ((self.__height - SPACE_FOR_UI) - (self.cell_size * self.rows)) // 2