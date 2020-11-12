class CollisionManager:
    def __init__(self, game, entity):
        self.game = game
        self.entity = entity
        self.collision_type = {'right': False, 'left': False, 'top': False, 'bottom': False}

    def reset(self):
        self.collision_type = {'right': False, 'left': False, 'top': False, 'bottom': False}

    @staticmethod
    def collision_test(object_1, object_list):
        return [obj for obj in object_list if obj.colliderect(object_1)]

    def handle_x_movement(self, movement, platforms):
        self.entity.x += movement[0]
        self.entity.rect.x = int(self.entity.x)
        block_hit_list = self.collision_test(self.entity.rect, platforms)

        for block in block_hit_list:
            if movement[0] > 0:
                self.entity.rect.right = block.left
                self.collision_type['right'] = True
            elif movement[0] < 0:
                self.entity.rect.left = block.right
                self.collision_type['left'] = True
            self.entity.x = self.entity.rect.x

    def handle_y_movement(self, movement, platforms):
        self.entity.y += movement[1]
        self.entity.rect.y = int(self.entity.y)
        block_hit_list = self.collision_test(self.entity.rect, platforms)

        for block in block_hit_list:
            if movement[1] > 0:
                self.entity.rect.bottom = block.top
                self.collision_type['bottom'] = True
            elif movement[1] < 0:
                self.entity.rect.top = block.bottom
                self.collision_type['top'] = True
            self.entity.change_y = 0
            self.entity.y = self.entity.rect.y

    def process_collisions(self, movement):
        self.reset()
        self.handle_x_movement(movement, self.game.entities.collision_blocks)
        self.handle_y_movement(movement, self.game.entities.collision_blocks)
