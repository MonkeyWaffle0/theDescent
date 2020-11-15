import pygame

DISPLAY_SIZE = [1300, 1024]
GRID_SIZE = 16
FPS = 300


GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 100, 100)
YELLOW = (255, 255, 0)
PURPLE = (102, 0, 102)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)

LEVEL_PATH = "/level_creator/data/saved_levels/"

BLOCK = {'letter': 'B', 'name': 'blocks', 'color': BLACK}
NOTHING = 'N'
EXIT = {'letter': 'E', 'name': 'exit', 'color': BLUE}
SPAWN = {'letter': 'S', 'name': 'spawn', 'color': GREEN}
SPIKE_UP = {'letter': 'M', 'name': 'spike_up', 'color': GRAY, 'direction': 'up'}
SPIKE_DOWN = {'letter': 'W', 'name': 'spike_down', 'color': GRAY, 'direction': 'down'}
SPIKE_LEFT = {'letter': 'L', 'name': 'spike_left', 'color': GRAY, 'direction': 'left'}
SPIKE_RIGHT = {'letter': 'R', 'name': 'spike_right', 'color': GRAY, 'direction': 'right'}
SPIKES = {
    SPIKE_UP['letter']: SPIKE_UP,
    SPIKE_DOWN['letter']: SPIKE_DOWN,
    SPIKE_LEFT['letter']: SPIKE_LEFT,
    SPIKE_RIGHT['letter']: SPIKE_RIGHT
}
NEXT_LINE = '\n'

pygame.font.init()
FONT = pygame.font.Font('freesansbold.ttf', 18)


DUNGEON_TILE = 512

SHAPES = {
    'I': {'width': DUNGEON_TILE, 'height': DUNGEON_TILE * 2, 'letter': 'I'},
    '_': {'width': DUNGEON_TILE * 2, 'height': DUNGEON_TILE, 'letter': '_'},
    'o': {'width': DUNGEON_TILE, 'height': DUNGEON_TILE, 'letter': 'o'},
    'O': {'width': DUNGEON_TILE * 2, 'height': DUNGEON_TILE * 2, 'letter': 'O'}
}

SMALL_LEFT_INDEX = 513
SMALL_RIGHT_INDEX = 544
SMALL_TOP_INDEX = 16
SMALL_BOTTOM_INDEX = 1010

BIG_TOPLEFT_TOP_INDEX = 16
BIG_TOPLEFT_LEFT_INDEX = 960
BIG_TOPRIGHT_TOP_INDEX = 48
BIG_TOPRIGHT_RIGHT_INDEX = 1023
BIG_BOTTOMLEFT_BOTTOM_INDEX = 4048
BIG_BOTTOMLEFT_LEFT_INDEX = 3072
BIG_BOTTOMRIGHT_BOTTOM_INDEX = 4081
BIG_BOTTOMRIGHT_RIGHT_INDEX = 3135

VERTICAL_TOP_INDEX = 16
VERTICAL_BOTTOM_INDEX = 2032
VERTICAL_TOPLEFT_INDEX = 480
VERTICAL_TOPRIGHT_INDEX = 511
VERTICAL_BOTTOMLEFT_INDEX = 1536
VERTICAL_BOTTOMRIGHT_INDEX = 1567

HORIZONTAL_LEFT_INDEX = 960
HORIZONTAL_RIGHT_INDEX = 1023
HORIZONTAL_TOPLEFT_INDEX = 16
HORIZONTAL_TOPRIGHT_INDEX = 48
HORIZONTAL_BOTTOMLEFT_INDEX = 1999
HORIZONTAL_BOTTOMRIGHT_INDEX = 2033


