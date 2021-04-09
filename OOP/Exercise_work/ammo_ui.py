# File name: ammo_ui
# Author: Pekka Lehtola
# Description: Used for showing ammo elements in the screen.

import pygame
from config import *
import time
from ui import Ui

class Ammo_ui(Ui):
    def __init__(self, image):

        super(Ammo_ui, self).__init__(image)
        self.reload_list = ["images/circle1.png", "images/circle2.png", "images/circle3.png", "images/circle4.png"]
        # Used for characters reload animation.
        self.counter = 0

    # Shows every ammo that character has in ammo list
    def show_ammo(self, character, screen):

        y = 10

        if character.name == "Cowboy":

            x = 60

            for ammo in character.ammo:
                ammo.rect.y = y
                ammo.rect.x = x
                screen.blit(ammo.surf, ammo.rect)

                x += 30

        if character.name == "Indian":

            x = 1826

            for ammo in character.ammo:
                ammo.rect.y = y
                ammo.rect.x = x
                screen.blit(ammo.surf, ammo.rect)

                x -= 70

    # When character is reloading, shows reload animation.
    def show_reload(self, character, screen):

        if character.reload_img == True:

            if character.name == "Indian":

                self.surf = pygame.image.load(self.reload_list[int(self.counter)])
                self.surf.set_colorkey(GREEN_SCREEN)
                self.rect.y = -5
                self.rect.x = 1810
                screen.blit(self.surf, self.rect)
                self.counter += 0.2
                if self.counter >= 3.9:
                    self.counter = 0

            if character.name == "Cowboy":

                self.surf = pygame.image.load(self.reload_list[int(self.counter)])
                self.surf.set_colorkey(GREEN_SCREEN)
                self.rect.y = -5
                self.rect.x = 44
                screen.blit(self.surf, self.rect)
                self.counter += 0.2
                if self.counter >= 3.9:
                    self.counter = 0