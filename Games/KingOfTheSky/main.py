import pygame as pg
import sys
from os import path
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player_group1 = pg.sprite.Group()
        self.player_group2 = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == 'w':
                    Wall(self, col, row)
                if tile == '1':
                    self.player1 = Player1(self, col, row)
                if tile == '2':
                    self.player2 = Player2(self, col, row)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

        hits = pg.sprite.spritecollide(self.player1, self.player_group2, False)
        if hits:
            winner = ''
            if self.player1.pos.y < self.player2.pos.y:
                winner = 'player1'
            if self.player2.pos.y < self.player1.pos.y:
                winner = 'player2'

            if winner == 'player1':
                self.player1.vel *= -1
                self.player2.vel *= -1
                self.player2.vel.y *= 3
            elif winner == 'player2':
                self.player1.vel.y *= 3






    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.player1.jump()
                    if event.key == pg.K_UP:
                        self.player2.jump()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()