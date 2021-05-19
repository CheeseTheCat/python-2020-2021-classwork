import pygame as pg
from settings import *


class Player1(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.player_group1
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((20, 150))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT / 2
        self.speedy = 0

    def update(self):
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.speedy += -5
        if keystate[pg.K_s]:
            self.speedy += 5
        self.rect.y += self.speedy

class Player2(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.player_group1
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((20, 150))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.centery = HEIGHT / 2
        self.speedy = 0

    def update(self):
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.speedy += -5
        if keystate[pg.K_DOWN]:
            self.speedy += 5
        self.rect.y += self.speedy

class Ball(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.ball_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2