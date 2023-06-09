import pygame

pygame.init()


class albert(pygame.sprite.Sprite):
    def __init__(self, deltaTime, playerImage, playerInControl, playerHitbox = pygame.Rect, playerVector = pygame.Vector2):
        self.display = pygame.display.get_surface()
        
        self.thingamajig = playerImage
        self.doohickey = playerHitbox
        self.playerPosition = playerVector
        self.dt = deltaTime
        self.canMove = playerInControl

        self.sonicJump = pygame.mixer.Sound("assets\sounds\sonicJump.ogg")
        self.sonicJumpWacky = pygame.mixer.Sound("assets\sounds\I'm outta here.ogg")

        self.keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if self.keys[pygame.K_SPACE]:
                pygame.mixer.Sound.play(self.sonicJump)
        if self.canMove:
            if self.keys[pygame.K_a]:
                self.playerPosition.x -= 1500 * self.dt
            if self.keys[pygame.K_d]:
                self.playerPosition.x += 1500 * self.dt   
            if self.keys[pygame.K_SPACE]:
                self.boingoing = True
            if self.keys[pygame.K_LEFT]:
                self.playerPosition.x -= 1500 * self.dt
            if self.keys[pygame.K_RIGHT]:
                self.playerPosition.x += 1500 * self.dt
        
        self.doohickey.topleft = (self.playerPosition)
        pygame.draw.rect(self.display, (255,0,255), self.doohickey, 100)
        self.display.blit(self.thingamajig, self.playerPosition)
                
        