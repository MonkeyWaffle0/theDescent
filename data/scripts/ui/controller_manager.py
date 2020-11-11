import pygame


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
            print('deconnected')
            self.is_plugged = False
            self.wait_for_reconnect()

    def wait_for_reconnect(self):
        joystick_count = pygame.joystick.get_count()
        if not joystick_count:
            print('you need to reconnect')
            return self.wait_for_reconnect()
        else:
            print('reconnected')
            joysticks = []
            for i in range(pygame.joystick.get_count()):
                joysticks.append(pygame.joystick.Joystick(i))
                joysticks[-1].init()
                self.joysticks = joysticks

