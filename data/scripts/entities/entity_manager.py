from data.scripts.core_funcs import *
from data.scripts.entities.player import Player


class EntityManager:
    def __init__(self, game):
        self.game = game
        self.collision_blocks = []
        self.touchables = []
        self.entities = []
        self.player = None

    def reset_entities(self):
        self.entities = []

    def reset_collisions(self):
        self.collision_blocks = []

    def reset_everything(self):
        self.collision_blocks = []
        self.touchables = []
        self.entities = []

    def update(self):
        for entity in self.entities:
            entity.update()

    def create_player(self):
        self.player = Player(self.game, self, 'player', -50, -50, GRID_SIZE, GRID_SIZE)
