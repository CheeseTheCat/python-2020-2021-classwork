# define some colors (R, G, B)
import pygame as pg
vec = pg.math.Vector2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)

# game settings
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "Definitely not Pong"
BGCOLOR = DARKGREY

BALL_HIT_RECT = pg.Rect(0, 0, 35, 35)

TITLE_FONT = 'arial'