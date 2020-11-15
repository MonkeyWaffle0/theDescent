import pygame

from level_creator.data.scripts.config import GRID_SIZE, BLACK, GREEN, BLUE


class Block:
    def __init__(self, game, x, y, block_type):
        self.game = game
        self.display = game.window.display
        self.x = x
        self.y = y
        self.type = block_type

        self.width = self.height = GRID_SIZE

    def update(self):
        pygame.draw.rect(self.display, self.type['color'], self.get_rect())

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
