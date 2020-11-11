TILE_SIZE = 20
DISPLAY_SIZE = [1280, 720]
GRID_SIZE = 32
CAMERA_SPEED = 20
FPS = 60
ENTITY_LIST = [['decor_0', 0, 0], ['decor_0', 1, 0], ['water', 0, 1], ['decor_1', 0, 0], ['decor_1', 1, 0],
               ['decor_1', 2, 0], ['decor_1', 3, 0], ['transitions_0', 0, 0], ['transitions_0', 1, 0],
               ['transitions_0', 2, 0], ['interior_1', 5, 2], ['climbing_0', 0, 0],
               ['item_spawners_0', 0, 0]]
ITEM_INDEX = {0: 'wheat_grain'}
ITEM_CONFIG = {
    'wheat_grain': [2, 2]
}
LINE_VFX = {
    'found_item': {
        'points': [[0, 0], [5, -5], [70, -5]],
        'color': (208, 223, 215),
        'width': 1,
        'speed': 0.03,
        'time_cap': True,
        'scroll_affected': True
    },
}
BEZIER_TYPES = {
    'bounce_out': [[2.4, 0.01], [1.25, 2.65]],
}

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 100, 100)
YELLOW = (255, 255, 0)
PURPLE = (102, 0, 102)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)

BLOCK = {'letter': 'B', 'name': 'blocks', 'color': BLACK}
NOTHING = 'N'
EXIT = {'letter': 'E', 'name': 'exit', 'color': BLUE}
SPAWN = {'letter': 'S', 'name': 'spawn', 'color': GREEN}
SPIKE = {'letter': 'W', 'name': 'spike', 'color': GRAY}
NEXT_LINE = '\n'

LEVEL_PATH = "level_generator/data/saved_levels/"
