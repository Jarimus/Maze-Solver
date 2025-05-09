# Screen resolution constants. Set to 0 for fullscreen.
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
SPACE_FOR_UI = 150

# Maze constants. Screen space is used most optimally when the cols/rows ratio is around 2:1.
MAZE_V_PADDING = 20 # Vertical padding
MAZE_H_PADDING = 20 # Horizontal padding
MAZE_COLS = 25
MAZE_ROWS = 10

# Maze speed constants. Seconds to draw a frame (draw a cell, draw a line)
MAZE_SPEED_SLOW = 0.1
MAZE_SPEED_NORMAL = 0.025
MAZE_SPEED_FAST = 0.005
RANDOM_SEED = None # Set to an int to generate the same mazes each time

# Line constants
WALL_LINE_THICKNESS = 2
PATH_LINE_THICKNESS = 3

# Widget constants
ELEMENT_PADDING = 10
FONT_SIZE = 14

# Color constants
WALL_COLOR = "white"
BACKGROUND_COLOR = "black"
CORRECT_PATH_COLOR = "green"
WRONG_PATH_COLOR = "black" # default 'red'. Set to background color to 'erase' the incorrect paths
EXIT_COLOR = "yellow"