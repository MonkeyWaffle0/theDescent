import pickle

from data.scripts.config import BLOCK, GRID_SIZE, NEXT_LINE, LEVEL_PATH, SPAWN, EXIT, SPIKE
from data.scripts.entities.exit import Exit
from data.scripts.entities.spike import Spike
from data.scripts.entities.wall import Wall
from level_creator.data.scripts.config import SPIKE_UP, SPIKE_DOWN, SPIKE_LEFT, SPIKE_RIGHT, SPIKES


class LevelHandler:
    def __init__(self, game):
        self.game = game

    def string_to_level(self, level):
        x = 0
        y = 0
        level_dic = {'blocks': [],
                     'spawn': [],
                     'exit': [],
                     'spike': []}
        for char in level['string']:
            if char == BLOCK['letter']:
                level_dic[BLOCK['name']].append(
                    Wall(self.game, self.game.entities, x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            elif char == SPAWN['letter']:
                pos = (x * GRID_SIZE, y * GRID_SIZE)
                level_dic[SPAWN['name']].append(pos)
                self.game.entities.player.set_pos(pos)
            elif char == EXIT['letter']:
                level_dic[EXIT['name']].append(
                    Exit(self.game, self.game.entities, x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            elif char in SPIKES:
                level_dic[SPIKE['name']].append(
                    Spike(self.game, self.game.entities, x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE, char))
            x += 1
            if char == NEXT_LINE:
                y += 1
                x = 0

        return level_dic

    def load_level(self, name):
        try:
            with open(LEVEL_PATH + name + '.pickle', 'rb') as file:
                level = pickle.load(file)
            print("Level " + name + " loaded.\n")
            return self.string_to_level(level)
        except FileNotFoundError:
            print("No such file found.\n")
