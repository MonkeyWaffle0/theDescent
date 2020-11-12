import pygame

from data.scripts.config import DISPLAY_SIZE, RED, ORANGE
from level_generator.data.scripts.config import FONT


class ReconnectController:
    def __init__(self, game):
        self.game = game
        self.text1 = FONT.render('Controller disconnected !', False, RED)
        self.text1_rect = self.text1.get_rect()
        self.text1_rect.center = (DISPLAY_SIZE[0] // 2, DISPLAY_SIZE[1] // 2 - 20)
        self.text2 = FONT.render('Reconnect controller or press Enter to play with keyboard', False, ORANGE)
        self.text2_rect = self.text2.get_rect()
        self.text2_rect.center = (DISPLAY_SIZE[0] // 2, DISPLAY_SIZE[1] // 2 + 20)

    def update(self):
        self.game.active_scene.handle_game_frame()

        self.game.input.controller_manager.wait_for_reconnect()
        if self.game.input.controller_manager.is_plugged or self.game.input.control_mode == 'keyboard':
            self.game.render_mode = 'game'

        mask_surf = pygame.Surface(DISPLAY_SIZE)
        mask_surf.set_alpha(200)
        mask_surf.blit(self.text1, self.text1_rect)
        mask_surf.blit(self.text2, self.text2_rect)
        self.game.window.display.blit(mask_surf, (0, 0))
