#Setup Python
import pygame
import math
from pygame.locals import *
#Start Pygame
pygame.init()
pygame.font.init()
#Screen Width and Height Variable (Makes it super easy if we ever want to change it)
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
#Setup Game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
start = pygame.time.get_ticks()
running = True
dt = 0
FontSonic = pygame.font.Font("assets/fonts/sonic1.ttf", 50)
#Setup the players and enemys position on the screen
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.9)
player2_pos = pygame.Vector2(screen.get_width()/ 2.5, screen.get_height() / 1.75)
#Load and play music
pygame.mixer.music.load("assets\music\Trip to Harlem.ogg")
pygame.mixer.music.play(-1)
#Load Sound Effects
sonicJump = pygame.mixer.Sound("assets\sounds\sonicJump.ogg")
sonicJumpWacky = pygame.mixer.Sound("assets\sounds\I'm outta here.ogg")
#Loads the Player and Enemy
prey = pygame.transform.scale(pygame.image.load("assets\images\characters\Berkovich.jpeg"), (200,200))
bystander = pygame.transform.scale(pygame.image.load("assets\images\characters\When you outside and smell that ZAZA.png"), (150,150))
predator = pygame.transform.scale(pygame.image.load("assets\images\characters\egghead.jpeg"), (250,250))
#Loads our Background and Foreground and scales them to the size of our screen
bg = pygame.transform.scale(pygame.image.load("assets\images\stages\Stardust Speedway\stardustBg.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
fg = pygame.transform.scale(pygame.image.load("assets\images\stages\Stardust Speedway\stardustFloor.png").convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
#Sets the background and foreground as rectangles in order to manipulate them later
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
#Variables for HUD
scoreLabel = FontSonic.render('SCORE', False, (255,255,0))
scoreValueText = FontSonic.render('0', False, (255,255,255))
timeLabel = FontSonic.render('TIME', False, (255,255,0))
ringsLabel = FontSonic.render('RINGS', False, (255,255,0))
ringsValueText = FontSonic.render('0', False, (255,255,255))
healthSprite = pygame.transform.scale(pygame.image.load("assets/images/UI/sonicLifeCounter.png"), (75,50))
healthValueText = FontSonic.render('3', False, (255,255,255))
#Variables for Time
sonicCDMil = 0
sonicCDSec = 0
sonicCDMin = 0
finalMil = 00
finalSec = 00
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
    #Time logic handled here
    counting = pygame.time.get_ticks() - start
    if (math.floor(start) >= 0):
        sonicCDSec = (math.floor((math.floor(counting) / 1000) % 60))
        sonicCDMil = ((round(((math.floor(counting)) % 1000) / 10) % 100))
        sonicCDMin = (math.floor(math.floor((math.floor(counting) / 1000) / 60) % 60))
    if (sonicCDMil < 10):
        finalMil = sonicCDMil
    else:
        finalMil = sonicCDMil
    if (sonicCDSec < 10):
        finalSec = sonicCDSec
    else:
        finalSec = sonicCDSec
    timeValue = "0%s'0%s'%s" % (sonicCDMin, sonicCDSec, sonicCDMil)
    if (sonicCDSec >= 10):
        timeValue = "0%s'%s'%s" % (sonicCDMin, sonicCDSec, sonicCDMil)
    if (sonicCDMin >= 10):
        timeValue = "%s'%s'%s" % (sonicCDMin, sonicCDSec, sonicCDMil)
    timeValueText = FontSonic.render(timeValue, False, (255,255,255))
    #Adds our background
    for i in range(tiles):
        #Forces our background to scroll
        screen.blit(bg, (i * bg_width + scroll - bg_width, 0))
    #How fast our Background and Foreground should scroll
    #Change the minus sign to the plus sign to make everything go backwards or vice versa
    scroll -= 25
    #Resets Scrolling
    if abs(scroll) > bg_width:
        scroll = 0
    #Adds our Player, Player 2, and enemy
    screen.blit(prey, player_pos)  
    screen.blit(bystander, player2_pos)
    #Add the foreground after the player and enemy for layering
    for i in range(0, tiles):
        screen.blit(fg, (i * bg_width + scroll - bg_width, -100))
    #Add the HUD above everything else
    screen.blit(scoreLabel, (222,140))
    screen.blit(scoreValueText, (507,140))
    screen.blit(timeLabel, (222,190))
    screen.blit(timeValueText, (350,190))
    screen.blit(ringsLabel, (222, 240))
    screen.blit(ringsValueText, (482, 240))
    screen.blit(healthSprite, (222, 888))
    screen.blit(healthValueText, (310, 892))
    #All the keys our Game uses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    #Every key below this is keys for movement
    if keys[pygame.K_a]:
        player_pos.x -= 1000 * dt
        player2_pos.x -= 950 * dt
        if keys[pygame.K_LSHIFT]:
            player_pos.x -= 5000 * dt
            player2_pos.x -= 4500 * dt
    if keys[pygame.K_d]:
        player_pos.x += 1000 * dt
        player2_pos.x += 950 * dt
        if keys[pygame.K_LSHIFT]:
            player_pos.x += 5000 * dt
            player2_pos.x += 4500 * dt
    #Enables Jumping        
    if keys[pygame.K_SPACE]:
        boingoing = True
        if keys[pygame.K_LSHIFT]:
           jump = 60
    #Alternative keys for movement
    if keys[pygame.K_LEFT]:
        player_pos.x -= 1000 * dt
        player2_pos.x -= 950 * dt
        if keys[pygame.K_LSHIFT]:
            player_pos.x -= 5000 * dt
            player2_pos.x -= 4500 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 1000 * dt
        player2_pos.x += 950 * dt
        if keys[pygame.K_LSHIFT]:
            player_pos.x += 5000 * dt
            player2_pos.x += 4500 * dt
    #Jump logic handled here
    if boingoing:
        player_pos.y -= jumpVelocity
        player2_pos.y -= jumpVelocity
        jumpVelocity -= jumpGravity
        if jumpVelocity < -jump:
            boingoing = False
            jumpVelocity = jump
    #Adds our work to the screen
    pygame.display.flip()
    #The FPS our game runs at
    dt = clock.tick(60) / 1000