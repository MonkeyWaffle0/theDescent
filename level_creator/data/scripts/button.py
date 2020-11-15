import pygame

from data.scripts.config import WHITE, BLACK, RED, GREEN, BLUE, PURPLE, YELLOW
from level_creator.data.scripts.config import FONT, BLOCK, SPAWN, LEVEL_WINDOW
from level_creator.data.scripts.core_funcs import save_level, load_level


class Button:
    def __init__(self, game, x, y, color, text, width=20, height=20):
        self.game = game
        self.display = game.window.display
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.ghost_surface = pygame.Surface((width, height))
        self.ghost_surface.set_alpha(150)
        self.ghost_surface.fill(WHITE)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.active = True
        self.text = FONT.render(text, True, BLACK)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x - len(text) * 6, y + 8)

    def action(self):
        print("you didn't override this in the child class")

    def check_clicked(self):
        if self.mouse_is_on() and self.game.input.just_clicked_left:
            return self.action()

    def update(self):
        self.check_clicked()
        self.display.blit(self.text, self.text_rect)
        pygame.draw.rect(self.display, self.color, self.rect)
        if self.mouse_is_on():
            self.display.blit(self.ghost_surface, (self.x, self.y))

    def mouse_is_on(self):
        if self.get_rect().collidepoint(self.game.input.mouse_pos):
            return True
        return False

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class BorderButton(Button):
    def __init__(self, game, x, y, color=RED, text='border'):
        super().__init__(game, x, y, color, text)
        self.on = False

    def action(self):
        self.switch()
        if not self.on:
            return self.game.active_scene.delete_border()
        else:
            return self.game.active_scene.create_border()

    def switch(self):
        if self.on:
            self.on = False
        else:
            self.on = True


class SaveButton(Button):
    def __init__(self, game, x, y, color=YELLOW, text='save'):
        super().__init__(game, x, y, color, text)

    def action(self):
        print("SAVING...")
        name = input("Input the level name :\n")
        return save_level(self.game.active_scene, name)


class LoadButton(Button):
    def __init__(self, game, x, y, color=PURPLE, text='load'):
        super().__init__(game, x, y, color, text)

    def action(self):
        print("LOADING...")
        return load_level(self.game)


class BlockButton(Button):
    def __init__(self, game, x, y, block_type, text):
        super().__init__(game, x, y, block_type['color'], text)
        self.block_type = block_type

    def action(self):
        self.game.active_scene.current = self.block_type
