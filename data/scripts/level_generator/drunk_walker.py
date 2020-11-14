from random import randint, choice

from data.scripts.level_generator.config import TAKEN
from data.scripts.level_generator.grid import Grid


class DrunkWalker:
    def __init__(self, grid):
        self.star_point = [randint(0, 9), randint(0, 9)]
        self.current = self.star_point
        self.grid = grid

    def drunk_walk(self, max_rooms):
        done = False
        while not done:
            self.grid.take(self.current)
            self.current = self.random_move()
            done = self.check_grid(max_rooms)
        return self.grid

    def random_move(self):
        return choice([pos for pos in self.grid.check_around(self.current) if pos])

    def check_grid(self, max_rooms):
        count = 0
        for room in self.grid:
            if room == TAKEN:
                count += 1

        return count == max_rooms




