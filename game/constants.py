# list of constants used in the game

# --- safe to play with
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 2 * 16 * 16
SCREEN_HEIGHT = 2 * 9 * 16

#  tile options be sure ratio of one tile is divisible within screen size and tilesheet
TILESIZE = 32
TILESHEET_SIZES = [(198, 128)
                   ]  # tilesizes [(w1,h1)...] list for all tilesheets

FONT_PATH = 'lib/fonts/pixel.ttf'
FONT_SIZE = 20

# title
CAPTION = "Tile Editor"

# --- dont change these unless method calls to classes are also changed
BRUSH_INIT_1 = "curr"
BRUSH_INIT_2 = "place"

# tile controller starts with first tile at 0,0 on tilesheet finishes one row before moving to next column 0,0 -> 1, 0 -> 1, m ... n, 0 -> n,m
TILE_CONTROLLER = 0, 0
