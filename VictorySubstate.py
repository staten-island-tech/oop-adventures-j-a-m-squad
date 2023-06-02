import pygame
from pyvidplayer import Video
pygame.init()
display = pygame.display.set_mode((1280, 720))
keys = pygame.key.get_pressed()    
daVideo = Video("assets/videos/Fortnite Song - Diverse Character (Fortnite Official Song)")
ico = pygame.image.load("icon.png")
pygame.display.set_caption("06-06-06. I'm sorry for your loss. He will be missed by everyone that knew him. He was a lovely man and will be greatly missed. You and your family are in my thoughts and prayers.")
pygame.display.set_icon(ico)
daVideo.set_size((1280,720))
while True:
    daVideo.draw(display, (0,0))
    pygame.display.update()
    for event in pygame.event.get():
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
