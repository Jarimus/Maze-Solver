# Screen resolution constants. Set to 0 for fullscreen.
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0

# Cell constants
CELL_SIZE = 0 # If set to zero, the cell size is set to fill the canvas.

# Maze constants. Screen space is used most optimally when the cols/rows ratio is around 2:1.
MAZE_V_PADDING = 50 # Vertical padding
MAZE_H_PADDING = 50 # Horizontal padding
MAZE_COLS = 22
MAZE_ROWS = 10
MAZE_GENERATION_SPEED = 0.005 # The delay between each draw in seconds
MAZE_SOLVE_SPEED = 0.05 # The delay between each line draw in seconds
RANDOM_SEED = None # Set to an int to generate the same mazes each time

# Line constants
WALL_LINE_THICKNESS = 2
PATH_LINE_THICKNESS = 3

# Color constants
WALL_COLOR = "white"
BACKGROUND_COLOR = "black"
CORRECT_PATH_COLOR = "green"
WRONG_PATH_COLOR = "red"