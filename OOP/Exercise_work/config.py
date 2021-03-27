# File name: config
# Author: Pekka Lehtola
# Description: Config file for constant variables.

import pygame

FRAME_DURATION = 1/120

SCREEN_SIZE_VER = 1080
SCREEN_SIZE_HOR = 1920

BULLET_VELOCITY = 30
MOVEMENT_SPEED = 10

SHOOTING_SPEED_COWBOY = 0.4
RELOAD_SPEED_COWBOY = 2

SHOOTING_SPEED_INDIAN = 0.3
RELOAD_SPEED_INDIAN = 0.9

INF = 100**100

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

HEART = "34px"

# Green screen color is used to remove background from sprites.
GREEN_SCREEN = (0, 177, 64)

BG = pygame.image.load("images/desert.png")
ONE = pygame.image.load("images/11.png")
TWO = pygame.image.load("images/22.png")
THREE = pygame.image.load("images/33.png")
COWBOY_WINS = pygame.image.load("images/cowboy_wins.png")
INDIAN_WINS = pygame.image.load("images/indian_wins.png")

# Keyboard inputs are located here.
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_w,
    K_s,
    K_d,
    K_a,
    K_SPACE,
    K_j,
    K_k,
    K_r,
    KEYDOWN,
    QUIT,
)