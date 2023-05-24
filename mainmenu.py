import pygame, sys
import math
from menu import *
from ClassHUD import HUD
from attacks import *
from berkovich_class import *
from player import *
from enemy import micheal
pygame.init()

SCREEN = pygame.display.set_mode((1920, 1080))

BG = pygame.transform.scale(pygame.image.load("IMG_8638.jpg"), (1920,1080))

def play():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    #Stops running the game
                pygame.quit()
                sys.exit()
        SCREEN_WIDTH = 1920
        SCREEN_HEIGHT = 1080
        #Setup Game
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        running = True
        dt = 0
        start = pygame.time.get_ticks()
        #Setup the players and enemys position on the screen
        player_pos = pygame.Vector2(screen.get_width() / 1.5, screen.get_height() / 1.92)
        #Load and play music
        pygame.mixer.music.load("assets/music/Trip to Burger King.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        #Load Sound Effects
        sonicJump = pygame.mixer.Sound("assets\sounds\sonicJump.ogg")
        #Loads the Player and Enemy
        prey = pygame.transform.scale(pygame.image.load("assets\images\characters\Berkovich.jpeg"), (200,200))
        preyHitbox = prey.get_rect()
        #Loads our Background and Foreground and scales them to the size of our screen
        bg = pygame.transform.scale(pygame.image.load("assets\images\stages\Stardust Speedway\stardustBg.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        fg = pygame.transform.scale(pygame.image.load("assets\images\stages\Stardust Speedway\stardustFloor.png").convert_alpha(), (SCREEN_WIDTH+500, SCREEN_HEIGHT+500))
        #Sets the background and foreground as rectangles in order to manipulate them later
        bg_width = bg.get_width()
        #Variabels for scrolling images
        bgSpeed = 0
        floorSpeed = 0
        tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 2
        #Variables for jumping
        boingoing = False
        jumpGravity = 1
        jump = 16
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
            #Adds our background
            for i in range(tiles):
                #Forces our background to scroll
                screen.blit(bg, (i * bg_width + bgSpeed - bg_width, 0))
            #How fast our Background and Foreground should scroll
            #Change the minus sign to the plus sign to make everything go backwards or vice versa
            bgSpeed -= 10
            floorSpeed += 25
            #Resets Scrolling
            if abs(bgSpeed) > bg_width:
                bgSpeed = 0
            if abs(floorSpeed) > bg_width:
                floorSpeed = 0
            #Adds our Player, Player 2, and enemy
            albert(dt, prey, preyHitbox, player_pos)
            micheal(start)
            basicAttack(start, 10)
            #Add the foreground after the player and enemy for layering            
            for i in range(0, tiles):
                screen.blit(fg, (i * bg_width + floorSpeed - bg_width, -500))
            #Add the HUD above everything else
            HUD(start)
            berkovich(start)
            # #All the keys our Game uses
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
            # #Enables Jumping        
            if keys[pygame.K_SPACE]:
                boingoing = True
            # #Jump logic handled here
            if boingoing:
                player_pos.y -= jumpVelocity
                jumpVelocity -= jumpGravity
                if jumpVelocity < -jump:
                    boingoing = False
                    jumpVelocity = jump
            #Adds our work to the screen
            pygame.display.flip()
            #The FPS our game runs at
            dt = clock.tick(360) / 1000
            pygame.display.update()
