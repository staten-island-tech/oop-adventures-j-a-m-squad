import pygame
import mainmenu

pygame.init()

class albert(pygame.sprite.Sprite):
    def __init__(self, x, y, deltaTime, playerImage, playerVector = pygame.Vector2):
        self.display = pygame.display.get_surface()
        self.thingamajig = playerImage
        self.playerPosition = playerVector
        self.dt = deltaTime
        self.x = x
        self.velx = 10
        self.y = y
        self.vely = 10
        self.sonicJump = pygame.mixer.Sound("assets\sounds\sonicJump.ogg")
        self.sonicJumpWacky = pygame.mixer.Sound("assets\sounds\I'm outta here.ogg")
        self.hitbox = (self.x, self.y, 64, 64)
        self.keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if self.keys[pygame.K_SPACE]:
                pygame.mixer.Sound.play(self.sonicJump)

        if self.keys[pygame.K_a]:
            self.playerPosition.x -= 1000 * self.dt
        if self.keys[pygame.K_d]:
            self.playerPosition.x += 1000 * self.dt   
        if self.keys[pygame.K_SPACE]:
            self.boingoing = True
        if self.keys[pygame.K_LEFT]:
            self.playerPosition.x -= 1000 * self.dt
        if self.keys[pygame.K_RIGHT]:
            self.playerPosition.x += 1000 * self.dt

        self.display.blit(self.thingamajig, self.playerPosition)
                
        