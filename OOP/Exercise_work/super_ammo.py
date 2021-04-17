# File name: super_ammo
# Author: Pekka Lehtola
# Description: super ammo used for ammo power ups.

from config import *
import pygame
from random import randint
from ammo import Ammo


class Ammo_power_up(pygame.sprite.Sprite):

    def __init__(self):
        super(Ammo_power_up, self).__init__()
        self.surf = pygame.image.load("images/super_ammo.png")
        self.surf.set_colorkey(GREEN_SCREEN)
        self.rect = self.surf.get_rect()

    # Creates new power up into random location in screen.
    # Adds it to the list of all ammo power ups.
    def add_power_up(self, super_ammo_power_up_list):

        self.rect.centerx = randint(300, 1620)
        self.rect.centery = randint(510, 1000)

        super_ammo_power_up_list.append(self)

    # Updates power up into the screen.
    def show_power_up(self, screen):

        screen.blit(self.surf, self.rect)

    # Sets up Character ammo list as empty.
    # Adds super ammo to ammo list
    def super_pickup(self, indian, cowboy):

        if self.rect.colliderect(cowboy.rect):

            self.rect.x = 2200
            self.kill()

            cowboy.ammo = []
            cowboy.reload_img = False
            cowboy.reloaded = True
            for ammo in range(0, 1):
                ammo = Ammo("images/bullet.png", "bullet")
                ammo.surf = pygame.image.load("images/bullet.png")
                ammo.surf = pygame.transform.scale(pygame.image.load("images/bullet.png"),
                                                   (BULLET_X * BULLET_MULTIPLIER, BULLET_Y * BULLET_MULTIPLIER))
                ammo.surf.set_colorkey(GREEN_SCREEN)
                ammo.rect = ammo.surf.get_rect()
                ammo.super = True

                cowboy.ammo.append(ammo)

        if self.rect.colliderect(indian.rect):

            self.rect.x = 2200
            self.kill()

            indian.ammo = []
            indian.reload_img = False
            indian.reloaded = True

            for ammo in range(0, 1):
                ammo = Ammo("images/arrow.png", "arrow")
                ammo.surf = pygame.image.load("images/arrow.png")
                ammo.surf = pygame.transform.scale(pygame.image.load("images/arrow.png"),
                                                   (ARROW_X * ARROW_MULTIPLIER, ARROW_Y * ARROW_MULTIPLIER))
                ammo.surf.set_colorkey(GREEN_SCREEN)
                ammo.rect = ammo.surf.get_rect()
                ammo.super = True

                indian.ammo.append(ammo)
