import pygame
import math
from pygame.locals import *
# pygame setup
pygame.init()
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((1080, 720))
display = pygame.Surface((1080,720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

pygame.mixer.music.load("assets\music\PokedexTheme.ogg")
pygame.mixer.music.play(-1)

size = (1080,720)
berkovich = pygame.image.load("berkovich.jpeg")
berkovich = pygame.transform.scale(berkovich, (200,200))

bg = pygame.image.load("stardustBg.png").convert()
fg = pygame.image.load("stardustFloor.png").convert_alpha()
bg = pygame.transform.scale(bg, size)
fg = pygame.transform.scale(fg, size)
bg_width = bg.get_width()
bg_rect = bg.get_rect()
fg_width = fg.get_width()
fg_rect = fg.get_rect()

scroll = 0
tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
  #draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll
        pygame.draw.rect(screen, (0, 0, 0), bg_rect, 1)

  #scroll background
    scroll -= 25

  #reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    screen.blit(berkovich, player_pos)
    
    for i in range(0, tiles):
        screen.blit(fg, (i * fg_width + scroll, 0))
        fg_rect.x = i * fg_width + scroll
        pygame.draw.rect(screen, (0, 0, 0), fg_rect, 1)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
 

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()