import pygame

from data.scripts.config import BLUE
from data.scripts.entities.base_entities import GameEntity
from data.scripts.scenes.game_scene import GameScene


class Exit(GameEntity):
    def __init__(self, game, entities, x, y, width, height, e_type='wall'):
        super().__init__(game, entities, e_type, x, y, width, height)
        self.color = BLUE

    def render(self):
        pygame.draw.rect(self.display, self.color, self.get_camera_rect())

    def next_level(self):
        print('yes ma gueule')

    def update(self):
        self.render()
        if self.player_is_on():
            self.next_level()
