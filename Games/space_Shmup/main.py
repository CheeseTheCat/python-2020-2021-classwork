#################################################
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
animation_folder = path.join(imgs_folder, "animations")
player_animation_folder = path.join(animation_folder,"player_animation")
npc_animation_folder = path.join(animation_folder,"npc_animation")
pow_folder = path.join(imgs_folder, "powerups")
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
POWERUP_TIME = 10000


title = "Shmup"
font_name = pg.font.match_font("arial")
powerUps_list = ["gun","sheild"]
powerUps_chance = ["gun","sheild","sheild","sheild"]

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

def draw_lives(surf,x,y,lives,img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x+30*i
        img_rect.y = y
        surf.blit(img,img_rect)

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "SHMUP!", 64, WIDTH / 2, HEIGHT / 4, WHITE)
    draw_text(screen, "Use Arrow keys or WASD to move, Space to fire", 22,
              WIDTH /2, HEIGHT/2, WHITE)
    draw_text(screen, "Press a key to begin", 18, WIDTH /2, HEIGHT *3/4, WHITE)
    pg.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYUP:
                waiting = False
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
        self.lives = 3
        self.hid_timer = pg.time.get_ticks()
        self.hidden = False
        self.power_level = 1
        self.pow_timer = pg.time.get_ticks()

    def update(self):
        # time out power ups
        if self.power_level >= 2 and pg.time.get_ticks() - self.pow_timer > POWERUP_TIME:
            self.power_level -= 1
            self.pow_timer = pg.time.get_ticks()

        # unhide if hidden
        if self.hidden and pg.time.get_ticks() - self.hid_timer > 3000:
            self.hidden = False
            self.rect.bottom = (HEIGHT - (HEIGHT*.04))
            self.rect.centerx = (WIDTH / 2)
            self.sheild = 100

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
        if keystate[pg.K_g] and not self.hidden:
            self.shootfast()
        if keystate[pg.K_SPACE] and not self.hidden:
            self.shoot()

        self.rect.x += self.speedx
        #self.rect.y += self.speedy

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT and self.rect.bottom <= HEIGHT + 100:
            self.rect.bottom = HEIGHT

    def hide(self):
        # hide the player temporarily
        self.lives -= 1
        self.hidden = True
        self.hid_timer = pg.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)


    def shoot(self):
        now = pg.time.get_ticks()
        if now-self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power_level == 1:
                b = Bullet(self.rect.centerx,self.rect.top+1)
                all_sprites.add(b)
                bullet_group.add(b)
                shoot_snd.play()
            elif self.power_level == 2:
                b1 = Bullet(self.rect.left, self.rect.top + 1)
                b2 = Bullet(self.rect.right, self.rect.top + 1)
                all_sprites.add(b1)
                bullet_group.add(b1)
                all_sprites.add(b2)
                bullet_group.add(b2)
                shoot_snd.play()
            elif self.power_level >= 3:
                b1 = Bullet(self.rect.left, self.rect.top + 1)
                b1.inc_spread(-2)
                b2 = Bullet(self.rect.right, self.rect.top + 1)
                b2.inc_spread(2)
                b3 = Bullet(self.rect.centerx, self.rect.top + 1)
                all_sprites.add(b1)
                bullet_group.add(b1)
                all_sprites.add(b2)
                bullet_group.add(b2)
                all_sprites.add(b3)
                bullet_group.add(b3)
                shoot_snd.play()

    def shootfast(self):
        if self.power_level == 1:
            b = Bullet(self.rect.centerx, self.rect.top + 1)
            all_sprites.add(b)
            bullet_group.add(b)
            shoot_snd.play()
        elif self.power_level == 2:
            b1 = Bullet(self.rect.left, self.rect.top + 1)
            b2 = Bullet(self.rect.right, self.rect.top + 1)
            all_sprites.add(b1)
            bullet_group.add(b1)
            all_sprites.add(b2)
            bullet_group.add(b2)
            shoot_snd.play()
        elif self.power_level >= 3:
            b1 = Bullet(self.rect.left, self.rect.top + 1)
            b1.inc_spread(-2)
            b2 = Bullet(self.rect.right, self.rect.top + 1)
            b2.inc_spread(2)
            b3 = Bullet(self.rect.centerx, self.rect.top + 1)
            all_sprites.add(b1)
            bullet_group.add(b1)
            all_sprites.add(b2)
            bullet_group.add(b2)
            all_sprites.add(b3)
            bullet_group.add(b3)
            shoot_snd.play()

    def sheilds_up(self,num):
        self.sheild += num
        if self.sheild >= 100:
            self.sheild = 100

    def gun_powerup(self):
        self.power_level += 1
        self.pow_timer = pg.time.get_ticks()

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
        self.spread = 0

    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.spread
        # kill bullet when bottom leaves screen
        if self.rect.bottom < 0:
            self.kill()

    def inc_spread(self,num):
        self.spread = num

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
            spwn_chance = r.randint(0,50)
            if spwn_chance >=49:
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

class Explosion(pg.sprite.Sprite):
    def __init__(self,center,size):
        super(Explosion, self).__init__()
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Powerup(pg.sprite.Sprite):
    def __init__(self,center):
        super(Powerup, self).__init__()
        self.type = r.choice(powerUps_chance)
        self.image = pows_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()

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
player_mini_img = pg.transform.scale(player_img,(25,19))
player_mini_img.set_colorkey(BLACK)

# npc img
npc_img = pg.image.load(path.join(enemy_img_folder, "enemy1.png"))

# bullet img
bullet_img = pg.image.load(path.join(player_img_folder, "orange_lazer.png"))

# explostions
explosion_anim = {}
explosion_anim["lg"] = []
explosion_anim["sm"] = []
explosion_anim["player"] = []
for i in range(0,9):
    fn = "regularExplosion0{}.png".format(i)
    img = pg.image.load(path.join(npc_animation_folder,fn)).convert()
    img.set_colorkey(BLACK)
    img_lg = pg.transform.scale(img,(100,100))
    img_sm = pg.transform.scale(img, (40, 40))
    explosion_anim["lg"].append(img_lg)
    explosion_anim["sm"].append(img_sm)
    # adding player explosion
    fn = "sonicExplosion0{}.png".format(i)
    img = pg.image.load(path.join(player_animation_folder, fn)).convert()
    img.set_colorkey(BLACK)
    explosion_anim["player"].append(img)

# powerups
pows_images = {}
for i in range(len(powerUps_list)):
    fn = "img_{}.png".format(i)
    pows_images[powerUps_list[i]] = pg.image.load(path.join(pow_folder,fn)).convert()


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
pow_group = pg.sprite.Group()

#######################################################################################################################


# Game Loop
#######################################################################################################################
Playing = True
game_over = True
#########################################
while Playing:
    if game_over:
        show_go_screen()
        game_over = False
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

        for i in pow_group:
            all_sprites.add(i)
        #######################################################################################################################

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
        exlp = Explosion(hit.rect.center, "sm")
        all_sprites.add(exlp)
        if player.sheild <= 0:
            player.sheild = 0
            death_expl = Explosion(player.rect.center,"player")
            all_sprites.add(death_expl)
            player.hide()
            if player.lives <= 0 : # and not death_expl.alive: need to fix
                game_over = True


    # bullet hits npc
    hits = pg.sprite.groupcollide(npc_group,bullet_group,True,True)
    for hit in hits:
        score += 50 - hit.radius
        exlp = Explosion(hit.rect.center, "lg")
        all_sprites.add(exlp)
        npc.spwn()
        r.choice(expl_sounds).play()
        pow_chance = r.random()
        if pow_chance >= .90:
            pow = Powerup(hit.rect.center)
            pow_group.add(pow)
            all_sprites.add(pow)

    # pow hits player
    hits = pg.sprite.spritecollide(player, pow_group, True, pg.sprite.collide_circle)
    for hit in hits:
        if hit.type == "sheild":
            num = r.randint(15,50)
            player.sheilds_up(num)
        elif hit.type == "gun":
            player.gun_powerup()


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
    draw_lives(screen, WIDTH-100, 10, player.lives, player_mini_img)

    pg.display.flip()

#########################################

pg.quit()
#######################################################################################################################