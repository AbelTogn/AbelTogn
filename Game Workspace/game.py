
import pygame
import sys
from random import randint
from classes import *
from functions import *

def main():
    # Initialization of Pygame
    pygame.init()

    # Screen parameters
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Platformer game")

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    purple = (255, 0, 255)

    # Starting points
    points = 0

    # Player
    player_size = 50
    player_x = screen_width // 2 - player_size // 2
    player_y = screen_height - player_size - 10
    player_y_speed = 0
    gravity = 1
    jump_strength = -15
    on_ground = True
    player_lives = 3

    # Enemy sizes
    enemy_low_size = 25
    enemy_normal_size = 50
    enemy_high_size = 100

    # Enemy speeds
    enemy_very_low_speed = 1.5
    enemy_low_speed = 2
    enemy_normal_speed = 5
    enemy_high_speed = 10
    enemy_very_high_speed = 15

    # Enemies
    all_enemies = []
    enemy_walk = Enemy(screen_width, screen_height, enemy_normal_size, enemy_normal_speed, False, False, False, red, False, gravity, player_y)
    all_enemies.append(enemy_walk)
    enemy_follow = Enemy(screen_width, screen_height, enemy_low_size, enemy_very_low_speed, True, False, False, green, False, gravity, player_y)
    all_enemies.append(enemy_follow)
    enemy_jump = Enemy(screen_width, screen_height, enemy_low_size, enemy_low_speed, False, True, False, black, False, gravity, player_y)
    all_enemies.append(enemy_jump)
    enemy_fly = Enemy(screen_width, screen_height, enemy_low_size, enemy_low_speed, True, False, False, purple, False, gravity, 0)
    all_enemies.append(enemy_fly)

    # New AI enemy with chase behavior
    enemy_ai_chase = EnemyAI(screen_width, screen_height, enemy_low_size, enemy_low_speed, blue, gravity, player_y, "chase")
    all_enemies.append(enemy_ai_chase)

    # Pen color
    pen_color = (0, 0, 0)
    drawing = False
    draw_radius = 5

    # Font for text
    font = pygame.font.Font(None, 36)

    # Invincibility settings
    invincibility_duration = 60
    invincibility_counter = 0

    # Main loop
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Drawing events
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawing = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                drawing = False
            elif event.type == pygame.MOUSEMOTION and drawing:
                pygame.draw.circle(screen, pen_color, event.pos, draw_radius)

        keys = pygame.key.get_pressed()

        # Player movement
        if (keys[pygame.K_LEFT] or keys[pygame.K_q]) and player_x > 0:
            player_x -= 5
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < screen_width - player_size:
            player_x += 5

        # Player jump
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_z]) and on_ground:
            player_y_speed = jump_strength
            on_ground = False

        # Move enemies
        for enemy in all_enemies:
            enemy.move(screen_width, screen_height, player_x, gravity, player_y)

        # Apply gravity to player
        player_y_speed += gravity
        player_y += player_y_speed

        # Invincibility handling
        if invincibility_counter > 0:
            invincibility_counter -= 1

        # Check if player touches the ground
        if player_y > screen_height - player_size - 10:
            player_y = screen_height - player_size - 10
            player_y_speed = 0
            on_ground = True

        # Check collision with enemy during invincibility period
        for enemy in all_enemies:
            if (
                not enemy.destroy
                and invincibility_counter == 0
                and player_x < enemy.x + enemy.size
                and player_x + player_size > enemy.x
                and player_y < enemy.y + enemy.size
                and player_y + player_size > enemy.y
            ):
                # If player is above the enemy and descending
                if player_y + player_size < enemy.y + enemy.size and player_y_speed > 0:
                    # Reset enemy position
                    if enemy.follow_player:
                        enemy.x = 0
                    else:
                        enemy.x = screen_width
                    enemy.y = screen_height - enemy.size - 10
                    points += 10

                    # Check if points are a multiple of 100
                    if points % 100 == 0:
                        player_lives += 1
                else:
                    player_lives -= 1
                    invincibility_counter = invincibility_duration

        # Clear the screen
        screen.fill(white)

        # Draw the player
        pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))

        # Draw enemies if not destroyed
        for enemy in all_enemies:
            if not enemy.destroy:
                pygame.draw.rect(screen, enemy.color, (enemy.x, enemy.y, enemy.size, enemy.size))

        # Draw lives count
        lives_text = font.render(f"Lives: {player_lives}", True, black)
        screen.blit(lives_text, (10, 10))

        # Game over handling
        if player_lives <= 0:
            game_over_text = font.render("Game Over", True, black)
            screen.blit(game_over_text, (screen_width // 2 - 70, screen_height // 2))
            for enemy in all_enemies:
                enemy.speed = 0
                enemy.x = screen_width
            enemy_follow.x = -enemy.size

            # Draw retry button
            retry_button = pygame.Rect(screen_width // 2 - 50, screen_height // 2 + 50, 100, 50)
            pygame.draw.rect(screen, red, retry_button)

            retry_text = font.render("Retry", True, white)

            # Center the text in the button
            text_rect = retry_text.get_rect(center=retry_button.center)
            screen.blit(retry_text, text_rect.topleft)

            # Mouse events
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            # Check if retry button clicked
            if retry_button.collidepoint(mouse_pos) and mouse_click[0]:
                # Reset game values
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

        # Draw points count
        points_text = font.render(f"Points: {points}", True, black)
        screen.blit(points_text, (10, 40))

        # Update display
        pygame.display.flip()

        # Control loop speed
        clock.tick(60)

if __name__ == "__main__":
    main()
