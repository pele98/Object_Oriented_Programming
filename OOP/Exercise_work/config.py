# File name: config
# Author: Pekka Lehtola
# Description: Config file for constant variables.

import pygame

SCREEN_SIZE_VER = 1080
SCREEN_SIZE_HOR = 1920

BULLET_VELOCITY = 30
MOVEMENT_SPEED = 10

SHOOTING_SPEED_COWBOY = 0.4
RELOAD_SPEED_COWBOY = 2

SHOOTING_SPEED_INDIAN = 0.3
RELOAD_SPEED_INDIAN = 0.9

BULLET_X = 20
BULLET_Y = 11

ARROW_X = 56
ARROW_Y = 19

BULLET_MULTIPLIER = 8
ARROW_MULTIPLIER = 6

SUPER_AMMO_DAMAGE = 3

cowboy_x = 57
cowboy_y = 129

indian_x = 64
indian_y = 116

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

COWBOY_STANDING = "images/updated_sprites/cowboy1.png"
COWBOY_LEFT = "images/updated_sprites/cowboy2.png"
COWBOY_RIGHT = "images/updated_sprites/cowboy3.png"

INDIAN_STANDING = "images/updated_sprites/indian1.png"
INDIAN_LEFT = "images/updated_sprites/indian2.png"
INDIAN_RIGHT = "images/updated_sprites/indian3.png"

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