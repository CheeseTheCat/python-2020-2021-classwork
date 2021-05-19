# Sprite classes for game
import pygame as pg
from settings import *
vec = pg.math.Vector2


def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, )
        if hits:
            if hits[0].rect.centerx > sprite.rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.rect.width / 2
            if hits[0].rect.centerx < sprite.rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.rect.width / 2
            sprite.vel.x = 0
            sprite.rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False)
        if hits:
            if hits[0].rect.centery > sprite.rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.rect.height / 2
            if hits[0].rect.centery < sprite.rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.rect.height / 2
            sprite.vel.y = 0
            sprite.rect.centery = sprite.pos.y



class Player1(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.player_group1
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.spawnx = self.x
        self.spawny = self.y
        self.pos = vec(self.x, self.y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.lives = 1

    def send_to_spawn(self):
        self.pos.x = self.spawnx
        self.pos.y = self.spawny

    def loose(self):
        self.lives += -1
        if self.lives <= 0:
            self.game.winner = "Player 2"
            self.game.playing = False


    def jump(self):
        self.vel.y = -3


    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        if self.vel.y > 2.5:
            self.vel.y = 2.5
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x += -PLAYER_ACC
        if keys[pg.K_d]:
            self.acc.x += PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH + self.rect.width / 2:
            self.pos.x = 0 - self.rect.width / 2
        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x = WIDTH + self.rect.width / 2

        if self.pos.y - TILESIZE < 0:
            self.vel.y = 10
        self.rect.midbottom = self.pos

        self.rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')

class Player2(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.player_group2
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.spawnx = self.x
        self.spawny = self.y
        self.pos = vec(self.x, self.y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.lives = 1

    def send_to_spawn(self):
        self.pos.x = self.spawnx
        self.pos.y = self.spawny

    def jump(self):
        self.vel.y = -3

    def loose(self):
        self.lives += -1
        if self.lives <= 0:
            self.game.winner = "Player 1"
            self.game.playing = False

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        if self.vel.y > 2.5:
            self.vel.y = 2.5
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x += -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x += PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH + self.rect.width / 2:
            self.pos.x = 0 - self.rect.width / 2
        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x = WIDTH + self.rect.width / 2

        if self.pos.y - TILESIZE < 0:
            self.vel.y = 10
        self.rect.midbottom = self.pos

        self.rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')



class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE