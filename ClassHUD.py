import pygame
import math
import mainmenu

pygame.init()
pygame.font.init()

class HUD:
    def __init__(self, daStartingTime):
        self.start = daStartingTime

        self.daFont = pygame.font.Font("assets/fonts/sonic1.ttf", 64)
        self.scoreLabelShadow = self.daFont.render('SCORE', False, (0,0,0))
        self.scoreLabel = self.daFont.render('SCORE', False, (255,255,0))
        self.scoreValueTextShadow = self.daFont.render('0', False, (0,0,0))
        self.scoreValueText = self.daFont.render('0', False, (255,255,255))
        self.timeLabelShadow = self.daFont.render('TIME', False, (0,0,0))
        self.timeLabel = self.daFont.render('TIME', False, (255,255,0))
        self.ringsLabel = self.daFont.render('RINGS', False, (255,255,0))
        self.ringsValueText = self.daFont.render('0', False, (255,255,255))
        self.healthSprite = pygame.transform.scale(pygame.image.load("assets/images/UI/sonicLifeCounter.png"), (75,50))
        self.healthValueText = self.daFont.render('3', False, (255,255,255))

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

        timeValue = "%s" % (sonicCDMin) +"'" + "0%s" % (sonicCDSec) + "'" + '"%s' % (sonicCDMil)
        if (sonicCDSec >= 10):
            timeValue = "%s" % (sonicCDMin) +"'" + "%s" % (sonicCDSec) + "'" + '"%s' % (sonicCDMil)

        self.timeValueText = self.daFont.render(timeValue, False, (255,255,255))

        self.screen = pygame.display.get_surface()

        self.screen.blit(self.scoreLabelShadow, (27,15))
        self.screen.blit(self.scoreLabel, (25,15))
        self.screen.blit(self.scoreValueText, (374,15))
        self.screen.blit(self.timeLabel, (25,75))
        self.screen.blit(self.timeValueText, (175,75))
        self.screen.blit(self.ringsLabel, (25, 135))
        self.screen.blit(self.ringsValueText, (374, 135))
        self.screen.blit(self.healthSprite, (30, 900))
        self.screen.blit(self.healthValueText, (118, 892))

