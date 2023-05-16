import pygame

pygame.init()
pygame.font.init()

class HUD:
    def __init__(self):
        self.daFont = pygame.font.Font("soniccd.ttf", 25)

        self.scoreLabel = self.daFont.render("SCORE", False, (255,255,0))
        self.scoreLabelShadow = self.daFont.render("SCORE", False, (0,0,0))
        self.timeLabel = self.daFont.render("TIME", False, (255,255,0))
        self.timeLabelShadow = self.daFont.render("TIME", False, (0,0,0))
        self.ringsLabel = self.daFont.render("RINGS", False, (255,255,0))
        self.ringsLabelShadow = self.daFont.render("RINGS", False, (0,0,0))

        self.display = pygame.display.get_surface()
        self.display.blit(self.scoreLabelShadow, (12,10))
        self.display.blit(self.scoreLabel, (10,10))
        self.display.blit(self.timeLabelShadow, (12,40))
        self.display.blit(self.timeLabel, (10,40))
        


