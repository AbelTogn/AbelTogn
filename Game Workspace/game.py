import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario-like Drawing and Jumping Game")

# Couleurs
white = (255, 255, 255)
blue = (0, 0, 255)

# Personnage
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_y_speed = 0
gravity = 1
jump_strength = -15
on_ground = True

# Couleur du crayon
pen_color = (0, 0, 0)
drawing = False
draw_radius = 5

# Boucle principale
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Gestion des événements de dessin
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            pygame.draw.circle(screen, pen_color, event.pos, draw_radius)

    keys = pygame.key.get_pressed()

    # Déplacement du personnage
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

    # Saut du personnage
    if keys[pygame.K_SPACE] and on_ground:
        player_y_speed = jump_strength
        on_ground = False

    # Appliquer la gravité
    player_y_speed += gravity
    player_y += player_y_speed

    # Vérifier si le personnage touche le sol
    if player_y > screen_height - player_size - 10:
        player_y = screen_height - player_size - 10
        player_y_speed = 0
        on_ground = True

    # Effacement de l'écran
    screen.fill(white)

    # Dessiner le personnage
    pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Réguler la vitesse de la boucle
    clock.tick(60)
