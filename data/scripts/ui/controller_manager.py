import pygame

from data.scripts.config import RECONNECT_CONTROLLER


class ControllerManager:
    def __init__(self, game):
        self.game = game

        self.joysticks = []
        for i in range(pygame.joystick.get_count()):
            self.joysticks.append(pygame.joystick.Joystick(i))
            self.joysticks[-1].init()

        if self.joysticks:
            self.is_plugged = True
        else:
            self.is_plugged = False

    def check_plug(self):
        joystick_count = pygame.joystick.get_count()
        if not joystick_count and self.is_plugged:
            self.is_plugged = False
            self.game.render_mode = RECONNECT_CONTROLLER

    def wait_for_reconnect(self):
        joystick_count = pygame.joystick.get_count()
        if joystick_count:
            self.is_plugged = True
            joysticks = []
            for i in range(pygame.joystick.get_count()):
                joysticks.append(pygame.joystick.Joystick(i))
                joysticks[-1].init()
                self.joysticks = joysticks

