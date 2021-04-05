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
        self.player_group = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()

        # create game objects
        self.player = Player()

        # add game objects to groups
        self.all_sprites.add(self.player)

        self.run()

        pass

    def run(self):
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

    def update(self):
        self.all_sprites.update()


    def draw(self):
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