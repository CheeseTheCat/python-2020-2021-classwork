import pygame as pg
from settings import *
from random import randint, random
vec = pg.math.Vector2

def collide_with_paddle(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False)
        if hits:
            if hits[0].rect.centerx > sprite.rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.rect.width / 2
            if hits[0].rect.centerx < sprite.rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.rect.width / 2
            sprite.vel.x *= -1.09
            sprite.rect.centerx = sprite.pos.x
            sprite.vel.y += hits[0].vel.y / 1.8
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
    def __init__(self, game):
        self.groups = game.all_sprites, game.player_group1, game.players
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((20, 150))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT / 2
        self.vel = vec(0, 0)
        self.pos = vec(self.rect.centerx, self.rect.centery)
        self.lives = 3

    def update(self):
        if self.vel.y > 400:
            self.vel.y = 400
        if self.vel.y < -400:
            self.vel.y = -400

        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.vel.y += -100
        if keystate[pg.K_s]:
            self.vel.y += 100

        if self.vel.y > 0:
            self.vel.y += -50
        if self.vel.y < 0:
            self.vel.y += 50

        if self.pos.y - self.rect.height/2 < 0:
            self.vel.y = 0
            self.pos.y += 1
        if self.pos.y + self.rect.height/2 > HEIGHT:
            self.vel.y = 0
            self.pos.y += -1

        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt

        if self.lives >= 3:
            self.image.fill(GREEN)
        elif self.lives == 2:
            self.image.fill(YELLOW)
        else:
            self.image.fill(RED)

    def looselife(self):
        self.lives += -1
        if self.lives <= 0:
            self.game.winner = "Player 2"
            self.game.playing = False


class Player2(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.player_group1, game.players
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((20, 150))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.centery = HEIGHT / 2
        self.vel = vec(0, 0)
        self.pos = vec(self.rect.centerx, self.rect.centery)
        self.lives = 3

    def update(self):
        if self.vel.y > 400:
            self.vel.y = 400
        if self.vel.y < -400:
            self.vel.y = -400

        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.vel.y += -100
        if keystate[pg.K_DOWN]:
            self.vel.y += 100

        if self.vel.y > 0:
            self.vel.y += -50
        if self.vel.y < 0:
            self.vel.y += 50

        if self.pos.y - self.rect.height/2 < 0:
            self.vel.y = 0
            self.pos.y += 1
        if self.pos.y + self.rect.height/2 > HEIGHT:
            self.vel.y = 0
            self.pos.y += -1

        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt

        if self.lives >= 3:
            self.image.fill(GREEN)
        elif self.lives == 2:
            self.image.fill(YELLOW)
        else:
            self.image.fill(RED)

    def looselife(self):
        self.lives += -1
        if self.lives <= 0:
            self.game.winner = "Player 1"
            self.game.playing = False

class Ball(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.ball_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((20, 20))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.hit_rect = BALL_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(-200, randint(-50, 50))
        self.pos = vec(self.rect.centerx, self.rect.centery)

    def update(self):
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.rect.centerx = self.pos.x
        collide_with_paddle(self, self.game.players, 'x')
        self.rect.centery = self.pos.y
        collide_with_paddle(self, self.game.players, 'y')
        if self.pos.y - self.rect.height/2 < 0:
             self.vel.y *= -1
        if self.pos.y + self.rect.height/2 > HEIGHT:
            self.vel.y *= -1
        self.hit_score()


    def hit_score(self):
        if self.pos.x < -200: # Player 1 side
            self.pos = vec(WIDTH / 2, HEIGHT / 2)
            self.vel = vec(-200, randint(-50, 50))
            self.game.player1.looselife()
        if self.pos.x > WIDTH + 200: # player 2 side
            self.pos = vec(WIDTH / 2, HEIGHT / 2)
            self.vel = vec(200, randint(-50, 50))
            self.game.player2.looselife()