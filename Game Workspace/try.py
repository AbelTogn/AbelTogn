import time
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game AI with Python")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    class NPC:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def draw(self, screen):
            pygame.draw.rect(screen, (255, 0, 0), (self.x * 50, self.y * 50, 50, 50))

    class Player:
        def __init__(self, x, y):
            self.x = x
            self.y =    y

        def draw(self, screen):
            pygame.draw.rect(screen, (0, 255, 0), (self.x * 50, self.y * 50, 50, 50))

    player = Player(1, 1)    

    npc = NPC(3, 3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    npc.draw(screen)


    pygame.display.flip()