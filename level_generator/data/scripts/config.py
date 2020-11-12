import pygame

LEVEL_WINDOW = [1280, 640]
DISPLAY_SIZE = [1280, 720]
GRID_SIZE = 32
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

LEVEL_PATH = "C:/Users/reafl/PycharmProjects/theDescent/level_generator/data/saved_levels/"

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
