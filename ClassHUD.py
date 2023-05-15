import pygame

pygame.init()
pygame.font.init()

class HUD:
    def __init__(self):
        self.daFont = pygame.font.Font("PhantomMuff Full Letters 1.1.5.ttf", 64)
        self.message = "This is my HUD. I love it <3"
        self.string = self.daFont.render(self.message, False, (0,0,0))
        self.display = pygame.display.get_surface()
        self.display.blit(self.string, (0,0))

