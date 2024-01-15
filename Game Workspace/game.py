import pygame
import sys

class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, width, height):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def set_height(self, height):
        self.height = height
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

    x, y = 255, 255
    width, height = 50, 50  # Initial width and height

    image_path = "images/sprite.png"

    my_sprite = MySprite(x, y, image_path, width, height)
    all_sprites = pygame.sprite.Group(my_sprite)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x += 10
                elif event.key == pygame.K_LEFT:
                    x -= 10
                elif event.key == pygame.K_UP:
                    y -= 10
                elif event.key == pygame.K_DOWN:
                    y += 10
                elif event.key == pygame.K_w:
                    my_sprite.set_width(my_sprite.width + 10)
                elif event.key == pygame.K_h:
                    my_sprite.set_height(my_sprite.height + 10)

        screen.fill((255, 255, 255))

        all_sprites.update()

        all_sprites.draw(screen)
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
