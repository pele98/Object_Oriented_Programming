# File name: character
# Author: Pekka Lehtola
# Description:

import pygame
from config import *

class Ammo(pygame.sprite.Sprite):

    def __init__(self, ammo, name):
        super(Ammo, self).__init__()
        self.name = name
        self.surf = pygame.image.load(ammo)
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

        self.shot = False



