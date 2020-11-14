class Room:
    def __init__(self, game, shape, doors, x, y):
        self.game = game
        self.shape = shape
        self.width = shape['width']
        self.height = shape['height']
        self.x = x
        self.y = y
        self.doors = doors