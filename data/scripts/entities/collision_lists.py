class CollisionLists:
    def __init__(self):
        self.reset()

    def reset(self):
        self.collision_tiles = []
        self.collision_ramps = []
        self.collision_platforms = []
        self.collision_water = []
