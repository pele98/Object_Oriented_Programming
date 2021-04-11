# File name: hearth_ui
# Author: Pekka Lehtola
# Description: Used for showing hearth elements in the screen.

import pygame
from config import *
from ui import Ui


class Heart_ui(Ui):

    def __init__(self):
        super(Heart_ui, self).__init__("images/hearth_1.png")

        # Sets 4 hearts for each player.

    def set_up_hearts(self, character):

        for heart in range(0, 4):
            heart = Heart_ui()
            character.health.append(heart)

        # Draws hearts for each player into the screen.
        # Heart location is determined with character name

    def show_hearts(self, character, screen):

        # height location is the same for both characters
        y = 60

        # Cowboys hearts are located in left corner
        if character.name == "Cowboy":

            x = 60

            for hearth in character.health:
                hearth.rect.y = y
                hearth.rect.x = x
                screen.blit(hearth.surf, hearth.rect)

                x += 40

        # indians hearts are located in the right corner
        if character.name == "Indian":

            x = 1826

            for hearth in character.health:
                hearth.rect.y = y
                hearth.rect.x = x
                screen.blit(hearth.surf, hearth.rect)

                x -= 40




