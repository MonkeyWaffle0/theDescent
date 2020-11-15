from random import randint, choice

from data.scripts.level_generator.config import TAKEN, OPPOSITE, EMPTY
from data.scripts.level_generator.grid import Grid


class DrunkWalker:
    def __init__(self, grid):
        self.current = [randint(0, 9), randint(0, 9)]
        self.previous = None
        self.grid = grid

    def drunk_walk(self, max_rooms):
        done = False
        while not done:
            self.grid.take(self.current)
            if self.previous:
                self.make_connection(self.previous, self.current)
            self.previous = self.current
            self.current = self.random_move()
            done = self.check_grid(max_rooms)
        return self.grid

    def random_move(self):
        return choice([pos for pos in self.grid.check_around(self.current).values() if pos])

    def make_connection(self, pos1, pos2):
        around = self.grid.check_around(pos1)
        for direction, room in around.items():
            if room == pos2:
                self.grid.get_room(pos1)[direction] = True
                self.grid.get_room(pos2)[OPPOSITE[direction]] = True

    def check_grid(self, max_rooms):
        count = 0
        for room in self.grid:
            if room != EMPTY:
                count += 1
        return count == max_rooms




