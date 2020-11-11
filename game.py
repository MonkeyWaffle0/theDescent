import pygame

from data.scripts.helper.level_handler import LevelHandler
from data.scripts.scenes.main_menu import MainMenu
from data.scripts.ui.gui import GUI
from data.scripts.ui.user_input import InputManager

from data.scripts.entities.entity_manager import EntityManager
from data.scripts.window import GameWindow
from data.scripts.vfx.transitions import Transitions

from data.scripts.config import FPS


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption('game base')

        self.window = GameWindow()
        self.input = InputManager(self)
        self.entities = EntityManager(self)
        self.gui = GUI(self)
        self.clock = pygame.time.Clock()
        self.transitions = Transitions(self)
        self.level_handler = LevelHandler(self)

        self.active_scene = MainMenu(self)

        self.render_mode = 'game'

        self.game_timer = 0

    def update(self):
        # self.fps.frame_begin()

        if self.render_mode == 'game':
            self.active_scene.handle_game_frame()

        if self.render_mode == 'transition':
            self.transitions.update()

        self.gui.update()
        # self.fps.frame_end()
        self.window.update(self)
        self.clock.tick(FPS)

    def run(self):
        while self.active_scene is not None:
            self.update()


if __name__ == '__main__':
    Game().run()
