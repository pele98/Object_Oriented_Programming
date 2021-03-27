# File name: character
# Author: Pekka Lehtola
# Description: Character class that is derived from pygame sprites

import pygame
from config import *
from ammo import *

class Character(pygame.sprite.Sprite):

    def __init__(self, sprite, name):
        super(Character, self).__init__()
        self.name = name
        self.surf = pygame.image.load(sprite)                           # Surface image
        self.surf.set_colorkey(GREEN_SCREEN)                            # Defining see through color
        self.rect = self.surf.get_rect(size=(40,114), center=(0, 0))    # Sets up characters hitbox
        self.ammo = []                                                  # Reloaded ammo
        self.shot_ammo = []                                             # Ammo that character has shot
        self.reloaded = False
        self.reload_img = False
        self.shooting_speed = 0
        self.reload_speed = INF
        self.health = []

    # Reloading function

    def reload(self, pressed_keys, time):

        # Detects which player is reloading
        if self.name == "Indian":

            # Reload speed updates with timer and emptys ammo list so shooting while reload timer is on
            # is prevented
            if pressed_keys[K_k]:

                self.reload_speed = time + RELOAD_SPEED_INDIAN
                self.ammo = []
                self.reload_img = True

            # If timer is smaller than reload speed reload is set to True
            if self.reload_speed < time:
                self.reloaded = False
                self.reload_speed = INF # sets reload speed to INF to prevent automatic reloading.

            # Restarts reload speed and appends ammo to magazine.
            if self.reloaded == False:

                self.reload_img = False
                for ammo in range(0, 4):

                    ammo = Ammo("images/arrow.png", "arrow")    # Define which ammo is inserted.

                    self.ammo.append(ammo)

                self.reloaded = True


        # Cowboys reload function is indentical
        if self.name == "Cowboy":

            # Reload speed updates with timer and emptys ammo list so shooting while reload timer is on
            # is prevented
            if pressed_keys[K_r]:

                self.reload_speed = time + RELOAD_SPEED_COWBOY
                self.ammo = []
                self.reload_img = True

            # If timer is smaller than reload speed reload is set to True
            if self.reload_speed < time:
                self.reloaded = False
                self.reload_speed = INF  # sets reload speed to INF to prevent automatic reloading.

            # Restarts reload speed and appends ammo to magazine.
            if self.reloaded == False:

                self.reload_img = False

                for ammo in range(0, 6):

                    ammo = Ammo("images/bullet.png", "bullet")  # Define which ammo is inserted.

                    self.ammo.append(ammo)

                self.reloaded = True

    # Shooting function
    # Work similary to reload function with time delay using time.perf_counter.
    def shoot(self, pressed_keys, time):

        if self.name == "Cowboy":

            if pressed_keys[K_SPACE] and self.shooting_speed < time:

                self.shooting_speed = time + SHOOTING_SPEED_COWBOY

                if self.reloaded:

                    try:
                        ammo = self.ammo.pop(-1)        # Removes last ammo object from ammo list
                        self.shot_ammo.append(ammo)     # Adds that ammo to shot ammo list
                        ammo.rect.x = self.rect.x + 30  # Ammos initial location is players X
                        ammo.rect.y = self.rect.y + 63  # And Y coordinates
                        ammo.shot = True

                    except:

                        pass


        # Indians shooting function is identical
        if self.name == "Indian":

            if pressed_keys[K_j] and self.shooting_speed < time:

                self.shooting_speed = time + SHOOTING_SPEED_INDIAN

                try:

                    ammo = self.ammo.pop(-1)
                    self.shot_ammo.append(ammo)
                    ammo.rect.x = self.rect.x - 30
                    ammo.rect.y = self.rect.y + 50
                    ammo.shot = True

                except:

                    pass


    # Moving function
    def move(self, pressed_keys):

        # Detects keyboard inputs and calculates new location for character.
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

        # Detects if character has reached levels edges and stops them moving off the screen.
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_SIZE_HOR:
            self.rect.right = SCREEN_SIZE_HOR
        if self.rect.top <= 380:
            self.rect.top = 380
        if self.rect.bottom >= SCREEN_SIZE_VER:
            self.rect.bottom = SCREEN_SIZE_VER

    ### WORK IN PROGRESS ###
    #def scale(self):