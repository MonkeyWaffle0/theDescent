import pygame
from pygame.locals import *

from data.scripts.config import RECONNECT_CONTROLLER
from data.scripts.ui.controller_manager import ControllerManager


class InputManager:
    def __init__(self, game):
        self.game = game
        self.right = False
        self.left = False
        self.down_press = False
        self.interact = False
        self.jump = False
        self.released_jump = True
        self.down = False
        self.attempting_climb = False
        self.up = False
        self.left_click = False
        self.just_clicked = False
        self.enter = False

        self.controller_manager = ControllerManager(game)
        self.controller_deadzone = 30
        self.controller_x = 0
        self.controller_y = 0
        self.A = False

        self.control_mode = 'controller' if self.controller_manager.is_plugged else 'keyboard'

        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pos = [self.mouse_pos[0], self.mouse_pos[1]]

    def reset(self):
        self.right = False
        self.left = False
        self.down_press = False
        self.interact = False
        self.jump = False
        self.down = False
        self.attempting_climb = False
        self.up = False
        self.left_click = False

    def get_updates(self):
        self.interact = False
        self.down_press = False
        self.attempting_climb = False
        self.left_click = False
        self.just_clicked = False
        self.jump = False
        self.enter = False

        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pos = [self.mouse_pos[0], self.mouse_pos[1]]

        self.controller_manager.check_plug()

        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            self.filter_quit_event(pressed_keys, event)
            if self.control_mode == 'keyboard':
                self.handle_keyboard_input(event)
            elif self.control_mode == 'controller':
                self.handle_controller_input(event)
                self.joystick_to_input()

    def filter_quit_event(self, pressed_keys, event):
        quit_attempt = False
        if event.type == pygame.QUIT:
            quit_attempt = True
        elif event.type == pygame.KEYDOWN:
            alt_pressed = pressed_keys[pygame.K_LALT] or \
                          pressed_keys[pygame.K_RALT]
            if event.key == pygame.K_ESCAPE or (event.key == pygame.K_F4 and alt_pressed):
                quit_attempt = True

        if quit_attempt:
            self.game.active_scene.terminate()

    def handle_keyboard_input(self, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                self.jump = True
                self.released_jump = False
            if event.key == K_d:
                self.right = True
            if event.key == K_a:
                self.left = True
            if event.key == K_s:
                self.down = True
                self.down_press = True
            if event.key == K_w:
                self.attempting_climb = True
                self.up = True
            if event.key == K_e:
                self.interact = True
        if event.type == KEYUP:
            if event.key == K_d:
                self.right = False
            if event.key == K_a:
                self.left = False
            if event.key == K_s:
                self.down = False
            if event.key == K_w:
                self.up = False
            if event.key == K_SPACE:
                self.jump = False
                self.released_jump = True
        if event.type == MOUSEBUTTONDOWN:
            self.left_click = True
        if event.type == MOUSEBUTTONUP:
            self.just_clicked = True
            self.left_click = False

    def handle_controller_input(self, event):
        if self.game.render_mode == RECONNECT_CONTROLLER and event.type == KEYDOWN and event.key == K_RETURN:
            self.enter = True
        if event.type == JOYBUTTONDOWN:
            if event.button == 0:
                self.jump = True
                self.A = True
                self.released_jump = False
        if event.type == JOYBUTTONUP:
            if event.button == 0:
                self.jump = False
                self.A = False
                self.released_jump = True
        if event.type == JOYAXISMOTION:
            if event.axis == 0:
                self.controller_x = event.value * 100
            elif event.axis == 1:
                self.controller_y = event.value * 100

    def joystick_to_input(self):
        self.left = False
        self.right = False
        if abs(self.controller_x) > self.controller_deadzone:
            if self.controller_x > 0:
                self.right = True
            elif self.controller_x < 0:
                self.left = True
