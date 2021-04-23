import pygame as pg
WIDTH = 1000
HEIGHT = 800
FPS = 60
TITLE = "4 vs 8 way movment"

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
DARKGREY = (40,40,40)
LIGHTGREY = (100,100,100)


class Player(pg.sprite.Sprite):
    def __init__(self,x,y):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vx,self.vy = 0,0

    def update(self, dt):
        self.vx,self.vy = 200*dt,0
        keystate = pg.key.get_pressed()
        # sum = 0
        # for i in keystate:
        #     sum += i
        # if sum <= 1:
        # if keystate[pg.K_UP]:
        #     self.vy += -5
        # if keystate[pg.K_DOWN]:
        #     self.vy += 5
        # if keystate[pg.K_LEFT]:
        #     self.vx += -5
        # if keystate[pg.K_RIGHT]:
        #     self.vx += 5

        # if self.vx != 0 and self.vy != 0:
        #     self.vx /= 1.4142
        #     self.vy /= 1.4142


        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH



pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Player(WIDTH/2, HEIGHT/2)
all_sprites.add(player)


running = True
while running:

    dt = clock.tick(FPS)/1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_sprites.update(dt)

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pg.display.flip()

pg.quit()