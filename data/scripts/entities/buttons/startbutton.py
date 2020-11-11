from data.scripts.entities.buttons.button import Button
from data.scripts.scenes.game_scene import GameScene


class StartButton(Button):
    def __init__(self, game, entities, x, y, width, height):
        super().__init__(game, entities, x, y, width, height)

    def action(self):
        self.game.entities.entities.remove(self)
        self.game.active_scene.switch_to(GameScene(self.game))
