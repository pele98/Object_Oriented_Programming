# File name: ui
# Author: Pekka Lehtola
# Description: User interface class. Used for showing different elements in screen.

import pygame
from config import *
import time



class Ui(pygame.sprite.Sprite):

    def __init__(self, image):
        super(Ui, self).__init__()
        self.surf = pygame.image.load(image)
        self.surf.set_colorkey(GREEN_SCREEN)
        self.rect = self.surf.get_rect()

        #Used for reload animations.
        self.counter = 0
        self.reload_list = ["images/circle1.png", "images/circle2.png", "images/circle3.png", "images/circle4.png"]

    # Sets 4 hearts for each player.
    def set_up_hearts(self, character):

        for heart in range(0, 4):
            heart = Ui("images/hearth_1.png")
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

    # Shows every ammo that character has in ammo list.
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

    ### WORK IN PROGRESS ###

    # In the start of the game shows count down
    def game_start(self, ONE, TWO, THREE, screen):

        self.rect.x = SCREEN_SIZE_HOR / 2
        self.rect.y = SCREEN_SIZE_VER / 2

        self.surf = ONE
        self.surf.set_colorkey(GREEN_SCREEN)
        screen.blit(self.surf, self.rect)
        pygame.display.flip()
        time.sleep(1)

        self.surf = TWO
        self.surf.set_colorkey(GREEN_SCREEN)
        screen.blit(self.surf, self.rect)
        pygame.display.flip()
        time.sleep(1)

        self.surf = THREE
        self.surf.set_colorkey(GREEN_SCREEN)
        screen.blit(self.surf, self.rect)
        pygame.display.flip()
        time.sleep(1)

    # Will be used to show the winner.
    #def game_end(self):
