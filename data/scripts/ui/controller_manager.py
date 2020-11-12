import pygame

from data.scripts.config import RECONNECT_CONTROLLER


class ControllerManager:
    def __init__(self, game):
        self.game = game

        self.joysticks = self.get_joysticks()

        if self.joysticks:
            self.is_plugged = True
        else:
            self.is_plugged = False

    def check_plug(self):
        joystick_count = pygame.joystick.get_count()
        if not joystick_count and self.is_plugged:
            self.is_plugged = False
            self.game.render_mode = RECONNECT_CONTROLLER
        if joystick_count and not self.is_plugged:
            self.joysticks = self.get_joysticks()
            self.is_plugged = True
            self.game.input.control_mode = 'controller'

    def wait_for_reconnect(self):
        if pygame.joystick.get_count():
            self.is_plugged = True
            self.joysticks = self.get_joysticks()
        elif self.game.input.enter:
            self.game.input.control_mode = 'keyboard'

    def get_joysticks(self):
        joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        for joystick in joysticks:
            joystick.init()
        return joysticks

