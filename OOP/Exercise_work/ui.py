# File name: ui
# Author: Pekka Lehtola
# Description: Classes for user interface

import pygame
from config import *

# Healtclass

class Hearth(pygame.sprite.Sprite):

    def __init__(self):
        super(Hearth, self).__init__()
        self.surf = pygame.image.load("images/hearth_1.png").convert()
        self.surf.set_colorkey(GREEN_SCREEN)
        self.rect = self.surf.get_rect()


    def set_up_hearths(self, character):

        for heart in range(0, 4):
            heart = Hearth()
            character.healt.append(heart)

    def show_hearts(self, character, screen):

        y = 60

        if character.name == "Cowboy":

            x = 60

            for hearth in character.healt:

                hearth.rect.y = y
                hearth.rect.x = x
                screen.blit(hearth.surf, hearth.rect)

                x += 40

        if character.name == "Indian":

            x = 1826

            for hearth in character.healt:

                hearth.rect.y = y
                hearth.rect.x = x
                screen.blit(hearth.surf, hearth.rect)

                x -= 40



