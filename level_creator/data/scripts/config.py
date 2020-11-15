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

LEVEL_PATH = "C:/Users/reafl/PycharmProjects/theDescent/level_creator/data/saved_levels/"

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

SMALL_LEFT_INDEX = 495
SMALL_RIGHT_INDEX = 526
SMALL_TOP_INDEX = 16
SMALL_BOTTOM_INDEX = 1038

BIG_TOPLEFT_TOP_INDEX = 16
BIG_TOPLEFT_LEFT_INDEX = 910
BIG_TOPRIGHT_TOP_INDEX = 48
BIG_TOPRIGHT_RIGHT_INDEX = 973
BIG_BOTTOMLEFT_BOTTOM_INDEX = 4111
BIG_BOTTOMLEFT_LEFT_INDEX = 3120
BIG_BOTTOMRIGHT_BOTTOM_INDEX = 4142
BIG_BOTTOMRIGHT_RIGHT_INDEX = 3183

VERTICAL_TOP_INDEX = 16
VERTICAL_BOTTOM_INDEX = 2095
VERTICAL_TOPLEFT_INDEX = 495
VERTICAL_TOPRIGHT_INDEX = 526
VERTICAL_BOTTOMLEFT_INDEX = 1617
VERTICAL_BOTTOMRIGHT_INDEX = 1648

HORIZONTAL_LEFT_INDEX = 975
HORIZONTAL_RIGHT_INDEX = 1038
HORIZONTAL_TOPLEFT_INDEX = 16
HORIZONTAL_TOPRIGHT_INDEX = 48
HORIZONTAL_BOTTOMLEFT_INDEX = 2030
HORIZONTAL_BOTTOMRIGHT_INDEX = 2062


