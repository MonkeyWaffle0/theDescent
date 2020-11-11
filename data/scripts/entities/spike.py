import pygame

from data.scripts.config import GRAY, GRID_SIZE
from data.scripts.entities.base_entities import GameEntity
from level_generator.data.scripts.config import SPIKE_UP, SPIKE_DOWN, SPIKE_LEFT, SPIKE_RIGHT


class Spike(GameEntity):
    def __init__(self, game, entities, x, y, width, height, char, e_type='spike'):
        super().__init__(game, entities, e_type, x, y, width, height)
        self.color = GRAY
        self.direction = self.char_to_direction(char)

    def char_to_direction(self, char):
        if char == SPIKE_UP['letter']:
            return 'up'
        elif char == SPIKE_DOWN['letter']:
            return 'down'
        elif char == SPIKE_LEFT['letter']:
            return 'left'
        elif char == SPIKE_RIGHT['letter']:
            return 'right'

    def render(self):
        if self.direction == 'up':
            pygame.draw.polygon(self.display, self.color, [(self.x, self.y + GRID_SIZE), (self.x + GRID_SIZE // 2, self.y),
                                                           (self.x + GRID_SIZE, self.y + GRID_SIZE)])
        elif self.direction == 'down':
            pygame.draw.polygon(self.display, self.color,
                                [(self.x, self.y), (self.x + GRID_SIZE // 2, self.y + GRID_SIZE),
                                 (self.x + GRID_SIZE, self.y)])
        elif self.direction == 'left':
            pygame.draw.polygon(self.display, self.color,
                                [(self.x + GRID_SIZE, self.y), (self.x, self.y + GRID_SIZE // 2),
                                 (self.x + GRID_SIZE, self.y + GRID_SIZE)])
        elif self.direction == 'right':
            pygame.draw.polygon(self.display, self.color,
                                [(self.x, self.y), (self.x + GRID_SIZE, self.y + GRID_SIZE // 2),
                                 (self.x, self.y + GRID_SIZE)])

    def kill(self):
        return self.game.entities.player.death()

    def update(self):
        self.render()
        if self.player_is_on():
            return self.kill()
