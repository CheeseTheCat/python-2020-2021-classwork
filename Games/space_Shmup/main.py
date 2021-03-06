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

    def update(self):
        self.rect.x += self.speedx

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0

class Npc(pg.sprite.Sprite):
    def __init__(self):
        super(Npc, self).__init__()
        self.image = pg.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2)
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
            if spwn_chance >=1:
                spwn_new_Npc()

def spwn_new_Npc():
    newnpc = Npc()
    newnpc.rect.centerx = r.randint(30, (WIDTH - 30))
    newnpc.speedy = 5
    all_sprites.add(newnpc)
    npc_group.add(newnpc)
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

#######################################################################################################################

# create game objects
#######################################################################################################################
player = Player()
npc = Npc()
#######################################################################################################################

# add objects to sprite groups
#######################################################################################################################
players_group.add(player)
npc_group.add(npc)

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
            if event.key == pg.K_ESCAPE:
                Playing = False
        if event.type == pg.QUIT:
            Playing = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d or event.key == pg.K_RIGHT:
                player.speedx += 5
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                player.speedx += -5
        if event.type == pg.KEYUP:
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                player.speedx += 5
            if event.key == pg.K_d or event.key == pg.K_RIGHT:
                player.speedx += -5

    #########################

    # updates
    #########################
    all_sprites.update()

    #########################

    # render changes
    #########################
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pg.display.flip()

#########################################

pg.quit()
#######################################################################################################################