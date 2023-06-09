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
        self.ThirdBar = self.daFont.render('and make it a meal so I can get a drink', False, (255,255,255))
        self.FourthBar = self.daFont.render('No, Im not finished, thats not everything', False, (255,255,255))
        self.FifthBar = self.daFont.render('Can I please get a Double Whopper with no cheese?', False, (255,255,255))
        self.SixthBar = self.daFont.render('Can I please get a number two with a large drink?', False, (255,255,255))
        self.SeventhBar = self.daFont.render('I got money so I dont care how much it costs me', False, (255,255,255))
        self.EigthBar = self.daFont.render('So just throw in some extra fries, dont make them salty', False, (255,255,255))
        self.NinthBar = self.daFont.render('All this cheese gonna make my booty drip drip', False, (255,255,255))
        self.TenthBar = self.daFont.render('Im lactose intolerant, I dont sip milk', False, (255,255,255))
        self.EleventhBar = self.daFont.render('If I see a sight of cheese, Ima trip trip', False, (255,255,255))
        self.TwelthBar = self.daFont.render('Ima sit on your toilet seat and doodoo then dip', False, (255,255,255))
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

        if sonicCDSec >= 1 and sonicCDSec <= 2: 
            self.screen.blit(self.FirstBar,general_pos)
            if general_pos.x != -1000:
                general_pos.x -= 50
            elif general_pos.x < 1700:
                general_pos.x += 2700
        if sonicCDSec >= 4 and sonicCDSec <= 5:
            self.screen.blit(self.SecondBar, general_pos)
            if general_pos.x != -1000:
                general_pos.x -= 50
            elif general_pos.x < 1700:
                general_pos.x += 2700
        if sonicCDSec >= 6 and sonicCDSec <= 7:
            self.screen.blit(self.ThirdBar, general_pos)
            if general_pos.x != -1000:
                general_pos.x -= 50
            elif general_pos.x <1700:
                general_pos.x += 2700
        if sonicCDSec >= 9 and sonicCDSec <= 10:
            self.screen.blit(self.FourthBar, general_pos)
            if general_pos.x != -1000:
                general_pos.x -=50
            elif general_pos.x <1700:
                general_pos.x += 2700
        if sonicCDSec >= 11 and sonicCDSec <= 12:
            self.screen.blit(self.FifthBar, general_pos)
            if general_pos.x != -1000:
                general_pos.x -=50
            elif general_pos.x <1700:
                general_pos.x += 2700
        if sonicCDSec >= 14 and sonicCDSec <= 15:
            self.screen.blit(self.SixthBar, general_pos)
            if general_pos.x != -1000:
                general_pos.x -=50
            elif general_pos.x <1700:
                general_pos.x += 2700
        if sonicCDSec >= 16 and sonicCDSec <= 17:
            self.screen.blit(self.SeventhBar, general_pos)
            if general_pos.x != -1000:
                general_pos.x -=50
            elif general_pos.x <1700:
                general_pos.x += 2700
        if sonicCDSec >= 18 and sonicCDSec <= 19:
            self.screen.blit(self.EigthBar, general_pos)
            if general_pos.x != -1000:
                general_pos.x -=50
            elif general_pos.x <1700:
                general_pos.x += 2700
        if sonicCDSec >= 21 and sonicCDSec <= 22:
            self.screen.blit(self.NinthBar, general_pos)
            if general_pos.x != -1000:
                general_pos.x -=50
            elif general_pos.x <1700:
                general_pos.x += 2700        
        if sonicCDSec >= 23 and sonicCDSec <= 24:
            self.screen.blit(self.TenthBar, general_pos)
            if general_pos.x != -1000:
                general_pos.x -=50
            elif general_pos.x <1700:
                general_pos.x += 2700
        if sonicCDSec >= 26 and sonicCDSec <= 27:
            self.screen.blit(self.EleventhBar, general_pos)
            if general_pos.x != -1000:
                general_pos.x -=50
            elif general_pos.x <1700:
                general_pos.x += 2700
        if sonicCDSec >= 28 and sonicCDSec <= 29:
            self.screen.blit(self.TwelthBar, general_pos)
            if general_pos.x != -1000:
                general_pos.x -=50
            elif general_pos.x <1700:
                general_pos.x += 2700