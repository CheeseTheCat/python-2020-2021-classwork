import pygame
import random
import math
import os

# setup folder Assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"imgs")
sound_folder = os.path.join(game_folder,"sounds")
save_folder = os.path.join(game_folder, "saveData")
text_folder = os.path.join(game_folder, "textData")
sprites_folder = os.path.join(img_folder, "sprites")



HEIGHT = 450
WIDTH = 550
FPS = 45
title = "Template"
mousex=0
mousey=0
mouse_bttn_held = False

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

GRIDMOVEMENT = True
FLOMOVEMENT = False

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
        self.image = pygame.Surface((25, 25))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = WIDTH/2,HEIGHT/2
        self.speedx = 0
        self.speedy = 0
        self.keypressed = False


    def update(self):


        # if mouse_bttn_held:
        #     self.rect.center = (mousex,mousey)


        # self.speedx = 0
        # self.speedy = 0
        # keystate = pygame.key.get_pressed()
        # if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
        #     self.speedx = -5
        # if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
        #     self.speedx = 5
        # if keystate[pygame.K_UP] or keystate[pygame.K_w]:
        #     self.speedy = -5
        # if keystate[pygame.K_DOWN or keystate[pygame.K_s]]:
        #     self.speedy = 5
        #
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # # grid movment (Dosent work)
        # keystate = pygame.key.get_pressed()
        # if keystate[pygame.K_LEFT] or keystate[pygame.K_a] and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centerx+=-50
        # if keystate[pygame.K_RIGHT] or keystate[pygame.K_d] and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centerx += 50
        # if keystate[pygame.K_UP] or keystate[pygame.K_w] and self.keypressed == False :
        #     self.keypressed = True
        #     self.rect.centery += -50
        # if keystate[pygame.K_DOWN] or keystate[pygame.K_s] and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centery += 50

        # bind player to screen
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH

def spwn_new_player(x, y):
    newplayer = Player()
    newplayer.rect.center = (x, y)
    newplayer.speedx = random.randint(-10,10)
    newplayer.speedy = random.randint(-10,10)
    all_sprites.add(newplayer)
    players_group.add(newplayer)



# initialize pygame and create window
pygame.init()
pygame.mixer.init()

#load in game imagaes
# player_img = pygame.image.load(os.path.join(sprites_folder,"player.png")).convert()


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

    mousex,mousey = pygame.mouse.get_pos()
    # Process input
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN and player.rect.collidepoint(pygame.mouse.get_pos()):
            mouse_bttn_held = True
            spwn_new_player(mousex,mousey)
        if event.type == pygame.MOUSEBUTTONUP and mouse_bttn_held == True:
            mouse_bttn_held = False



    #     if FLOMOVEMENT:
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
    #                 player.speedx += -5
    #             if event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
    #                 player.speedx += 5
    #             if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_KP8:
    #                 player.speedy += -5
    #             if event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
    #                 player.speedy += 5
    #         if event.type == pygame.KEYUP:
    #             if event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_KP4 or event.key == pygame.K_KP6:
    #                 player.speedx = 0
    #             if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_KP8 or event.key == pygame.K_KP2:
    #                 player.speedy = 0
    #     if GRIDMOVEMENT:
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
    #                 player.rect.x += -50
    #             if event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
    #                 player.rect.x += 50
    #             if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_KP8:
    #                 player.rect.y += -50
    #             if event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
    #                 player.rect.y += 50
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


        if event.type == pygame.QUIT:
            running = False


    # update every thing
    all_sprites.update()


    # render all changes
    screen.fill(GREEN)
    all_sprites.draw(screen)


    pygame.display.flip()

pygame.quit()

