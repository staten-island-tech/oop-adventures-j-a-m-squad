import pygame

pygame.init()


class albert(pygame.sprite.Sprite):
    def __init__(self,deltaTime, playerImage, x,y,width, height, playerVector = pygame.Vector2):
        self.display = pygame.display.get_surface()
    
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.thingamajig = playerImage
        self.dt = deltaTime
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 17, self.y + 11, 29, 52) 
        self.playerPosition = playerVector
        self.sonicJump = pygame.mixer.Sound("assets\sounds\sonicJump.ogg")
        self.sonicJumpWacky = pygame.mixer.Sound("assets\sounds\I'm outta here.ogg")

        self.keys = pygame.key.get_pressed()

        self.display.blit(self.thingamajig, self.playerPosition)

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
    def draw(self, win):
        self.hitbox = (self.x + 17, self.y + 11, 29, 52) # NEW
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
       
                
        