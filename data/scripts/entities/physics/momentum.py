class Momentum:
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.jumping = False
        self.velocity = [0, 0]
        self.slow_down_speed = 2
        self.grav_accel = 3
        self.jump_force = 22
        self.long_jump_momentum = 5.5
        self.jump_timer = 0
        self.jump_max = 2
        self.jumps = self.jump_max
        self.jumping = False
        self.jump_direction = None
        self.speed = 10
        self.air_time = 0
        self.drop_through = 0

    def jump_handling(self):
        # Jump if input a jump and player can jump
        if self.game.input.jump and self.jumps > 0:
            self.jumping = True
            self.velocity[1] = -self.jump_force
            self.jumps -= 1
            if self.velocity[0] > 0:
                self.jump_direction = 'right'
            if self.velocity[0] < 0:
                self.jump_direction = 'left'

        # Increase jump timer if still pressing jump button in the air
        if self.jumping:
            if self.game.input.released_jump:
                self.jumping = False
            self.jump_timer += 1

        # Increase upward velocity if player keep jump button pressed
        if self.jumping and self.jumps < self.jump_max and self.jump_timer >= 4:
            self.velocity[1] -= self.long_jump_momentum / (self.jump_timer - 3)

        if self.jump_timer != 0 and self.game.input.released_jump:
            self.jump_timer = 0

    def gravity_handling(self):
        self.velocity[1] = min(self.velocity[1] + self.grav_accel, 15)

    def movement_handling(self):
        if self.air_time == 0 or not self.jump_direction:
            self.ground_movement()
        else:
            self.air_movement()
        self.progressive_slowdown()

    def ground_movement(self):
        if self.game.input.right and not self.game.input.left:
            self.velocity[0] = min(self.velocity[0] + self.speed, self.speed)
        if self.game.input.left and not self.game.input.right:
            self.velocity[0] = max(self.velocity[0] - self.speed, -self.speed)

    def air_movement(self):
        if self.jump_direction == 'right':
            if self.game.input.left:
                self.velocity[0] = max(self.velocity[0] - self.speed // 4, -self.speed)
            elif self.game.input.right:
                self.velocity[0] = min(self.velocity[0] + self.speed // 2, self.speed)
        elif self.jump_direction == 'left':
            if self.game.input.right:
                self.velocity[0] = min(self.velocity[0] + self.speed // 4, self.speed)
            elif self.game.input.left:
                self.velocity[0] = max(self.velocity[0] - self.speed // 2, -self.speed)

    def progressive_slowdown(self):
        if self.velocity[0] > 0 and not self.game.input.right:
            self.velocity[0] = max(self.velocity[0] - self.slow_down_speed, 0)
        elif self.velocity[0] < 0 and not self.game.input.left:
            self.velocity[0] = min(self.velocity[0] + self.slow_down_speed, 0)

    def land(self):
        self.velocity[1] = 0
        self.jumps = self.jump_max
        self.air_time = 0
        self.jump_direction = None

    def update(self):
        self.jump_handling()
        self.movement_handling()
        self.gravity_handling()
