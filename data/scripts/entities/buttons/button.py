import pygame

from data.scripts.entities.base_entities import GameEntity

from data.scripts.config import RED


class Button(GameEntity):
    def __init__(self, game, entities, x, y, width, height, e_type='button'):
        super().__init__(game, entities, e_type, x, y, width, height)
        self.color = RED
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.active = True
        # TODO: a changer quand j'aurais ajouté des menus a scroller avec le controller
        self.controller_selected = True

    def action(self):
        print("you didn't override this in the child class")

    def check_clicked(self):
        if self.mouse_is_on() and self.game.input.just_clicked:
            return self.action()

    def check_controller_selected(self):
        # TODO: ajuster quand plusieurs boutons
        if self.game.input.A:
            return self.action()

    def disable_and_hide(self):
        self.active = False
        self.visible = False

    def enable_and_show(self):
        self.active = True
        self.visible = True

    def update(self):
        if self.active:
            if self.game.input.control_mode == 'keyboard':
                self.check_clicked()
            elif self.game.input.control_mode == 'controller':
                self.check_controller_selected()
        if self.visible:
            pygame.draw.rect(self.game.window.display, self.color, self.rect)
