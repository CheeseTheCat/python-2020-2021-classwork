import pygame as pg
import random
import os
from settings import *
from sprites import *

class Game(object):
    def __init__(self):
        self.running = True
        # initialize pygame and create window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()

    def new(self):
        # start a new game

        #create sprite groups
        self.all_sprites = pg.sprite.Group()
        self.platforms_group = pg.sprite.Group()

        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms_group.add(p)
        # create game objects
        self.player = Player(self)

        # add game objects to groups
        self.all_sprites.add(self.player)

        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE or event.key == pg.K_UP or event.key == pg.K_w:
                    self.player.jump()

    def update(self):
        self.all_sprites.update()

        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms_group, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        # if player reaches top 1/4 of screen

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_GO_screen(self):
        pass

    def load_img(self):
        pass

g = Game()

g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()


pg.quit()