import pygame
import sys

class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, width, height):
        super().__init__()
        self.set_image(image_path, width, height)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def set_image(self, image_path, width, height):
        original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(original_image, (width, height))

def main():
    pygame.init()

    # Define the screen
    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

    x, y = 255, 255                     # Initial position
    width, height = 50, 50              # Initial width and height
    image_path = "images/sprite.png"    # Sprite image

    # Define the sprite
    my_sprite = MySprite(x, y, image_path, width, height)

    # Add sprite to all sprites
    all_sprites = pygame.sprite.Group(my_sprite)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.VIDEORESIZE:
                # Adjust the window size
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x += 10
                    my_sprite.rect.x = x
                elif event.key == pygame.K_LEFT:
                    x -= 10
                    my_sprite.rect.x = x
                
        all_sprites.update()

        screen.fill((255, 255, 255))

        all_sprites.draw(screen)
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
