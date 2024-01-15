import pygame
import sys

class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, width, height):
        super().__init__()
        self.set_image(image_path, width, height)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity_x = 0  # Initial horizontal velocity
        self.velocity_y = 0  # Initial vertical velocity
        self.gravity = 1  # Gravity value

    def set_image(self, image_path, width, height):
        original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(original_image, (width, height))

    def jump(self):
        # Only allow jumping if the sprite is on the ground (you can modify this condition)
        if self.rect.y == 255:
            self.velocity_y = -15  # Set a negative value to go upwards

    def update(self):
        self.velocity_y += self.gravity  # Apply gravity
        self.rect.y += self.velocity_y

        # Limit the vertical speed (optional)
        if self.velocity_y > 10:
            self.velocity_y = 10

        # Check if the sprite has reached the ground
        if self.rect.y >= 255:
            self.rect.y = 255  # Reset the position to the ground
            self.velocity_y = 0  # Stop the vertical movement

        # Update horizontal position based on velocity
        self.rect.x += self.velocity_x

def main():
    pygame.init()

    # Define window
    screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
    # Define the name of the window
    pygame.display.set_caption('Game')

    x, y = 0,0                          # Initial position
    width, height = 50, 50              # Initial width and height
    image_path = "images/sprite.png"    # Sprite image

    # Define the sprite
    my_sprite = MySprite(x, y, image_path, width, height)   

    # Add sprite to all sprites
    all_sprites = pygame.sprite.Group(my_sprite)

    running = True
    while running:

        for event in pygame.event.get():
            # Define Quit 
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.VIDEORESIZE:
                # Adjust the window size
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            # Handle continuous movement when a key is held down
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    my_sprite.velocity_x = 1.25  # Adjust the speed as needed
                elif event.key == pygame.K_LEFT:
                    my_sprite.velocity_x = -1.25  # Adjust the speed as needed
                elif event.key == pygame.K_SPACE:
                    my_sprite.jump()

            # Stop movement when a key is released
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    my_sprite.velocity_x = 0

        all_sprites.update()

        screen.fill((255, 255, 255))

        all_sprites.draw(screen)
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
