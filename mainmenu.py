import pygame, sys
import math
from menu import *
from ClassHUD import HUD
from attacks import *
from berkovich_class import *
from player import *
pygame.init()

SCREEN = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Menu")

BG = pygame.transform.scale(pygame.image.load("tails.png").convert(), (1920, 1080))
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
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        clock = pygame.time.Clock()
        running = True
        dt = 0
        saving = 0
        start = pygame.time.get_ticks()
        FontSonic = pygame.font.Font("assets/fonts/sonic1.ttf", 64)
        #Setup the players and enemys position on the screen
        player_pos = pygame.Vector2(screen.get_width() / 1.5, screen.get_height() / 1.92)
        player2_pos = pygame.Vector2(screen.get_width()/ 1.75, screen.get_height() / 1.75)
        enemy_pos = pygame.Vector2(-555, 360)
        #Load and play music
        pygame.mixer.music.load("assets/music/Trip to Burger King.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        #Load Sound Effects
        sonicJump = pygame.mixer.Sound("assets\sounds\sonicJump.ogg")
        sonicJumpWacky = pygame.mixer.Sound("assets\sounds\I'm outta here.ogg")
        SaveYourAudio = pygame.mixer.Sound("assets\sounds\Save Your Work audio.mp3")
        #Loads the Player and Enemy
        prey = pygame.transform.scale(pygame.image.load("assets\images\characters\Berkovich.jpeg"), (200,200))
        bystander = pygame.transform.scale(pygame.image.load("assets\images\characters\When you outside and smell that ZAZA.png"), (150,150))
        predator = pygame.transform.scale(pygame.image.load("WhalenPic.png"), (300,280))
        #Loads our Background and Foreground and scales them to the size of our screen
        bg = pygame.transform.scale(pygame.image.load("assets\images\stages\Stardust Speedway\stardustBg.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        fg = pygame.transform.scale(pygame.image.load("assets\images\stages\Stardust Speedway\stardustFloor.png").convert_alpha(), (SCREEN_WIDTH+500, SCREEN_HEIGHT+500))
        #Sets the background and foreground as rectangles in order to manipulate them later
        bg_width = bg.get_width()
        fg_width = fg.get_width()
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

            SaveYour_pos = pygame.Vector2(1500, 400)
            commit_pos = pygame.Vector2(1500,600)
            saving += 1
            #Quits the game
            for event in pygame.event.get():
                saving += 1
                if event.type == pygame.QUIT:
                    #Stops running the game
                    running = False
                #The reason the sound effects are put here is to only play them after the spacebar is released
                elif event.type == pygame.KEYUP:
                    if keys[pygame.K_SPACE]:
                        pygame.mixer.Sound.play(sonicJump)
                    if keys[pygame.K_LSHIFT] and keys[pygame.K_SPACE]:
                        pygame.mixer.Sound.play(sonicJumpWacky)
            #Time logic handled here
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
            screen.blit(predator, enemy_pos)
            screen.blit(bystander, player2_pos) 
            screen.blit(prey, player_pos)
            Basic(start, 8)
            #Get the enemy into frame
            if player_pos.x > 1750 :
                player_pos.x = 1700
                player2_pos.x = 1700
            if player_pos.x < -100:
                player_pos.x = 0
                player2_pos.x = 0
            if player_pos.y > 563:
                player_pos.y = 562.5
                player2_pos.y = 562.5
            if player_pos.y < 0:
                player_pos.y = 1
                player2_pos.y = 1
            #Add the foreground after the player and enemy for layering            
            """ for i in range(0, tiles):
                screen.blit(SaveYour, (i * bg_width + floorSpeed - bg_width, +400))
                pygame.mixer.Sound.play(SaveYourAudio)
            for i in range(0, tiles):
                screen.blit(commit, (i * bg_width + bgSpeed - bg_width, +650))
                pygame.mixer.Sound.play(SaveYourAudio) """
            for i in range(0, tiles):
                screen.blit(fg, (i * bg_width + floorSpeed - bg_width, -500))
            #Add the HUD above everything else
            HUD(start)
            berkovich(start)
            # #All the keys our Game uses
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
            # #Every key below this is keys for movement
            # if keys[pygame.K_a]:
            #     player_pos.x -= 1111 * dt
            #     player2_pos.x -= 950 * dt
            #     if keys[pygame.K_LSHIFT]:
            #         player_pos.x -= 5000 * dt
            #         player2_pos.x -= 4500 * dtS
            # if keys[pygame.K_d]:
            #     player_pos.x += 1111 * dt
            #     player2_pos.x += 950 * dt
            #     if keys[pygame.K_LSHIFT]: 
            #         player_pos.x += 5000 * dt
            #         player2_pos.x += 4500 * dt
            # #Enables Jumping        
            # if keys[pygame.K_SPACE]:
            #     boingoing = True
            #     if keys[pygame.K_LSHIFT]:
            #         jump = 60
            # #Alternative keys for movement
            # if keys[pygame.K_LEFT]:
            #     player_pos.x -= 1111 * dt
            #     player2_pos.x -= 950 * dt
            #     if keys[pygame.K_LSHIFT]:
            #         player_pos.x -= 5000 * dt
            #         player2_pos.x -= 4500 * dt
            # if keys[pygame.K_RIGHT]:
            #     player_pos.x += 1111 * dt
            #     player2_pos.x += 950 * dt
            #     if keys[pygame.K_LSHIFT]:
            #         player_pos.x += 5000 * dt
            #         player2_pos.x += 4500 * dt
            # #Jump logic handled here
            # if boingoing:
            #     player_pos.y -= jumpVelocity
            #     player2_pos.y -= jumpVelocity
            #     jumpVelocity -= jumpGravity
            #     if jumpVelocity < -jump:
            #         boingoing = False
            #         jumpVelocity = jump
            #Adds our work to the screen
            pygame.display.flip()
            #The FPS our game runs at
            dt = clock.tick(60) / 1000


            pygame.display.update()
