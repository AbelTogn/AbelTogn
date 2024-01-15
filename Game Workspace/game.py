import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

    circle_x = 255
    circle_y = 255


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    circle_x += 10
                elif event.key == pygame.K_LEFT:
                    circle_x -= 10
                elif event.key == pygame.K_UP:
                    circle_y -= 10
                elif event.key == pygame.K_DOWN:
                    circle_y += 10

        screen.fill((255, 255, 255))

        pygame.draw.circle(screen, (255,0,0), (circle_x, circle_y),100)
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
