import pygame
from pyvidplayer import Video
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
keys = pygame.key.get_pressed()    
daVideo = Video("assets/videos/Game Over (Milk) - Soulles DX Milk & Cereal DLC.mp4")
pygame.display.set_caption("06-06-06. I'm sorry for your loss. He will be missed by everyone that knew him. He was a lovely man and will be greatly missed. You and your family are in my thoughts and prayers.")
daVideo.set_size((1280,720))
def gameoverstart():
    while True:
        daVideo.draw(SCREEN, (0,0), force_draw=False)
        pygame.display.update()
        for event in pygame.event.get():
            pygame.display.update()
gameoverstart()