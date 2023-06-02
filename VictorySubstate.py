import pygame
from pyvidplayer import Video
pygame.init()
display = pygame.display.set_mode((1280, 720))
keys = pygame.key.get_pressed()    
daVideo = Video("assets/videos/Fortnite Song - Diverse Character (Fortnite Official Song).mp4")
ico = pygame.image.load("berkovich.jpeg")
pygame.display.set_caption("VICTORY ROYALE")
pygame.display.set_icon(ico)
daVideo.set_size((1280,720))
while True:
    daVideo.draw(display, (0,0))
    pygame.display.update()
    for event in pygame.event.get():
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
