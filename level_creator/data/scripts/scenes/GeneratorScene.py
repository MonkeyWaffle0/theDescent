from math import floor

import pygame

from level_creator.data.scripts.block import Block
from level_creator.data.scripts.button import BorderButton, SaveButton, LoadButton, BlockButton
from level_creator.data.scripts.config import LEVEL_WINDOW, GRID_SIZE, WHITE, BLACK, NEXT_LINE, BLOCK, EXIT, SPAWN, \
    SPIKE_UP, SPIKE_DOWN, SPIKE_LEFT, SPIKE_RIGHT
from level_creator.data.scripts.core_funcs import mouse_over
from level_creator.data.scripts.scenes.scene import Scene


class GeneratorScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.level_list = []

        block_list = []
        for i in range(LEVEL_WINDOW[0] // GRID_SIZE):
            x = i * GRID_SIZE
            block_list.append(Block(self.game, x, 0, BLOCK))
            block_list.append(Block(self.game, x, LEVEL_WINDOW[1] - GRID_SIZE, BLOCK))

        for i in range((LEVEL_WINDOW[1] // GRID_SIZE) - 2):
            y = i * GRID_SIZE
            block_list.append(Block(self.game, 0, y + GRID_SIZE, BLOCK))
            block_list.append(Block(self.game, LEVEL_WINDOW[0] - GRID_SIZE, y + GRID_SIZE, BLOCK))

        self.border_blocks = block_list
        self.ghost_surface = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.ghost_surface.set_alpha(150)
        self.ghost_surface.fill(WHITE)

        self.current = BLOCK

        self.save_button = SaveButton(game, 50, LEVEL_WINDOW[1] + 10)
        self.load_button = LoadButton(game, 50, LEVEL_WINDOW[1] + 40)
        self.border_button = BorderButton(game, 200, LEVEL_WINDOW[1] + 10)
        self.block_button = BlockButton(game, 200, LEVEL_WINDOW[1] + 40, BLOCK, 'Block')
        self.spawn_button = BlockButton(game, 300, LEVEL_WINDOW[1] + 10, SPAWN, 'Spawn')
        self.exit_button = BlockButton(game, 300, LEVEL_WINDOW[1] + 40, EXIT, 'Exit')
        self.spike_up_button = BlockButton(game, 450, LEVEL_WINDOW[1] + 10, SPIKE_UP, 'Spike up')
        self.spike_down_button = BlockButton(game, 450, LEVEL_WINDOW[1] + 40, SPIKE_DOWN, 'Spike down')
        self.spike_left_button = BlockButton(game, 600, LEVEL_WINDOW[1] + 10, SPIKE_LEFT, 'Spike left')
        self.spike_right_button = BlockButton(game, 600, LEVEL_WINDOW[1] + 40, SPIKE_RIGHT, 'Spike right')
        self.buttons = [self.border_button, self.save_button, self.load_button, self.block_button, self.spawn_button,
                        self.exit_button, self.spike_up_button, self.spike_down_button, self.spike_left_button,
                        self.spike_right_button]

    def update(self):
        self.display.fill(WHITE)
        pygame.draw.line(self.display, BLACK, (0, LEVEL_WINDOW[1]), (LEVEL_WINDOW[0], LEVEL_WINDOW[1]))
        grid_pos = self.get_grid_pos()
        if mouse_over(pygame.Rect(0, 0, LEVEL_WINDOW[0], LEVEL_WINDOW[1])):
            self.draw_ghost_block(grid_pos)
            if self.game.input.left_click:
                self.place_block(grid_pos)

            if self.game.input.right_click:
                self.remove_block()

        self.update_entities()
        for button in self.buttons:
            button.update()

    def get_grid_pos(self):
        return (floor(self.game.input.mouse_pos[0] / GRID_SIZE) * GRID_SIZE,
                floor(self.game.input.mouse_pos[1] / GRID_SIZE) * GRID_SIZE)

    def draw_ghost_block(self, grid_pos):
        pygame.draw.rect(self.display, self.current['color'],
                         pygame.Rect(grid_pos[0],
                                     grid_pos[1],
                                     GRID_SIZE,
                                     GRID_SIZE))
        self.display.blit(self.ghost_surface, (grid_pos[0], grid_pos[1]))

    def place_block(self, grid_pos):
        if not self.block_is_here(grid_pos):
            if self.current == EXIT or self.current == SPAWN:
                self.move_block(self.current)
            self.level_list.append(Block(self.game, grid_pos[0], grid_pos[1], self.current))

    def move_block(self, block_type):
        for block in self.level_list:
            if block.type == block_type:
                self.level_list.remove(block)
                break

    def block_is_here(self, point):
        offset_point = (point[0] + 1, point[1] + 1)  # Offset by one pixel otherwise the collision check fuck up
        for block in self.level_list:
            if block.get_rect().collidepoint(offset_point):
                return True
        return False

    def remove_block(self):
        for block in self.level_list:
            if mouse_over(block):
                self.level_list.remove(block)

    def update_entities(self):
        for block in self.level_list:
            block.update()

    def create_border(self):
        for border_block in self.border_blocks:
            block_here = False
            for block in self.level_list:
                if block.get_rect().collidepoint((border_block.x + 1, border_block.y + 1)):
                    block_here = True
            if not block_here:
                self.level_list.append(border_block)

    def delete_border(self):
        block_list = list(self.level_list)
        for block in block_list:
            for border_block in self.border_blocks:
                if block.x == border_block.x and block.y == border_block.y:
                    self.level_list.remove(block)
                    break

    def convert_to_level(self, string):
        x = 0
        y = 0
        level_list = []
        for char in string:
            if char == BLOCK['letter']:
                level_list.append(Block(self.game, x * GRID_SIZE, y * GRID_SIZE, BLOCK))
            x += 1
            if char == NEXT_LINE:
                y += 1
                x = 0
        self.level_list = level_list

    def check_double(self):
        for block in self.level_list:
            x = 1
            for block2 in self.level_list:
                if block.x == block2.x and block.y == block2.y and x > 1:
                    print(x)
                    x += 1
