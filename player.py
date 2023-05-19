import pygame
import mainmenu

pygame.init()

class albert(pygame.sprite.Sprite):
    def __init__(self, deltaTime, playerImage):
        self.display = pygame.display.get_surface()

        self.boingoing = False
        self.jumpGravity = 1
        self.jump = 16
        self.jumpVelocity = self.jump

        self.thingamajig = playerImage
        self.playerPosition = pygame.Vector2(self.display.get_width() / 1.5, self.display.get_height() / 1.92)
        self.dt = deltaTime

        self.sonicJump = pygame.mixer.Sound("assets\sounds\sonicJump.ogg")
        self.sonicJumpWacky = pygame.mixer.Sound("assets\sounds\I'm outta here.ogg")

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

        if self.boingoing:
            self.playerPosition.y -= self.jumpVelocity
            self.jumpVelocity -= self.jumpGravity
            if self.jumpVelocity < -self.jump:
                self.boingoing = False
                self.jumpVelocity = self.jump

        self.display.blit(self.thingamajig, self.playerPosition)
                
        