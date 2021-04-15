# File name: character
# Author: Pekka Lehtola
# Description: Character class that is derived from pygame sprites

import pygame
from config import *
from ammo import *

class Character(pygame.sprite.Sprite):

    def __init__(self, sprite, name, left, right, character_x, character_y):
        super(Character, self).__init__()
        self.name = name
        self.surf = pygame.transform.scale(pygame.image.load(sprite), (character_x, character_y))                    # Surface image
        self.surf.set_colorkey(GREEN_SCREEN)                            # Defining see through color
        self.rect = self.surf.get_rect()    # Sets up characters hitbox
        self.animation_list = [left, right]
        self.animation_counter = 0
        self.ammo = []                                                  # Reloaded ammo
        self.shot_ammo = []                                             # Ammo that character has shot
        self.reloaded = False
        self.reload_img = False
        self.shooting_speed = 0
        self.reload_speed = INF
        self.health = []

    # Reloading function

    def animation_update(self, animation):

        self.surf = pygame.transform.scale(pygame.image.load(animation), (int(indian_x), int(indian_y)))
        self.surf.set_colorkey(GREEN_SCREEN)
        self.rect = self.surf.get_rect(topleft=(self.rect.x, self.rect.y))

        self.animation_counter += 1
        if self.animation_counter == 2:
            self.animation_counter = 0

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

        global indian_y, indian_x, cowboy_y, cowboy_x

        # Detects keyboard inputs and calculates new location for character.
        if self.name == "Indian":

            animation = self.animation_list[self.animation_counter]

            if pressed_keys[K_UP]:

                indian_y -= 1
                indian_x -= 0.8
                print("y", indian_y)
                print("x", indian_x)
                if indian_y <= 92:
                    indian_y = 92
                    indian_x = 44
                self.surf = pygame.transform.scale(pygame.image.load(animation), (int(indian_x), int(indian_y)))
                self.surf.set_colorkey(GREEN_SCREEN)
                self.rect = self.surf.get_rect(topleft=(self.rect.x, self.rect.y))
                self.rect.move_ip(0, -MOVEMENT_SPEED)

            if pressed_keys[K_DOWN]:


                indian_y += 1
                indian_x += 0.8
                print("y", indian_y)
                print("x", indian_x)
                if indian_y >= 146:
                    indian_y = 146
                    indian_x = 88
                self.surf = pygame.transform.scale(pygame.image.load(INDIAN_STANDING),
                                                   (int(indian_x), int(indian_y)))
                self.surf.set_colorkey(GREEN_SCREEN)
                self.rect = self.surf.get_rect(topleft=(self.rect.x, self.rect.y))
                self.rect.move_ip(0, MOVEMENT_SPEED)

            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-MOVEMENT_SPEED, 0)

            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(MOVEMENT_SPEED, 0)

        if self.name == "Cowboy":

            if pressed_keys[K_w]:

                cowboy_y -= 1.0
                cowboy_x -= 0.441
                print("y", cowboy_y)
                print("x", cowboy_x)
                if cowboy_y <= 104:
                    cowboy_y = 104
                    cowboy_x = 46
                self.surf = pygame.transform.scale(pygame.image.load(COWBOY_STANDING),
                                                   (int(cowboy_x), int(cowboy_y)))
                self.surf.set_colorkey(GREEN_SCREEN)
                self.rect = self.surf.get_rect(topleft=(self.rect.x, self.rect.y))

                self.rect.move_ip(0, -MOVEMENT_SPEED)

            if pressed_keys[K_s]:

                cowboy_y += 1
                cowboy_x += 0.44
                print("y", cowboy_y)
                print("x", cowboy_x)
                if cowboy_y >= 158:
                    cowboy_y = 158
                    cowboy_x = 70
                self.surf = pygame.transform.scale(pygame.image.load(COWBOY_STANDING),
                                                   (int(cowboy_x), int(cowboy_y)))
                self.surf.set_colorkey(GREEN_SCREEN)
                self.rect = self.surf.get_rect(topleft=(self.rect.x, self.rect.y))

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
        if self.rect.bottom <= 496:
            self.rect.bottom = 496
        if self.rect.bottom >= SCREEN_SIZE_VER:
            self.rect.bottom = SCREEN_SIZE_VER

    ### WORK IN PROGRESS ###
    #def scale(self):