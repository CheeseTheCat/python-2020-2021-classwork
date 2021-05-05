import pygame as pg
import random
import os
vec = pg.math.Vector2

# setup folder Assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")
snd_folder = os.path.join(game_folder,"snd")

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


WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "Tiles"
BGCOLOR = DARKGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

PLAYER_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_ROT_SPEED = 250
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 11)
PLAYER_HEALTH = 100

WALL_IMG = 'tile_196.png'

MOB_IMG = 'zoimbie1_hold.png'
MOB_SPEEDS = [150, 100, 75, 125, 150, 175, 150, 125]
MOB_HIT_RECT = pg.Rect(0,0, 30, 30)
MOB_HEALTH = 100
MOB_DMG = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50

BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1200
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DMG = 10

MUZZLE_FLASHES = ["muzzle_00.png","muzzle_01.png","muzzle_02.png","muzzle_03.png","muzzle_04.png",
                  "muzzle_05.png","muzzle_06.png","muzzle_01.png","muzzle_02.png","muzzle_03.png",
                  "muzzle_04.png","muzzle_05.png","muzzle_06.png"]
FLASH_DURATION = 40

WALL_LAYER = 1
ITEMS_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4

ITEM_IMAGES = {'health': 'medkit.png'}