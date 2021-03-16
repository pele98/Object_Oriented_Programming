# File name: config
# Author: Pekka Lehtola
# Description:

import pygame

FRAME_DURATION = int(1000 / 25)

SCREEN_SIZE_VER = 1080
SCREEN_SIZE_HOR = 1920

BULLET_VELOCITY = 100
MOVEMENT_SPEED = 10

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

BG = pygame.image.load("images/desert.png")

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
    KEYDOWN,
    QUIT,
)