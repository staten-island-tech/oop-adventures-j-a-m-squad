import pygame
import math

pygame.init()

class micheal(pygame.sprite.Sprite):
    def __init__(self, daStartingTime, enemyHitbox = pygame.Rect, enemyVector = pygame.Vector2):
        self.start = daStartingTime
        self.poop = pygame.transform.scale(pygame.image.load("WhalenPic.png"), (300,280))
        self.enemyPosition = enemyVector
        self.ouchy = enemyHitbox

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
        
        if sonicCDSec >= 8 and sonicCDMin >= 0:
            self.screen.blit(self.poop, enemyVector)
            pygame.draw.rect(self.screen, (255,0,0), self.ouchy, 200)
            self.ouchy.topleft = enemyVector
            if enemyVector.x != 1500:
                enemyVector.x += 30
