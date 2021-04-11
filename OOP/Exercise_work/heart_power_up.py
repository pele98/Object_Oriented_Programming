# File name: hearth_power_up
# Author: Pekka Lehtola
# Description: Used for creating heart power ups in game.

from random import randint
from heart_ui import Heart_ui
from heart_ui import *

class Heart_power_up(Heart_ui):
    def __init__(self):
        super(Heart_power_up, self).__init__()
        self.surf = pygame.image.load("images/heart_gold.png")
        self.surf.set_colorkey(GREEN_SCREEN)


    def add_power_up(self, hearth_power_up_list):

        self.rect.centerx = randint(300, 1620)
        self.rect.centery = randint(510, 1000)

        hearth_power_up_list.append(self)

    def show_power_up(self, screen):

        screen.blit(self.surf, self.rect)

    def heart_pickup(self, indian, cowboy, heart):

        if self.rect.colliderect(cowboy.rect):
            cowboy.health.append(heart)
            self.rect.x = 2200
            self.kill()

        if self.rect.colliderect(indian.rect):
            indian.health.append(heart)
            self.rect.x = 2200
            self.kill()
