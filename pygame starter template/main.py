import pygame
import random
import math

HEIGHT = 360
WIDTH = 480
FPS = 45
title = "Template"

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
ORANGE = (255,116,0)
YELLOW = (255,211,0)
LIME = (182,255,0)
CYAN = (0,199,199)
MAGENTA = (215,0,174)
PURPLE = (145,0,208)
DARKGREEN = (15,109,0)

GRIDMOVEMENT = False
REGMOVEMENT = True

# game Classes
class Npc(pygame.sprite.Sprite):
    def __init__(self):
        super(Npc, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottomright = (0,0)
        self.do_Circle = False
        self.speedx = 10
        self.speedy = 10
        self.ang = 0
        self.screenwrap = False
        self.warping = False
        self.circling = False
        self.boardering = False
        self.bounceing = True
        if self.screenwrap:
            self.rect.center = (WIDTH/2, HEIGHT/2)
            self.speedx = 10
            self.speedy = 0
        if self.warping:
            self.rect.center = (WIDTH/2, HEIGHT/2)
            self.speedx = 10
            self.speedy = 0
        if self.circling:
            self.rect.bottomright = (0, 0)
            self.speedx = 10
            self.speedy = 10
        if self.boardering:
            self.rect.center = (WIDTH / 2, HEIGHT / 2)
            self.speedx = 10
            self.speedy = 0
        if self.bounceing:
            self.rect.center = (10, 10)
            self.speedx = 5
            self.speedy = 5
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # screen wrapping wrap
        if self.screenwrap:
            if self.rect.left > WIDTH:
                self.rect.right = 0
            elif self.rect.right < 0:
                self.rect.left = WIDTH
            elif self.rect.bottom < 0:
                self.rect.top = HEIGHT
            elif self.rect.top > HEIGHT:
                self.rect.bottom = 0

        # Warping
        if self.warping:
            if self.rect.left > WIDTH:
                self.rect.top = HEIGHT
                self.rect.centerx = WIDTH/2
                self.speedx=0
                self.speedy = -10
            if self.rect.bottom < 0:
                self.rect.left = WIDTH
                self.rect.centery = HEIGHT/2
                self.speedx= -10
                self.speedy=0
            if self.rect.right < 0:
                self.rect.bottom = 0
                self.rect.centerx = WIDTH/2
                self.speedx=0
                self.speedy= 10
            if self.rect.top > HEIGHT:
                self.rect.right = 0
                self.rect.centery = HEIGHT/2
                self.speedx = 10
                self.speedy = 0

        # circling
        if self.circling:
            if self.rect.center[0] > WIDTH/2:
                self.do_Circle = True
            if self.do_Circle:
                if self.ang < 360:
                    rad = self.ang * math.pi / 180
                    self.rect.centery = -math.sin(rad) * 25 + self.rect.centery
                    self.rect.centerx = math.cos(rad) * 25 + self.rect.centerx
                    self.ang += 20
                    self.speedx = 0
                    self.speedy = 0
                else:
                    self.do_Circle = False
                    self.speedx = 10
                    self.speedy = -10
        if (self.rect.bottomleft[0] > WIDTH) and (self.rect.bottomleft[1] < 0):
            self.rect.bottomright = (0, 0)
            self.speedx = 10
            self.speedy = 10
            self.ang = 0

        # bordering
        if self.boardering:
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
                self.speedx = 0
                self.speedy = -10
            if self.rect.top < 0:
                self.rect.top = 0
                self.speedx = -10
                self.speedy = 0
            if self.rect.left < 0:
                self.rect.left = 0
                self.speedx = 0
                self.speedy = 10
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
                self.speedx = 10
                self.speedy = 0

        # Bouncing
        if self.bounceing:
            if self.rect.right>=WIDTH or self.rect.left<=0:
                self.speedx = self.speedx*-1
            if self.rect.top<=0 or self.rect.bottom >= HEIGHT:
                self.speedy = self.speedy*-1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = WIDTH/2,HEIGHT/2
        self.speedx = 0
        self.speedy = 0


    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy


# initialize pygame and create window
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(title)

clock = pygame.time.Clock()

# sprite Groups
all_sprites = pygame.sprite.Group()
players_group = pygame.sprite.Group()
mobs_group = pygame.sprite.Group()


#create Game objects
npc = Npc()
player = Player()

#add objects to sprite groups
mobs_group.add(npc)
players_group.add(player)
all_sprites.add(npc)
all_sprites.add(player)

running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input
    for event in pygame.event.get():
        if REGMOVEMENT:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.speedx += -5
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.speedx += 5
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.speedy += -5
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.speedy += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.speedy = 0
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.speedy = 0
        if GRIDMOVEMENT:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.rect.x += -50
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.rect.x += 50
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.rect.y += -50
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.rect.y += 50


        if event.type == pygame.QUIT:
            running = False


    # update every thing
    all_sprites.update()


    # render all changes
    screen.fill(GREEN)
    all_sprites.draw(screen)


    pygame.display.flip()



