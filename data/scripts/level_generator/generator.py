from random import randint, choice

from data.scripts.level_generator.config import ROOM_RANGE, SHAPES, ROOMS
from data.scripts.level_generator.drunk_walker import DrunkWalker
from data.scripts.level_generator.grid import Grid


class Generator:
    def __init__(self):
        # self.game = game
        self.level_list = []
        self.grid = Grid()
        self.drunk_walker = DrunkWalker(self.grid)

    def generate(self):
        self.grid = self.drunk_walker.drunk_walk(20)
        print(self.grid)

    def choose_door(self, room):
        for door, value in room['doors'].items():
            if value:
                if door == 'left':
                    self.current = self.grid.get_left(self.current)
                elif door == 'right':
                    self.current = self.grid.get_right(self.current)
                elif door == 'top':
                    self.current = self.grid.get_top(self.current)
                elif door == 'bottom':
                    self.current = self.grid.get_bottom(self.current)
                elif door == 'topleft_top':
                    self.current = self.grid.get_left(self.grid.get_top(self.current))
                elif door == 'bottomright_right':
                    self.current = self.grid.get_right(self.grid.get_right(self.grid.get_bottom(self.current)))
                room['doors'][door] = True
                return True
            return False


generator = Generator()
generator.generate()
