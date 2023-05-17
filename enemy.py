#enemy
import pygame   
import pygame, sys
from button import Button
import math
pygame.font.init()
enemy_pos = pygame.Vector2(0, 360)
SaveYour_pos = pygame.Vector2(1500, 400)
commit_pos = pygame.Vector2(1500,600)
SaveYourAudio = pygame.mixer.Sound("assets\sounds\Save Your Work audio.mp3")
class whale:
    def __init__(self,daStartingTime, seconds4timing):
        self.start = daStartingTime
        self.predator = pygame.transform.scale(pygame.image.load("WhalenPic.png"), (300,280))

        self.FontSonic = pygame.font.Font("assets/fonts/sonic1.ttf", 64)
        self.SaveYour = self.FontSonic.render('SAVE YOUR WORK', False, (255,255,0))
        self.commit = self.FontSonic.render('COMMIT TO GITHUB', False, (255,255,0))
        
        self.sonicCDMil = 0
        self.sonicCDSec = 0
        self.sonicCDMin = 0
        self.finalMil = 00
        self.finalSec = 00
        counting = pygame.time.get_ticks() - self.start
        if (math.floor(self.start) >= 0):
            sonicCDSec = (math.floor((math.floor(counting) / 1000) % 60))
            sonicCDMil = ((round(((math.floor(counting)) % 1000) / 10) % 100))
            sonicCDMin = (math.floor(math.floor((math.floor(counting) / 1000) / 60) % 60))

        if (sonicCDMil < 10):
            self.finalMil = sonicCDMil
        else:
            self.finalMil = sonicCDMil
        if (sonicCDSec < 10):
            self.finalSec = sonicCDSec
        else:
            self.finalSec = sonicCDSec

        self.screen = pygame.display.get_surface()

        if sonicCDSec >= 8:
            self.screen.blit(self.predator, enemy_pos)
            if enemy_pos.x != 1500:
                enemy_pos.x += 30
        if sonicCDSec == seconds4timing:
            self.screen.blit(self.SaveYour, SaveYour_pos)
            if SaveYour_pos.x != 0:
                SaveYour_pos.x -= 30
            elif SaveYour_pos.x != 1500:
                SaveYour_pos.x += 1500 #It was this fucking easy Michael
            pygame.mixer.Sound.play(SaveYourAudio)
        if sonicCDSec == seconds4timing + 1:
            self.screen.blit(self.commit, commit_pos)            
            if commit_pos.x != 0:
                commit_pos.x -= 30
            elif commit_pos.x != 1500:
                commit_pos.x += 1500 #stu-pid Jessica lover
        
        


            




