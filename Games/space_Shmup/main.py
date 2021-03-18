import pygame as pg
import random as r
import math
from os import *

# code created by James Hooper
# art creatged by James hooper
# background created by Cuzco, image taken from https://opengameart.org/content/space-background

# folder stuff
#################################################
game_folder = path.dirname(__file__)
imgs_folder = path.join(game_folder,"imgs")
snds_folder = path.join(game_folder, "snds")
scores_folder = path.join(game_folder, "highscores")
# images
player_img_folder = path.join(imgs_folder, "player_imgs")
enemy_img_folder = path.join(imgs_folder, "enemy_imgs")
background_folder = path.join(imgs_folder, "backgrounds")

#################################################

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
font_name = pg.font.match_font("arial")

#######################################################################################################################

# Game functions
#######################################################################################################################
def draw_text(surf,text,size,x,y,color):
    font = pg.font.Font(font_name,size)
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface,text_rect)

def drawbar(surf,x,y,pct):
    if pct <0:
        pct = 0
    bar_len = 200
    bar_height = 40
    fill = (pct/100)*bar_len
    outline_rect = pg.Rect(x,y,bar_len,bar_height)
    fill_rect = pg.Rect(x,y,fill,bar_height)
    pg.draw.rect(surf,GREEN,fill_rect)
    pg.draw.rect(surf,WHITE,outline_rect,2)
#######################################################################################################################

# Game object classes
#######################################################################################################################
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.sheild = 100
        # self.image = pg.Surface((50,40))
        # self.image.fill(GREEN)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(player_img,(50,40))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 2 * 0.95)
        # pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = (HEIGHT - (HEIGHT*.04))
        self.speedx = 0
        self.speedy = 0
        self.shoot_delay = 250
        self.last_shot = pg.time.get_ticks()


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

        # un comment this for insta fire
        if keystate[pg.K_g]:
            self.shootfast()
        if keystate[pg.K_SPACE]:
            self.shoot()

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
        now = pg.time.get_ticks()
        if now-self.last_shot > self.shoot_delay:
            self.last_shot = now
            b = Bullet(self.rect.centerx,self.rect.top+1)
            all_sprites.add(b)
            bullet_group.add(b)
            shoot_snd.play()

    def shootfast(self):
        b = Bullet(self.rect.centerx,self.rect.top+1)
        all_sprites.add(b)
        bullet_group.add(b)
        shoot_snd.play()

class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet, self).__init__()
        # self.image = pg.Surface((10,30))
        # self.image.fill(CYAN)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(bullet_img, (10, 30))
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
        self.randsize = r.randint(20,70)
        self.image = npc_img
        self.image_orig = pg.transform.scale(npc_img, (self.randsize, self.randsize))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width/2 * 0.70)
        # pg.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.centerx = r.randint(30,(WIDTH-30))
        self.rect.bottom = (-1)
        self.speedx = 0
        self.speedy = r.randint(4,6)
        self.rot = 0
        self.rot_speed = r.randint(-8,8)
        self.last_update = pg.time.get_ticks()

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 60:
            self.last_update = now
            # do the rotation
            self.rot = (self.rot+self.rot_speed)%360
            new_image = pg.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):

        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.top >= HEIGHT:
            self.rect.bottom = -1
            self.rect.centerx = r.randint(30,(WIDTH-30))
            self.speedy = r.randint(4, 10)
            spwn_chance = r.randint(0,100)
            if spwn_chance >=100:
                self.spwn()
    def spwn(self):
        npc = Npc()
        npc_group.add(npc)
        all_sprites.add(npc)

class Star(pg.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.size = r.randint(1,5)
        self.image = pg.Surface((self.size, self.size))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = r.randint(0,(WIDTH))
        self.rect.top = (0)
        self.speedx = 0
        self.speedy = r.randint(4,7)



    def update(self):
        self.rect.y += self.speedy

        if self.rect.top >= HEIGHT:
            self.kill()
            # self.rect.bottom = -1
            # self.rect.centerx = r.randint(30,(WIDTH-30))
            # self.speedy = r.randint(4, 10)

    def spwnstar(self):
        star = Star()
        star_group.add(star)
        all_sprites.add(star)
#######################################################################################################################

# Initialize pygame and create window
#######################################################################################################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
score = 0

#######################################################################################################################

# load imgs
#######################################################################################################################
# background img
background = pg.image.load(path.join(background_folder, "background1.jpg")).convert()
background = pg.transform.scale(background,(WIDTH,HEIGHT))
background_rect = background.get_rect()

# player img
player_img = pg.image.load(path.join(player_img_folder, "player1_ship.png")).convert()

# npc img
npc_img = pg.image.load(path.join(enemy_img_folder, "enemy1.png"))

# bullet img
bullet_img = pg.image.load(path.join(player_img_folder, "orange_lazer.png"))

#######################################################################################################################
# load sounds

shoot_snd = pg.mixer.Sound(path.join(snds_folder,"pew.wav"))
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pg.mixer.Sound(path.join(snds_folder, snd)))

pg.mixer.music.load(path.join(snds_folder, "tgfcoder-FrozenJam-SeamlessLoop.ogg"))
pg.mixer.music.set_volume(0.4)
pg.mixer.music.play(loops=-1)
#######################################################################################################################

# create Sprite groups
#######################################################################################################################
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()
star_group = pg.sprite.Group()

#######################################################################################################################

# create game objects
#######################################################################################################################
player = Player()
for i in range(10):
    npc = Npc()
    npc_group.add(npc)
star = Star()

#######################################################################################################################

# add objects to sprite groups
#######################################################################################################################
players_group.add(player)
star_group.add(star)
# npc_group.add(npc)

for i in players_group:
    all_sprites.add(i)

for i in npc_group:
    all_sprites.add(i)

for i in star_group:
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
            # if event.key == pg.K_SPACE:
            #     player.shoot()
            if event.key == pg.K_ESCAPE:
                Playing = False
        if event.type == pg.QUIT:
            Playing = False


    #########################

    # updates
    #########################
    all_sprites.update()

    # if npc hits player
    hits = pg.sprite.spritecollide(player,npc_group,True, pg.sprite.collide_circle)
    for hit in hits:
        score += -100 - hit.radius
        npc.spwn()
        r.choice(expl_sounds).play()
        player.sheild -= hit.radius*2
        if player.sheild <= 0:
            player.sheild = 0
            Playing = False


    # bullet hits npc
    hits = pg.sprite.groupcollide(npc_group,bullet_group,True,True)
    for hit in hits:
        score += 50 - hit.radius
        npc.spwn()
        r.choice(expl_sounds).play()

    # randomly make stars
    starchance = r.randint(0,75)
    if starchance >= 60:
        star.spwnstar()

    #########################

    # render changes
    #########################
    screen.fill(BLACK)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    # draw hud
    draw_text(screen, "Score: "+str(score),18, WIDTH/2,10,WHITE)
    drawbar(screen, 5, 10, player.sheild)

    pg.display.flip()

#########################################

pg.quit()
#######################################################################################################################