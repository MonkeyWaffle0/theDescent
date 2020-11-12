from data.scripts.config import CAMERA_WINDOW, DISPLAY_SIZE


class Camera:
    def __init__(self, game):
        self.game = game
        self.true_scroll = [(self.game.entities.player.x - CAMERA_WINDOW[0] // 2) / 20,
                            (self.game.entities.player.y - CAMERA_WINDOW[1] // 2) / 20]
        self.scroll = self.true_scroll.copy()
        self.width = CAMERA_WINDOW[0]
        self.height = CAMERA_WINDOW[1]

    def follow_player(self):
        self.true_scroll[0] += (self.game.entities.player.x - self.true_scroll[0] - DISPLAY_SIZE[0] // 2) / 20
        self.true_scroll[1] += (self.game.entities.player.y - self.true_scroll[1] - DISPLAY_SIZE[1] // 2) / 20
        self.scroll[0] = int(self.true_scroll[0])
        self.scroll[1] = int(self.true_scroll[1])
