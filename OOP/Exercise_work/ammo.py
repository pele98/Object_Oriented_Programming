# File name: character
# Author: Pekka Lehtola
# Description: Ammo class for characters to shoot.

import pygame
from config import *

# Ammo is derived from pygame sprites
class Ammo(pygame.sprite.Sprite):

    def __init__(self, ammo, name):
        super(Ammo, self).__init__()
        self.name = name
        self.surf = pygame.image.load(ammo)     # Image
        self.surf.set_colorkey(GREEN_SCREEN)    # See through color
        self.rect = self.surf.get_rect()        # Hitbox

        self.shot = False

    # Function for shot ammo
    def ammo_shot(self, shooter, enemy):

        if self.shot == True:

            # If the shooter is indian arrow travels to left
            # If arrow hits cowboy, cowboy is killed.
            if shooter.name == "Indian":
                self.rect.move_ip(-BULLET_VELOCITY, 0)

                if self.rect.colliderect(enemy.rect):
                    self.rect.x = -200
                    self.kill()
                    enemy.healt.pop(-1)
                    if len(enemy.healt) == 0:
                        enemy.kill()

            # Same as indian but bullet travels right
            if shooter.name == "Cowboy":
                self.rect.move_ip(BULLET_VELOCITY, 0)

                if self.rect.colliderect(enemy.rect):
                    self.rect.x = 2200
                    self.kill()
                    enemy.healt.pop(-1)
                    if len(enemy.healt) == 0:
                        enemy.kill()