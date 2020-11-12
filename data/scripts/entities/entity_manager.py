import data.scripts.rapid_potato.entities as e
from data.scripts.core_funcs import *
from data.scripts.entities.collision_lists import CollisionLists
from data.scripts.entities.player import Player


class EntityManager:
    def __init__(self, game):
        self.game = game
        self.collision_blocks = []

        e.set_global_colorkey((0, 0, 0))
        e.load_animations2('data/images/animations')
        e.load_particle_images('data/images/particles')

        self.entity_config = {
            'player': {'offset': [-2, -2]},
        }

        self.entities = []

    def reset_entities(self):
        self.entities = []

    def update(self):
        for entity in self.entities:
            entity.update()

    def reset(self):
        self.collision_blocks = []
        self.entities = []

    def create_player(self):
        self.player = Player(self.game, self, 'player', -50, -50, GRID_SIZE, GRID_SIZE)
