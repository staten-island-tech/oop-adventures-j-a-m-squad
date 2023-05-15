#Menu
import pygame   
import pygame, sys
import os
from button import Button
from mainmenu import play
pygame.init()
class MENU:
    def __init__(self):
        def get_font(size): # Returns Press-Start-2P in the desired size
            return pygame.font.Font("assets/fonts/sonic1.ttf", size)
        self.SCREEN = pygame.display.set_mode((1920, 1080))
        self.BG = pygame.transform.scale(pygame.image.load("IMG_8638.jpg"), (1920,1080))
        self.CURSOR = pygame.image.load("IMG_8638.jpg")
        def options():
            while True:
                wega = pygame.transform.scale(pygame.image.load("assets\images\characters\meow.jpg"), (1080,1080))
                spooky = pygame.mixer.Sound("assets\sounds\HL2 Stalker Scream.ogg")
                self.SCREEN.fill((0,0,0))
                self.SCREEN.blit(wega, (400, 0))
                pygame.mixer.Sound.play(spooky)

                pygame.display.update()

        def main_menu():
            while True:
                self.SCREEN.blit(self.BG, (0, 0))
                self.SCREEN.blit(self.CURSOR, pygame.mouse.get_pos())

                MENU_MOUSE_POS = pygame.mouse.get_pos()
                pygame.mouse.set_visible(False)

                MENU_TEXT = get_font(100).render("ATTACK OF THE KILLER WHALE(N)", True, "#FFFFFF")
                MENU_RECT = MENU_TEXT.get_rect(center=(1000, 300))

                PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("meow.jpg"), (300,150)), pos=(1000, 450), 
                                    text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
                OPTIONS_BUTTON = Button(image=pygame.image.load("lol.png"), pos=(1000, 600), 
                                    text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
                QUIT_BUTTON = Button(image=pygame.image.load("lol.png"), pos=(1000, 750), 
                                    text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

                self.SCREEN.blit(MENU_TEXT, MENU_RECT)

                for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                    button.changeColor(MENU_MOUSE_POS)
                    button.update(self.SCREEN)
                
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
                pygame.display.update()

MENU.main_menu()