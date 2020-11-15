DUNGEON_TILE = 1024

SHAPES = {
    'I': {'width': DUNGEON_TILE, 'height': DUNGEON_TILE * 2, 'letter': 'I'},
    '_': {'width': DUNGEON_TILE * 2, 'height': DUNGEON_TILE, 'letter': '_'},
    'o': {'width': DUNGEON_TILE, 'height': DUNGEON_TILE, 'letter': 'o'},
    'O': {'width': DUNGEON_TILE * 2, 'height': DUNGEON_TILE * 2, 'letter': 'O'}
}

VERTICAL_SHAPE = 'I'
HORIZONTAL_SHAPE = '_'
BIG_SQUARE_SHAPE = 'O'
SMALL_SQUARE_SHAPE = 'o'
BIG_ROOMS_SHAPES = [VERTICAL_SHAPE, HORIZONTAL_SHAPE, BIG_SQUARE_SHAPE]

EMPTY = 0
TAKEN = 1
ROOM_RANGE = (8, 12)

ROOM1 = {'shape': SHAPES['I'], 'doors': {'top': False, 'bottom': False}, 'spawn': False, 'done': False}
ROOM2 = {'shape': SHAPES['_'], 'doors': {'left': False, 'right': False}, 'spawn': False, 'done': False}
ROOM3 = {'shape': SHAPES['o'], 'doors': {'top': False, 'bottom': False, 'left': False}, 'spawn': True, 'done': False}
ROOM4 = {'shape': SHAPES['O'], 'doors': {'topleft_top': False, 'bottomright_right': False}, 'spawn': False,
         'done': False}

ROOM = {'pos': (0, 0), 'top': False, 'bottom': False, 'left': False, 'right': False,
        'shape': SMALL_SQUARE_SHAPE}
OPPOSITE = {'top': 'bottom', 'bottom': 'top', 'left': 'right', 'right': 'left'}

ROOMS = [ROOM1, ROOM2, ROOM3, ROOM4]
