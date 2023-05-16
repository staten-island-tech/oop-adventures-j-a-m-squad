import pygame

pygame.init()
pygame.font.init()

class HUD:
    def __init__(self, urFont):
        self.daFont = pygame.font.Font(urFont, 25)
        self.scoreText = self.daFont.render("SCORE", False, (255,255,0))
        self.stringShadow = self.daFont.render("SCORE", False, (0,0,0))
        self.display = pygame.display.get_surface()
        self.display.blit(self.stringShadow, (12,10))
        self.display.blit(self.scoreText, (10,10))
        


