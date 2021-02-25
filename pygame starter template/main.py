import pygame
import random

HEIGHT = 360
WIDTH = 480
FPS = 30
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

# game Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 10
        self.speedy = 0
        self.screenwrap = False
        self.loopwrap = True
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

        if self.loopwrap:
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
player = Player()
players_group.add(player)

#add objects to sprite groups
all_sprites.add(player)

running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # update every thing
    all_sprites.update()


    # render all changes
    screen.fill(GREEN)
    all_sprites.draw(screen)


    pygame.display.flip()



