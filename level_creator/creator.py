import pygame

from data.scripts.ui.user_input import InputManager

from data.scripts.window import GameWindow

from data.scripts.config import FPS
from level_creator.data.scripts.scenes.GeneratorScene import GeneratorScene


class LevelGenerator:
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption('level generator')

        self.window = GameWindow()
        self.input = InputManager(self)
        self.clock = pygame.time.Clock()

        self.active_scene = GeneratorScene(self)

        self.game_timer = 0

    def update(self):
        self.active_scene.handle_game_frame()
        self.window.update(self)
        self.clock.tick(FPS)

    def run(self):
        while self.active_scene is not None:
            self.update()


if __name__ == '__main__':
    LevelGenerator().run()
