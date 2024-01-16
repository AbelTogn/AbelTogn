import pygame
import sys

def main():
    # Initialisation de Pygame
    pygame.init()

    # Paramètres de l'écran
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Mario-like Drawing and Jumping Game")

    # Couleurs
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    # Valeurs de départ
    points = 0
    coins = 0

    # Personnage
    player_size = 50
    player_x = screen_width // 2 - player_size // 2
    player_y = screen_height - player_size - 10
    player_y_speed = 0
    gravity = 1
    jump_strength = -15
    on_ground = True
    player_lives = 3

    # Ennemi
    enemy_size = 50
    enemy_x = screen_width
    enemy_y = screen_height - enemy_size - 10
    enemy_speed = 5

    # Couleur du crayon
    pen_color = (0, 0, 0)
    drawing = False
    draw_radius = 5

    # Police pour le texte
    font = pygame.font.Font(None, 36)

    # Couleur du texte
    black = (0, 0, 0)

    # Durée de l'invincibilité en frames (60 frames par seconde)
    invincibility_duration = 60
    invincibility_counter = 0

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
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and on_ground:
            player_y_speed = jump_strength
            on_ground = False

        # Déplacement de l'ennemi
        enemy_x -= enemy_speed
        if enemy_x + enemy_size < 0:
            # Réinitialisation de la position de l'ennemi
            enemy_x = screen_width
            enemy_y = screen_height - enemy_size - 10

        # Appliquer la gravité
        player_y_speed += gravity
        player_y += player_y_speed

        # Gestion de l'invincibilité
        if invincibility_counter > 0:
            invincibility_counter -= 1

        # Vérifier si le personnage touche le sol
        if player_y > screen_height - player_size - 10:
            player_y = screen_height - player_size - 10
            player_y_speed = 0
            on_ground = True

        # Vérifier la collision avec l'ennemi pendant la période d'invincibilité
        if (
            invincibility_counter == 0
            and player_x < enemy_x + enemy_size 
            and player_x + player_size > enemy_x
            and player_y < enemy_y + enemy_size
            and player_y + player_size > enemy_y
        ):
            # Si le joueur est au-dessus de l'ennemi et en train de descendre
            if player_y + player_size < enemy_y + enemy_size and player_y_speed > 0:
                # Réinitialisation de la position de l'ennemi
                enemy_x = screen_width
                enemy_y = screen_height - enemy_size - 10
                points += 10

                # Vérifier si le nombre de points est un multiple de 100
                if points % 100 == 0:
                    player_lives += 1
            else:
                # Réinitialisation de la position du personnage
                player_x = screen_width // 2 - player_size // 2
                player_y = screen_height - player_size - 10
                player_lives -= 1
                invincibility_counter = invincibility_duration

        # Effacement de l'écran
        screen.fill(white)

        # Dessiner le personnage
        pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))

        # Dessiner l'ennemi
        pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_size, enemy_size))

        # Dessiner le nombre de vies
        lives_text = font.render(f"Lives: {player_lives}", True, black)
        screen.blit(lives_text, (10, 10))

        # Dessiner et activer le game over
        if player_lives <= 0:
            game_over_text = font.render("Game Over", True, black)
            screen.blit(game_over_text, (screen_width // 2 - 70, screen_height // 2))
            enemy_speed = 0
            enemy_x = screen_width

        # Dessiner le nombre de points
        points_text = font.render(f"Points: {points}", True, black)
        screen.blit(points_text, (10, 40))

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Réguler la vitesse de la boucle
        clock.tick(60)

if __name__ == "__main__":
    main()
