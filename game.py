import pygame

from data.scripts.helper.level_handler import LevelHandler
from data.scripts.scenes.main_menu import MainMenu
from data.scripts.ui.gui import GUI
from data.scripts.ui.user_input import InputManager

from data.scripts.entities.entity_manager import EntityManager
from data.scripts.vfx.reconnect_controller import ReconnectController
from data.scripts.window import GameWindow
from data.scripts.vfx.transitions import Transitions

from data.scripts.config import FPS, GAME, TRANSITION, RECONNECT_CONTROLLER


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption('The Descent')

        self.window = GameWindow()
        self.input = InputManager(self)
        self.entities = EntityManager(self)
        self.gui = GUI(self)
        self.clock = pygame.time.Clock()
        self.transitions = Transitions(self)
        self.reconnect_controller = ReconnectController(self)
        self.level_handler = LevelHandler(self)

        self.active_scene = MainMenu(self)

        self.render_mode = 'game'

        self.game_timer = 0

    def update(self):
        if self.render_mode == GAME:
            self.active_scene.handle_game_frame()

        if self.render_mode == TRANSITION:
            self.transitions.update()

        if self.render_mode == RECONNECT_CONTROLLER:
            self.reconnect_controller.update()

        self.gui.update()
        self.window.update(self)
        self.clock.tick(FPS)

    def run(self):
        while self.active_scene is not None:
            self.update()


if __name__ == '__main__':
    Game().run()
