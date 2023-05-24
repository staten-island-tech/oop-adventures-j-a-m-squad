import pygame
import math
pygame.font.init()

general_pos = pygame.Vector2(1700,200)

class drivethru:
    def __init__(self,daStartingTime):
        self.start = daStartingTime
        self.daFont = pygame.font.Font("assets/fonts/sonic1.ttf", 64)
        self.FirstBar = self.daFont.render('Im in a drive thru of burgerking', False, (255,255,255))
        self.SecondBar = self.daFont.render('Can I please get a Whopper jr with onion rings', False, (255,255,255))
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

        if sonicCDSec >= 1 and sonicCDSec <= 3: 
            self.screen.blit(self.FirstBar,general_pos)
            if general_pos.x != -10:
                general_pos.x -= 37
            elif general_pos.x != 1700:
                general_pos.x += 1710
        if sonicCDSec >= 3 and sonicCDSec <= 5:
            self.screen.blit(self.SecondBar, general_pos)
