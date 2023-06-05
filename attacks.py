import pygame
import math
import random
pygame.font.init()

SaveYour_pos = pygame.Vector2(1500, 300)
commit_pos = pygame.Vector2(1500,666)
SaveYourAudio = pygame.mixer.Sound("assets\sounds\Save Your Work audio.mp3")

test = pygame.transform.scale(pygame.image.load("lol.png"), (600,75))

testBox = test.get_rect()
iThoguhtThisWasSupposeToBeATest = test.get_rect()

class basicAttack:
    def __init__(self,daStartingTime, seconds4timing, attackSpeed = int, attackSpeedToo = int, attackHitbox1 = pygame.Rect, attackHitbox2 = pygame.Rect): #Without specified minutes, it will reapeat everytime the secounds are equal to the input
        self.start = daStartingTime

        self.daFont = pygame.font.Font("assets/fonts/HelpMe.ttf", 64)
        self.SaveYour = self.daFont.render('SAVE YOUR WORK', False, (255,255,255))
        self.commit = self.daFont.render('COMMIT TO GITHUB', False, (255,255,255))
        self.doohickey = attackHitbox1
        self.thingamajig = attackHitbox2
        
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

        if sonicCDSec == random.randint(1,60):
            pygame.draw.rect(self.screen, (255,0,0), self.thingamajig, 200)
            self.thingamajig.topleft = (SaveYour_pos)
            self.screen.blit(self.SaveYour, SaveYour_pos)
            if SaveYour_pos.x != -0:
                SaveYour_pos.x -= attackSpeed
            elif SaveYour_pos.x != 1500:
                SaveYour_pos.x += 1500 #It was this easy Michael
                self.thingamajig.move((1500,300))
            pygame.mixer.Sound.play(SaveYourAudio)
        if sonicCDSec == random.randint(1,60) + 1:
            pygame.draw.rect(self.screen, (255,0,0), self.doohickey, 200)
            self.doohickey.topleft = (commit_pos)
            self.screen.blit(self.commit, commit_pos)            
            if commit_pos.x != -0:
                commit_pos.x -= attackSpeedToo
            elif commit_pos.x != 1500:
                commit_pos.x += 1500 #i dot
                self.doohickey.move((1500,666))


            




