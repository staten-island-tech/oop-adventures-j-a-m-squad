#Menu
import pygame
import os
from button import Button
from main import play
pygame.init()
def get_font(size):
        return pygame.font.Font("assets/fonts/Avenir-BlackOblique.ttf", size)

SCREEN = pygame.display.set_mode((1920, 1080))
BG = pygame.transform.scale(pygame.image.load("IMG_8638.jpg"), (1920,1080))
CURSOR = pygame.transform.scale2x(pygame.image.load("cursor.png"))

def options():
    while True:
        wega = pygame.transform.scale(pygame.image.load("assets\images\characters\meow.jpg"), (1080,1080))
        spooky = pygame.mixer.Sound("assets\sounds\HL2 Stalker Scream.ogg")
        SCREEN.fill((0,0,0))
        SCREEN.blit(wega, (400, 0))
        pygame.mixer.Sound.play(spooky)

        pygame.display.update()

def main_menu():
    while True:
        
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)

        MENU_TEXT = get_font(100).render("ATTACK OF THE KILLER WHALE(N)", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(1000, 300))

        PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("meow.jpg"), (300,150)), pos=(1000, 450), 
                            text_input="PLAY", font=get_font(64), base_color="White", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("lol.png"), pos=(1000, 600), 
                            text_input="OPTIONS", font=get_font(64), base_color="White", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("lol.png"), pos=(1000, 750), 
                            text_input="QUIT", font=get_font(64), base_color="White", hovering_color="White")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.system('python GameOverSubstate.py')
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    os.system('python GameOverSubstate.py')
                    
        SCREEN.blit(CURSOR, pygame.mouse.get_pos())
        pygame.display.update()

main_menu()