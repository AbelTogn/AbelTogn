import pygame

def main():
    pygame.init()

    # Ajouter une icône
    # icon = pygame.image.load("icon.png")
    # pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((500,500))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_LEFT:
                    pygame.draw.circle(screen, (255,0,0), (255,255), 100)

        screen.fill((255,255,255))

if __name__ == "__main__":
    main()