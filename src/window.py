from tkinter import Tk, Button, Canvas, font, Entry, Label
from line import Line
from constants import BACKGROUND_COLOR, MAZE_V_PADDING, MAZE_H_PADDING, MAZE_COLS, MAZE_ROWS, RANDOM_SEED, SPACE_FOR_UI, ELEMENT_PADDING, FONT_SIZE
from maze import Maze


class Window():

    def __init__(self, width, height):
        self.__tk = Tk()
        self._canvas = None
        self.buttons = []

        # Font
        self.button_font = font.Font(size=FONT_SIZE)

        # Window size
        if width == 0 or height == 0:
            self.__width, self.__height = self.__tk.winfo_screenwidth(), self.__tk.winfo_screenheight()
        else:
            self.__width = width
            self.__height = height
        
        self.__tk.attributes("-fullscreen", True)
        
        # Tk widget
        self.__tk.configure(background=BACKGROUND_COLOR)
        self.__tk.geometry(str(self.__width) + "x" + str(self.__height) + "+0+0")
        self.__tk.title = "Maze Solver"

        # 'Maze speed' button
        self.speed = "normal"
        self.speed_btn = Button(self.__tk, text=f"Speed: {self.speed}", command=self.set_speed, font=self.button_font)
        self.speed_btn.grid( column=0, row=0, pady=ELEMENT_PADDING)
        self.buttons.append(self.speed_btn)

        # 'Create Maze' button
        self.create_maze_btn = Button(self.__tk, text="Create a maze", command=self.start_maze, font=self.button_font)
        self.create_maze_btn.grid( column=1, row=0, pady=ELEMENT_PADDING )
        self.buttons.append(self.create_maze_btn)

        # 'Solve Maze' button
        self.solve_maze_btn = Button(self.__tk, text="Solve (random path)", state="disabled", command=self.solve_maze("random"), font=self.button_font)
        self.solve_maze_btn.grid( column=2, row=0, pady=ELEMENT_PADDING )
        self.buttons.append(self.solve_maze_btn)

        # 'Solve with Correct Path' button
        self.solve_maze_direct_btn = Button(self.__tk, text="Solve (correct path)", state="disabled", command=self.solve_maze("direct"), font=self.button_font)
        self.solve_maze_direct_btn.grid( column=3, row=0, pady=ELEMENT_PADDING )
        self.buttons.append(self.solve_maze_direct_btn)

        # 'Exit' button
        self.exit_btn = Button(self.__tk, text="Exit", state="normal", command=self.close, font=self.button_font)
        self.exit_btn.grid( column=4, columnspan=2, row=0, pady=ELEMENT_PADDING )
        self.buttons.append(self.exit_btn)

        # Labels and Entries for rows and columns
        self.rows_label = Label(self.__tk, text=f"Rows (Default {MAZE_ROWS}):", font=self.button_font)
        self.rows_label.grid(column=0, columnspan=2, row=1, pady=ELEMENT_PADDING)
        self.rows_entry = Entry(self.__tk, font=self.button_font)
        self.rows_entry.grid(column=2, row=1, pady=ELEMENT_PADDING)

        self.cols_label = Label(self.__tk, text=f"Columns(Default {MAZE_COLS}):", font=self.button_font)
        self.cols_label.grid(column=3, columnspan=2, row=1, pady=ELEMENT_PADDING)
        self.cols_entry = Entry(self.__tk, font=self.button_font)
        self.cols_entry.grid(column=5, row=1, pady=ELEMENT_PADDING)

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

    def set_speed(self):
        match self.speed:
            case "normal":
                self.speed = "fast"
            case "fast":
                self.speed = "instant"
            case "instant":
                self.speed = "slow"
            case "slow":
                self.speed = "normal"
        self.speed_btn.config(text=f"Speed: {self.speed}")

    def start_maze(self):
        self.create_canvas()

        # disable the buttons
        for btn in self.buttons:
            btn["state"] = "disabled"
        # Clear canvas
        self._canvas.delete("all")


        # Initiate the maze
        self.maze = Maze(self.maze_x, self.maze_y, self.rows, self.cols, self.cell_size, self, RANDOM_SEED, self.speed)
        # Reactivate buttons
        for btn in self.buttons:
            btn["state"] = "normal"

    
    def solve_maze(self, style="random"):
        def solve():
            # disable the buttons
            for btn in self.buttons:
                btn["state"] = "disabled"
            if style == "direct":
                self.maze._solve_r_direct(self.speed)
            elif style == "random":
                self.maze._solve_r(self.speed)
            # enable the buttons
            for btn in self.buttons:
                btn["state"] = "normal"
            self.solve_maze_btn["state"] = "disabled"
            self.solve_maze_direct_btn["state"] = "disabled"
        return solve

    def create_canvas(self):
        # canvas
        if self._canvas:
            self._canvas.delete()
        self._canvas = Canvas()

        #Get dimensions for the canvas
        canvas_width = self.__width * 0.99
        canvas_height = self.__height - SPACE_FOR_UI

        # Get rows and columns from entries
        try:
            self.rows = int(self.rows_entry.get())
            self.cols = int(self.cols_entry.get())
        except ValueError:
            self.rows = MAZE_ROWS
            self.cols = MAZE_COLS

        # Apply UI
        self._canvas.config( width=canvas_width, height=canvas_height, bg=BACKGROUND_COLOR )
        self._canvas.grid( column=0, columnspan=6,row=2 )

        # Count cell_size to fill the canvas with the maze
        self.cell_size = min( (canvas_width - MAZE_H_PADDING) // self.cols, (canvas_height - MAZE_V_PADDING) // self.rows )

        # Adjust maze to the center of the canvas
        self.maze_x = (self.__width - (self.cell_size * self.cols)) // 2
        self.maze_y = ((self.__height - SPACE_FOR_UI) - (self.cell_size * self.rows)) // 2