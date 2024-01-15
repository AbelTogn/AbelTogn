import pygame
import sys

class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

    x, y = 255, 255

    image_path = "images/sprite.png"

    my_sprite = MySprite(x,y,image_path)
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

        screen.fill((255, 255, 255))

        all_sprites.update()

        all_sprites.draw(screen)
        pygame.draw.circle(screen, (255,0,0), (x, y),100)
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
