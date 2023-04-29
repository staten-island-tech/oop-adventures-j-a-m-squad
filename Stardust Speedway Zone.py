#Setup Python
import pygame
import math
from pygame.locals import *
#Start Pygame
pygame.init()
#Screen Width and Height Variable (Makes it super easy if we ever want to change it)
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
#Setup Game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dead = False
dt = 0
#Setup the players position on the screen
player_pos = pygame.Vector2(screen.get_width() / 2.4, screen.get_height() / 2.1)
#Load and play music
pygame.mixer.music.load("assets\music\Stardust Speedway Bad Future.ogg")
pygame.mixer.music.play(-1)
#Load Sound Effects
sonicJump = pygame.mixer.Sound("assets\sounds\sonicJump.ogg")
sonicJumpWacky = pygame.mixer.Sound("assets\sounds\I'm outta here.ogg")
#Loads the Player and Enemy
player = pygame.image.load("assets\images\characters\egghead.jpeg")
player = pygame.transform.scale(player, (250,250))
enemy = pygame.image.load("assets\images\characters\Lighting_McQueen.png")
enemy = pygame.transform.scale(enemy, (250,250))
#Loads our Background and Foreground
#bg = pygame.image.load("assets\images\stages\Stardust Speedway\stardustBg.png").convert()
bg = pygame.image.load("assets\images\characters\Berkovich.jpeg").convert()
fg = pygame.image.load("assets\images\stages\Stardust Speedway\stardustFloor.png").convert_alpha()
#Scales our background and foregroudn to the size of the screen
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
fg = pygame.transform.scale(fg, (SCREEN_WIDTH, SCREEN_HEIGHT))
#Sets the background and foreground as rectangles in order to manipulate them
bg_width = bg.get_width()
bg_rect = bg.get_rect()
fg_width = fg.get_width()
fg_rect = fg.get_rect()
#Variabels for scrolling images
scroll = 0
tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 2
#Variables for jumping
boingoing = False
jumpGravity = 1
jump = 20
jumpVelocity = jump
#Everything after this point is what happens while our game is running
while running:
    #Quits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Stops running the game
            running = False
        #The reason the sound effects are put here is to only play them after the spacebar is released
        elif event.type == pygame.KEYUP:
            if keys[pygame.K_SPACE]:
                pygame.mixer.Sound.play(sonicJump)
            if keys[pygame.K_LSHIFT] and keys[pygame.K_SPACE]:
                pygame.mixer.Sound.play(sonicJumpWacky)

    #Adds our background
    for i in range(tiles):
        #Forces our background to scroll
        screen.blit(bg, (i * bg_width + scroll - bg_width, 0))
    #How fast our Background and Foreground should scroll
    #Change the minus sign to the plus sign to make everything go backwards or vice versa
    scroll -= 88
    #Resets Scrolling
    if abs(scroll) > bg_width:
        scroll = 0
    #Adds our Player
    screen.blit(player, player_pos)
    #Add the foreground after the player for layering
    for i in range(0, tiles):
        screen.blit(fg, (i * bg_width + scroll - bg_width, -100))
    #Adds our enemy
    screen.blit(enemy, (350,350))
    #All the keys our Game uses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    if keys[pygame.K_a]:
        player_pos.x -= 500 * dt
        if keys[pygame.K_LSHIFT]:
            player_pos.x -= 5000 * dt
    if keys[pygame.K_d]:
        player_pos.x += 500 * dt
        if keys[pygame.K_LSHIFT]:
            player_pos.x += 5000 * dt
    #Enables Jumping        
    if keys[pygame.K_SPACE]:
        boingoing = True
        if keys[pygame.K_LSHIFT]:
           jump = 60
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
        if keys[pygame.K_LSHIFT]:
            player_pos.x -= 5000 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
        if keys[pygame.K_LSHIFT]:
            player_pos.x += 5000 * dt
    #Jump logic handled here
    if boingoing:
        player_pos.y -= jumpVelocity
        jumpVelocity -= jumpGravity
        if jumpVelocity < -jump:
            boingoing = False
            jumpVelocity =jump
    #Adds our work to the screen
    pygame.display.flip()
    #The FPS our game runs at
    dt = clock.tick(60) / 1000