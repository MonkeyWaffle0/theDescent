from random import randint, choice

from data.scripts.level_generator.config import ROOM_RANGE, SHAPES, ROOMS, BIG_ROOMS_SHAPES, EMPTY, VERTICAL_SHAPE, \
    HORIZONTAL_SHAPE, BIG_SQUARE_SHAPE, SMALL_SQUARE_SHAPE
from data.scripts.level_generator.drunk_walker import DrunkWalker
from data.scripts.level_generator.grid import Grid


class Generator:
    def __init__(self):
        # self.game = game
        self.level_list = []
        self.grid = Grid()
        self.drunk_walker = DrunkWalker(self.grid)

    def generate(self):
        self.grid = self.drunk_walker.drunk_walk(randint(ROOM_RANGE[0], ROOM_RANGE[1]))
        self.make_big_rooms(4)

    def make_big_rooms(self, amount):
        for _ in range(amount):
            shape = choice(BIG_ROOMS_SHAPES)
            for room in self.grid:
                if room != EMPTY:
                    self.create_big_room(room)
                    if (shape == VERTICAL_SHAPE and self.create_vertical_room(room)) or (
                            shape == HORIZONTAL_SHAPE and self.create_horizontal_room(room)) or (
                            shape == BIG_SQUARE_SHAPE and self.create_big_room(room)):
                        break

    def create_vertical_room(self, room):
        if room['shape'] == SMALL_SQUARE_SHAPE and room['bottom'] and self.grid.get_grid_bottom(room['pos'])['top']:
            self.grid.get_grid_bottom(room['pos'])['shape'] = VERTICAL_SHAPE
            room['shape'] = VERTICAL_SHAPE
            return True
        return False

    def create_horizontal_room(self, room):
        if room['shape'] == SMALL_SQUARE_SHAPE and room['right'] and self.grid.get_grid_right(room['pos'])['left']:
            self.grid.get_grid_right(room['pos'])['shape'] = HORIZONTAL_SHAPE
            room['shape'] = HORIZONTAL_SHAPE
            return True
        return False

    def create_big_room(self, room):
        if room['shape'] == SMALL_SQUARE_SHAPE:
            rooms = [room, self.grid.get_grid_right(room['pos']), self.grid.get_grid_bottom(room['pos'])]
            if rooms[1] and rooms[2]:
                rooms.append(self.grid.get_grid_right(self.grid.get_grid_bottom(room['pos'])['pos']))
            if EMPTY not in rooms and None not in rooms:
                room['shape'] = BIG_SQUARE_SHAPE
                self.grid.get_grid_right(room['pos'])['shape'] = BIG_SQUARE_SHAPE
                self.grid.get_grid_bottom(room['pos'])['shape'] = BIG_SQUARE_SHAPE
                self.grid.get_grid_right(self.grid.get_grid_bottom(room['pos'])['pos'])['shape'] = BIG_SQUARE_SHAPE
                return True
        return False


generator = Generator()
generator.generate()

