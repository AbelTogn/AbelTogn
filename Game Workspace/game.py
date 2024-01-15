import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 500))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pygame.draw.circle(screen, (255, 0, 0), (255, 255), 100)
                    pygame.display.flip()

        screen.fill((255, 255, 255))
        pygame.display.flip()

if __name__ == "__main__":
    main()
