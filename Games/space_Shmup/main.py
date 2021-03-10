import pygame as pg
import random as r
import math
from os import *

# Game constants
#######################################################################################################################
HEIGHT = 800
WIDTH = 600
FPS = 60

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


title = "Shmup"
total_npcs = 0

#######################################################################################################################

# Game object classes
#######################################################################################################################
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = (HEIGHT - (HEIGHT*.04))
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0

        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedx += -5
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx += 5
        # if keystate[pg.K_UP] or keystate[pg.K_w]:
        #     self.speedy += -5
        # if keystate[pg.K_DOWN] or keystate[pg.K_s]:
        #     self.speedy += 5
        # if keystate[pg.K_SPACE]:
        #     self.shoot()

        self.rect.x += self.speedx
        #self.rect.y += self.speedy

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        b = Bullet(self.rect.centerx,self.rect.top+1)
        all_sprites.add(b)
        bullet_group.add(b)

class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet, self).__init__()
        self.image = pg.Surface((10,30))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -10

    def update(self):
        self.rect.y += self.speed

        # kill bullet when bottom leaves screen
        if self.rect.bottom < 0:
            self.kill()


class Npc(pg.sprite.Sprite):
    def __init__(self):
        super(Npc, self).__init__()
        self.image = pg.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = r.randint(30,(WIDTH-30))
        self.rect.top = (0)
        self.speedx = 0
        self.speedy = r.randint(4,7)
        self.total_npcs = 1


    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.top >= HEIGHT:
            self.rect.bottom = -1
            self.rect.centerx = r.randint(30,(WIDTH-30))
            self.speedy = r.randint(4, 10)
            spwn_chance = r.randint(0,50)
            if spwn_chance >=48:
                self.spwn()
    def spwn(self):
        npc = Npc()
        npc_group.add(npc)
        all_sprites.add(npc)

#######################################################################################################################

# Initialize pygame and create window
#######################################################################################################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()

#######################################################################################################################

# load imgs
#######################################################################################################################

#######################################################################################################################

# create Sprite goups
#######################################################################################################################
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()

#######################################################################################################################

# create game objects
#######################################################################################################################
player = Player()
for i in range(10):
    npc = Npc()
    npc_group.add(npc)
#######################################################################################################################

# add objects to sprite groups
#######################################################################################################################
players_group.add(player)
# npc_group.add(npc)

for i in players_group:
    all_sprites.add(i)

for i in npc_group:
    all_sprites.add(i)

#######################################################################################################################

# Game Loop
#######################################################################################################################
Playing = True
#########################################
while Playing:
    # timing
    clock.tick(FPS)

    # collect input
    #########################
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.shoot()
            if event.key == pg.K_ESCAPE:
                Playing = False
        if event.type == pg.QUIT:
            Playing = False




    #########################

    # updates
    #########################
    all_sprites.update()

    # if npc hits player
    hits = pg.sprite.spritecollide(player,npc_group,True)
    if hits:
        npc.spwn()
        Playing = False

    # bullet hits npc
    hits = pg.sprite.groupcollide(npc_group,bullet_group,True,True)
    for hit in hits:
        npc.spwn()

    #########################

    # render changes
    #########################
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pg.display.flip()

#########################################

pg.quit()
#######################################################################################################################