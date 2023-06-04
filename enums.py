import pygame
import math

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

start = pygame.time.get_ticks()

bgSpeed = 0
floorSpeed = 0

bg_width = 1920
tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 2