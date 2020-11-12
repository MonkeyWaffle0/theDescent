import pygame

from data.scripts.config import GRAY, GRID_SIZE
from data.scripts.entities.base_entities import GameEntity
from level_generator.data.scripts.config import SPIKE_UP, SPIKE_DOWN, SPIKE_LEFT, SPIKE_RIGHT


class Spike(GameEntity):
    def __init__(self, game, entities, x, y, width, height, direction, e_type='spike'):
        super().__init__(game, entities, e_type, x, y, width, height)
        self.color = GRAY

        self.topleft = (self.x, self.y)
        self.topright = (self.x + GRID_SIZE, self.y)
        self.bottomleft = (self.x, self.y + GRID_SIZE)
        self.bottomright = (self.x + GRID_SIZE, self.y + GRID_SIZE)
        self.midtop = (self.x + GRID_SIZE // 2, self.y)
        self.midbottom = (self.x + GRID_SIZE // 2, self.y + GRID_SIZE)
        self.midleft = (self.x, self.y + GRID_SIZE // 2)
        self.midright = (self.x + GRID_SIZE, self.y + GRID_SIZE // 2)

        if direction == SPIKE_UP['letter']:
            self.points = [self.bottomleft, self.bottomright, self.midtop]
        elif direction == SPIKE_DOWN['letter']:
            self.points = [self.topleft, self.topright, self.midbottom]
        elif direction == SPIKE_LEFT['letter']:
            self.points = [self.topright, self.bottomright, self.midleft]
        elif direction == SPIKE_RIGHT['letter']:
            self.points = [self.topleft, self.bottomleft, self.midright]

    def get_camera_points(self):
        return [
            (self.points[0][0] - self.game.active_scene.camera.scroll[0],
             self.points[0][1] - self.game.active_scene.camera.scroll[1]),
            (self.points[1][0] - self.game.active_scene.camera.scroll[0],
             self.points[1][1] - self.game.active_scene.camera.scroll[1]),
            (self.points[2][0] - self.game.active_scene.camera.scroll[0],
             self.points[2][1] - self.game.active_scene.camera.scroll[1])]

    def render(self):
        pygame.draw.polygon(self.display, self.color, self.get_camera_points())

    def kill(self):
        return self.game.entities.player.death()

    def update(self):
        self.render()
        if self.player_is_on():
            return self.kill()
