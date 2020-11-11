import pygame

from data.scripts.config import DISPLAY_SIZE, RED
from level_generator.data.scripts.config import FONT


class ReconnectController:
    def __init__(self, game):
        self.game = game
        self.text = FONT.render('Controller disconnected !', False, RED)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (DISPLAY_SIZE[0] // 2, DISPLAY_SIZE[1] // 2)

    def update(self):
        self.game.active_scene.handle_game_frame()

        self.game.input.controller_manager.wait_for_reconnect()
        if self.game.input.controller_manager.is_plugged:
            self.game.render_mode = 'game'

        mask_surf = pygame.Surface(DISPLAY_SIZE)
        mask_surf.set_alpha(200)
        mask_surf.blit(self.text, self.text_rect)
        self.game.window.display.blit(mask_surf, (0, 0))
