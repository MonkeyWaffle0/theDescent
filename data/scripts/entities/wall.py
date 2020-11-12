import pygame

from data.scripts.config import BLACK
from data.scripts.entities.base_entities import GameEntity


class Wall(GameEntity):
    def __init__(self, game, entities, x, y, width, height, e_type='wall'):
        super().__init__(game, entities, e_type, x, y, width, height)
        self.color = BLACK
        self.game.entities.collisions.collision_tiles.append(self.get_rect())

    def update(self):
        pygame.draw.rect(self.display, self.color, self.get_camera_rect())
