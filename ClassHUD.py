import pygame

pygame.init()
pygame.font.init()

class HUD:
    def __init__(self):
        self.daFont = pygame.font.Font("assets/fonts/sonic1.ttf", 64)
        self.message = "This is my HUD. I love it <3"
        self.string = self.daFont.render(self.message, False, (0,0,0))
        self.display = pygame.display.get_surface()
        self.display.blit(self.string, (self.display.get_width() / 1.5, self.display.get_height() / 1.92))

