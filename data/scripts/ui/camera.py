from data.scripts.config import CAMERA_WINDOW


class Camera:
    def __init__(self, game):
        self.game = game
        self.x = self.game.entities.player.x - CAMERA_WINDOW[0] // 2
        self.y = self.game.entities.player.y - CAMERA_WINDOW[1] // 2
        self.width = CAMERA_WINDOW[0]
        self.height = CAMERA_WINDOW[1]

    def follow_player(self):
        self.x += self.game.entities.player.x - self.x
        self.y += self.game.entities.player.y - self.y
