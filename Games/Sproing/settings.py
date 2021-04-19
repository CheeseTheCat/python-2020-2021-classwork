import pygame as pg
import random
import os

# setup folder Assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")
snd_folder = os.path.join(game_folder,"snd")


HEIGHT = 600
WIDTH = 480
FPS = 45
title = "Sproing"
FONT_NAME = "arial"
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

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
DARKISHGREEN = (45, 150, 15)


# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 60),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4 - 50),
                 (125, HEIGHT - 350),
                 (350, 200),
                 (175, 100)]

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20
PLAYER_LAYER = 2

# Game Properties
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLATFORM_LAYER = 1
POW_LAYER = 2
MOB_LAYER = 2
CLOUD_LAYER = 0

