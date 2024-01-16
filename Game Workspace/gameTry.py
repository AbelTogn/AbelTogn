import pygame
import sys

pygame.init()

# Paramètres de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario-like Movement")

# Couleurs
white = (255, 255, 255)

# Personnage
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height // 2 - player_size // 2
player_speed = 5

# Boucle principale
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Déplacement du personnage
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Limitation de la position du joueur à l'écran
    player_x = max(0, min(screen_width - player_size, player_x))
    player_y = max(0, min(screen_height - player_size, player_y))

    # Effacement de l'écran
    screen.fill(white)

    # Dessiner le personnage
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_size, player_size))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Réguler la vitesse de la boucle
    clock.tick(60)
