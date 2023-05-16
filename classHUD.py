import pygame

pygame.init()
pygame.font.init()

class HUD:
    def __init__(self, urFont):
        self.daFont = pygame.font.Font(urFont, 25)
        self.message = "SCORE"
        self.string = self.daFont.render(self.message, False, (255,255,0))
        self.stringShadow = self.daFont.render(self.message, False, (0,0,0))
        self.display = pygame.display.get_surface()
        self.display.blit(self.string, (10,10))


