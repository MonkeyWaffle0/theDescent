from data.scripts.scenes.scene import Scene, WHITE
from data.scripts.ui.camera import Camera


class GameScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.display = game.window.display
        self.level_dic = {'blocks': [],
                          'spawn': [],
                          'exit': []}
        self.level_handler = self.game.level_handler
        self.game.entities.create_player()
        self.camera_mode = True
        self.camera = Camera(game)
        self.load_level()

    def update(self):
        self.camera.follow_player()
        self.display.fill(WHITE)

    def load_level(self):
        self.level_dic = self.level_handler.load_level('level1')
