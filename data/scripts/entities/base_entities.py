import pygame

import data.scripts.rapid_potato.entities as e
from data.scripts.entities.physics.momentum import Momentum


class GameEntity(e.Entity):
    def __init__(self, game, entities, e_type, x, y, x_size, y_size):
        super().__init__(x, y, x_size, y_size, e_type)
        self.game = game
        self.display = game.window.display
        self.entities_ptr = entities
        self.momentum = Momentum(game, self)
        self.in_water = False
        self.game.entities.entities.append(self)
        self.visible = True

    def process_collisions(self, movement):
        return self.move(movement, self.game.entities.collisions.collision_tiles,
                         self.game.entities.collisions.collision_ramps,
                         self.game.entities.collisions.collision_platforms)

    def mouse_is_on(self):
        return self.get_rect().collidepoint(self.game.input.mouse_pos)

    def player_is_on(self):
        return self.game.entities.player.get_rect().colliderect(self.get_rect())

    def get_camera_rect(self):
        return pygame.Rect(self.x - self.game.active_scene.camera.x, self.y - self.game.active_scene.camera.y, self.width, self.height)
