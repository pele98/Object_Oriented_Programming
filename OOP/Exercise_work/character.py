# File name: character
# Author: Pekka Lehtola
# Description:

import pygame
from config import *
from ammo import *

class Character(pygame.sprite.Sprite):

    def __init__(self, sprite, name):
        super(Character, self).__init__()
        self.name = name
        self.surf = pygame.image.load(sprite)
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(size=(40,114), center=(0, 0))
        self.ammo = []

    def reload(self):

        if self.name == "indian":

            for ammo in range(0,2):

                ammo = Ammo("images/arrow.gif", "arrow")

                self.ammo.append(ammo)

        if self.name == "cowboy":

            for ammo in range(0,5):

                ammo = Ammo("images/bullet.gif", "bullet")

                self.ammo.append(ammo)

    def move(self, pressed_keys):

        if self.name == "Indian":

            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -MOVEMENT_SPEED)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, MOVEMENT_SPEED)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-MOVEMENT_SPEED, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(MOVEMENT_SPEED, 0)

        if self.name == "Cowboy":

            if pressed_keys[K_w]:
                self.rect.move_ip(0, -MOVEMENT_SPEED)
            if pressed_keys[K_s]:
                self.rect.move_ip(0, MOVEMENT_SPEED)
            if pressed_keys[K_a]:
                self.rect.move_ip(-MOVEMENT_SPEED, 0)
            if pressed_keys[K_d]:
                self.rect.move_ip(MOVEMENT_SPEED, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_SIZE_HOR:
            self.rect.right = SCREEN_SIZE_HOR
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_SIZE_VER:
            self.rect.bottom = SCREEN_SIZE_VER


indian = Character("images/indian.png", "Indian")
cowboy = Character("images/cowboy.png", "Cowboy")

all_sprites = pygame.sprite.Group()
all_sprites.add(indian)
all_sprites.add(cowboy)