import pygame
from pygame.locals import *

from data.scripts.config import *


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
        self.just_clicked_left = False
        self.right_click = False
        self.just_clicked_right = False

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

    def get_updates(self):
        self.interact = False
        self.down_press = False
        self.attempting_climb = False
        self.just_clicked_left = False
        self.just_clicked_right = False
        self.jump = False

        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pos = [self.mouse_pos[0], self.mouse_pos[1]]

        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            self.filter_quit_event(pressed_keys, event)
            self.handle_input(event)

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

    def handle_input(self, event):
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
            if event.button == 1:
                self.left_click = True
            elif event.button == 3:
                self.right_click = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                self.just_clicked_left = True
                self.left_click = False
            elif event.button == 3:
                self.just_clicked_right = True
                self.right_click = False
