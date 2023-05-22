import pygame
import math
import random
class berkovich:
        def __init__(self, daStartingTime, x, y):
            self.start = daStartingTime

            self.poop = pygame.transform.scale(pygame.image.load("assets\images\characters\Berkovich.jpeg"), (1080,1080))
            self.goofyahh = pygame.mixer.Sound("ahh.ogg")
            self.goofy = False
            self.x = x
            self.y = y
            self.sonicCDMil = 0
            self.sonicCDSec = 0
            self.sonicCDMin = 0
            self.finalMil = 00
            self.finalSec = 00
            self.hitbox = (self.x, self.y, 64, 64)

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

            if sonicCDMil == random.randint(1,60):
                 self.screen.fill((0,0,0))
                 self.screen.blit(self.poop, (400,0))
                 pygame.mixer.Sound.play(self.goofyahh)
                 pygame.mixer.Sound.play(self.goofyahh)
                 pygame.mixer.Sound.play(self.goofyahh)
                 pygame.mixer.Sound.play(self.goofyahh)
                 pygame.mixer.Sound.play(self.goofyahh)
                 pygame.mixer.Sound.play(self.goofyahh)
                 pygame.display.update()
                 

