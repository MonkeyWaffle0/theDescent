import pygame

from data.scripts.config import *
from data.scripts.entities.base_entities import GameEntity


class Player(GameEntity):
    def __init__(self, game, entities, e_type, x, y, width, height):
        super().__init__(game, entities, e_type, x, y, width, height)
        self.climb_rect = pygame.Rect(self.x + self.width / 4, self.y + self.height / 2, self.width / 2, 2)
        self.climbing = False
        self.climb_speed = 1
        self.action = ''

        self.touching_item = None
        self.last_touching_item = self.touching_item

        self.color = GREEN

    def focus_scroll(self):
        return [self.x + self.width / 2 - DISPLAY_SIZE[0] / 2, self.y + self.height / 2 - DISPLAY_SIZE[1] / 2]

    def update(self):
        if self.game.input.down and self.momentum.air_time < 4:
            self.set_action('land')
            self.momentum.drop_through = 16
            if self.game.input.down_press:
                self.momentum.velocity[1] = -4

        self.momentum.update()
        self.momentum.air_time += 1
        movement = self.momentum.velocity.copy()

        collision_info = self.process_collisions(movement)

        if collision_info['bottom']:
            self.momentum.land()

        if self.momentum.air_time > 4:
            if self.animation_progress < 0.7:
                if movement[1] < 0:
                    self.set_action('jump')
                else:
                    self.set_action('fall')
        else:
            if movement[0] != 0:
                self.set_action('run')
            else:
                self.set_action('idle')

        if not self.climbing:
            if movement[0] > 0:
                self.set_flip(True)
            if movement[0] < 0:
                self.set_flip(False)

        self.render()

    def render(self):
        pygame.draw.rect(self.display, self.color, self.get_rect())

    def death(self):
        self.set_pos(self.game.active_scene.level_dic['spawn'][0])
