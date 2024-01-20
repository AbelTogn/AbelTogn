class Enemy:
    def __init__(self, screen_width: int, screen_height: int, size: int, speed: float, follow_player: bool, jump: bool, fly: bool, color: tuple, destroy: bool, gravity: float, player_y: float):
        if follow_player:
            self.x = 0
        else:
            self.x = screen_width
        if fly:
            self.y = screen_height - size
        else:
            self.y = screen_height - size - 10
        self.size = size
        self.speed = speed
        self.follow_player = follow_player
        self.color = color
        self.destroy = destroy
        self.jump = jump
        self.follow_player = follow_player
        self.y_speed = 0
        self.jump_strength = -10
        self.fly = fly

    def move(self, screen_width: int, screen_height: int, player_x: float, gravity: float, player_y: float):
        if self.follow_player:
            if player_x > self.x:
                self.x += self.speed
            elif player_x < self.x:
                self.x -= self.speed

        elif self.jump:
            if self.y == screen_height - self.size - 10:
                self.y_speed = self.jump_strength
            self.y_speed += gravity
            self.x -= self.speed
            self.y += self.y_speed

            if self.y > screen_height - self.size - 10:
                self.y = screen_height - self.size - 10
                self.y_speed = 0
            self.x -= self.speed

        elif self.fly:
            if self.x < player_x:
                self.x += self.speed
            else:
                self.x -= self.speed
            if self.y > player_y:
                self.y -= self.speed
            else:
                self.y += self.speed

        else:
            self.x -= self.speed

        if self.x + self.size < 0:
            self.x = screen_width
            self.y = screen_height - self.size - 10


class EnemyAI(Enemy):
    def __init__(self, screen_width: int, screen_height: int, size: int, speed: float, color: tuple, gravity: float, player_y: float, ai_behavior: str):
        super().__init__(screen_width, screen_height, size, speed, False, False, False, color, False, gravity, player_y)
        self.ai_behavior = ai_behavior

    def move(self, screen_width: int, screen_height: int, player_x: float, gravity: float, player_y: float):
        if self.ai_behavior == "chase":
            if player_x > self.x:
                self.x += self.speed
            elif player_x < self.x:
                self.x -= self.speed

        elif self.ai_behavior == "random":
            # Implement your custom random movement logic here
            pass

        # Add more AI behaviors as needed

        # Apply gravity
        self.y_speed += gravity
        self.y += self.y_speed

        if self.y > screen_height - self.size - 10:
            self.y = screen_height - self.size - 10
            self.y_speed = 0
            self.x -= self.speed

        if self.x + self.size < 0:
            self.x = screen_width
            self.y = screen_height - self.size - 10
