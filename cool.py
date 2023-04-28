import time
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print('initiating game')
time.sleep(1)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                    running = False

            if event.key == K_DOWN:
                surf = pygame.Surface((50, 50))
                surf.fill((0, 0, 0))
                rect = surf.get_rect()
                screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                pygame.display.flip()


    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()
pygame.quit()