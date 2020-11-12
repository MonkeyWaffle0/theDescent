from data.scripts.core_funcs import *
from data.scripts.ui.camera import Camera


class Scene:
    def __init__(self, game):
        self.game = game
        self.display = game.window.display
        self.next = self
        self.game.entities.create_player()
        self.camera = Camera(game)

    def handle_game_frame(self):
        self.game.input.get_updates()
        self.display.fill(WHITE)
        self.camera.follow_player()
        self.update()
        self.game.entities.update()

        self.game.active_scene = self.game.active_scene.next

    def switch_to(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to(None)

    def update(self):
        print("You didn't override this in the child class.")
