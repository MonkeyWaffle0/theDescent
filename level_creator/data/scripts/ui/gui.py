class GUI:
    def __init__(self, game):
        self.game = game
        self.inventory_target_loc = 0
        self.inventory_loc = 0

    def render_overlay(self):
        pass

    def update(self):
        self.render_overlay()
