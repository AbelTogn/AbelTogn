import pygame

def main():
    pygame.init()

    # Ajouter une icône
    #icon = pygame.image.load("icon.png")
    #pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((240,180))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
if __name__ == "__main__":
    main()