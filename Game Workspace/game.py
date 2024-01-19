#1
import pygame
import sys
import time
from random import  randint

class Enemy:
    def __init__(self, screen_width: int, screen_height: int, size: int, speed: float, follow_player: bool, jump: bool, fly: bool, color: tuple, destroy: bool, gravity: float, player_y: float):
        if follow_player:
            self.x = 0
        else:
            self.x = screen_width
        if fly:
            self.y = screen_height - size
        else:
            self.y = screen_height - size - 10
        self.size = size
        self.speed = speed
        self.follow_player = follow_player
        self.color = color
        self.destroy = destroy
        self.jump = jump
        self.follow_player = follow_player
        self.y_speed = 0
        self.jump_strength = -10
        self.fly = fly

    def move(self, screen_width: int, screen_height: int, player_x: float, gravity: float, player_y: float):
        if self.follow_player:
            if player_x > self.x:
                self.x += self.speed
            elif player_x < self.x:
                self.x -= self.speed

        elif self.jump:
            if self.y == screen_height - self.size - 10:
                self.y_speed = self.jump_strength
            self.y_speed += gravity
            self.x -= self.speed
            self.y += self.y_speed

            if self.y > screen_height - self.size - 10:
                self.y = screen_height - self.size - 10
                self.y_speed = 0
            self.x -= self.speed

        elif self.fly:
            if self.x < player_x:
                self.x += self.speed
            else:
                self.x -= self.speed
            if self.y > player_y: 
                self.y -= self.speed
            else:
                self.y += self.speed

        else:
            self.x -= self.speed

        if self.x + self.size < 0:
            self.x = screen_width
            self.y = screen_height - self.size - 10

def main():
    # Initialisation de Pygame
    pygame.init()

    # Paramètres de l'écran
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Platformer game")

    # Couleurs
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    purple = (255, 0, 255)

    # Points de départ
    points = 0

    # Personnage
    player_size = 50
    player_x = screen_width // 2 - player_size // 2
    player_y = screen_height - player_size - 10
    player_y_speed = 0
    gravity = 1
    jump_strength = -15
    on_ground = True
    player_lives = 3

    # Taille des ennemis
    enemy_low_size = 25
    enemy_normal_size = 50
    enemy_high_size = 100

    # Vitesse des ennemis
    enemy_very_low_speed = 1.5
    enemy_low_speed = 2
    enemy_normal_speed = 5
    enemy_high_speed = 10
    enemy_very_high_speed = 15

    # Ennemis
    all_enemies = []
    enemy_walk = Enemy(screen_width, screen_height, enemy_normal_size, enemy_normal_speed, False, False, False, red, False, gravity, player_y)
    all_enemies.append(enemy_walk)
    enemy_follow = Enemy(screen_width, screen_height, enemy_low_size, enemy_very_low_speed, True, False, False, green, False, gravity, player_y)
    all_enemies.append(enemy_follow)
    enemy_jump = Enemy(screen_width, screen_height, enemy_low_size, enemy_low_speed, False, True, False, black, False, gravity, player_y)
    all_enemies.append(enemy_jump)
    enemy_fly = Enemy(screen_width, screen_height, enemy_low_size, enemy_low_speed, True, False, False, purple, False, gravity, 0)
    all_enemies.append(enemy_fly)

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
        if (keys[pygame.K_LEFT] or keys[pygame.K_q]) and player_x > 0:
            player_x -= 5
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < screen_width - player_size:
            player_x += 5

        # Saut du personnage
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_z]) and on_ground:
            player_y_speed = jump_strength
            on_ground = False

        # Déplacement des ennemis
        for enemy in all_enemies:
            enemy.move(screen_width, screen_height, player_x, gravity, player_y)

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
        for enemy in all_enemies:
            if (
                not enemy.destroy
                and invincibility_counter == 0
                and player_x < enemy.x + enemy.size
                and player_x + player_size > enemy.x
                and player_y < enemy.y + enemy.size
                and player_y + player_size > enemy.y
            ):
                # Si le joueur est au-dessus de l'ennemi et en train de descendre
                if player_y + player_size < enemy.y + enemy.size and player_y_speed > 0:
                    # Réinitialisation de la position de l'ennemi
                    if enemy.follow_player:
                        enemy.x = 0
                    else:
                        enemy.x = screen_width
                    enemy.y = screen_height - enemy.size - 10
                    points += 10

                    # Vérifier si le nombre de points est un multiple de 100
                    if points % 100 == 0:
                        player_lives += 1
                else:
                    player_lives -= 1
                    invincibility_counter = invincibility_duration

        # Effacement de l'écran
        screen.fill(white)

        # Dessiner le personnage
        pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))

        # Dessiner les ennemis s'ils ne sont pas détruits
        for enemy in all_enemies:
            if not enemy.destroy:
                pygame.draw.rect(screen, enemy.color, (enemy.x, enemy.y, enemy.size, enemy.size))

        # Dessiner le nombre de vies
        lives_text = font.render(f"Lives: {player_lives}", True, black)
        screen.blit(lives_text, (10, 10))

        if player_lives <= 0:
            # Dessiner et activer le game over
            game_over_text = font.render("Game Over", True, black)
            screen.blit(game_over_text, (screen_width // 2 - 70, screen_height // 2))
            for enemy in all_enemies:
                enemy.speed = 0
                enemy.x = screen_width
            enemy_follow.x = -enemy.size
                    
            # Dessiner le bouton retry
            retry_button = pygame.Rect(screen_width // 2 - 50, screen_height // 2 + 50, 100, 50)
            pygame.draw.rect(screen, red, retry_button)
            
            retry_text = font.render("Retry", True, white)
            
            # Calculer la position du texte pour le centrer dans le bouton
            text_rect = retry_text.get_rect(center=retry_button.center)
            screen.blit(retry_text, text_rect.topleft)

            # Gestion des événements de la souris
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            # Vérifier si le bouton retry a été cliqué
            if retry_button.collidepoint(mouse_pos) and mouse_click[0]:
                # Réinitialiser les valeurs du jeu
                player_lives = 3
                points = 0
                player_x = screen_width // 2 - player_size // 2
                player_y = screen_height - player_size - 10
                enemy_walk.x = screen_width
                enemy_follow.x = screen_width
                enemy_fly.x = 0
                enemy_jump.x = 0
                on_ground = True
                for enemy in all_enemies:
                    if enemy.follow_player:
                        enemy.speed = enemy_very_low_speed
                    elif enemy.jump:
                        enemy.speed = enemy_low_speed
                    elif not enemy.follow_player and not enemy.jump:
                        enemy.speed = enemy_normal_speed

        # Dessiner le nombre de points
        points_text = font.render(f"Points: {points}", True, black)
        screen.blit(points_text, (10, 40))

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Réguler la vitesse de la boucle
        clock.tick(60)

if __name__ == "__main__":
    main()
