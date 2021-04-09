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

    ### WORK IN PROGRESS ###

    # In the start of the game shows count down
    def show_element(self, screen):


        self.rect.centerx = (SCREEN_SIZE_HOR / 2)
        self.rect.centery = (SCREEN_SIZE_VER / 2)
        screen.blit(self.surf, self.rect)
        pygame.display.flip()
        time.sleep(1.2)

    # Will be used to show the winner.
    #def game_end(self):

