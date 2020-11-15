import pygame

from level_creator.data.scripts.config import DISPLAY_SIZE, BLACK, LEVEL_WINDOW


class GameWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode([DISPLAY_SIZE[0], DISPLAY_SIZE[1]], 0, 32)

        self.display = pygame.Surface(DISPLAY_SIZE)
        self.size = DISPLAY_SIZE

    def update(self, game):
        pygame.draw.line(self.display, BLACK, (LEVEL_WINDOW[0], 0), (LEVEL_WINDOW[0], LEVEL_WINDOW[1]))
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
        pygame.display.update()
        game.clock.tick(60)
