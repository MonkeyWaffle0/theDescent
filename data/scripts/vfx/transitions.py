import pygame
from data.scripts.config import *
from data.scripts.core_funcs import *

TRANSITION_TYPES = {
    'startvillage>house': 'enter',
    'house>startvillage': 'exit',
}


class Transitions:
    def __init__(self, game):
        self.game = game
        self.time_remaining = 0
        self.type = None

    def start_transition(self):
        self.time_remaining = 60
        self.max_time = self.time_remaining
        self.type = 'enter'
        self.reloaded_map = False

    def update(self):
        self.time_remaining -= 1
        if self.time_remaining <= 0:
            self.game.minigame_manager.next_game()
            self.game.render_mode = 'game'

        self.game.active_scene.handle_game_frame()

        if self.time_remaining == self.max_time / 2:
            self.game.entities.reset_entities()

        # exit and enter have the same animation
        if self.type == 'exit':
            self.type = 'enter'

        if self.type == 'enter':
            mask_surf = pygame.Surface(DISPLAY_SIZE)
            if self.time_remaining / self.max_time >= 0.5:
                pygame.draw.circle(mask_surf,
                                   (255, 255, 255),
                                   get_center_pos(self.game.window.display),
                                   int(((self.time_remaining - self.max_time / 2) / (self.max_time / 2)) ** 4 * DISPLAY_SIZE[0]))
            else:
                pygame.draw.circle(mask_surf, (255, 255, 255), get_center_pos(self.game.window.display),
                                   int((1 - (self.time_remaining / (self.max_time / 2))) ** 4 * DISPLAY_SIZE[0]))

            mask_surf.set_colorkey((255, 255, 255))
            self.game.window.display.blit(mask_surf, (0, 0))
