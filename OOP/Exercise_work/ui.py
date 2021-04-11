# File name: ui
# Author: Pekka Lehtola
# Description: User interface class. Used for showing different elements in screen.

import pygame
from config import *
from time import sleep
#from main import main



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
        sleep(1.2)

    # Will be used to show the winner.
    #def game_end(self):

    def countdown(self, screen):

        self.surf = pygame.image.load("images/33.png")
        self.surf.set_colorkey(GREEN_SCREEN)
        self.show_element(screen)
        screen.blit(BG, (0, 0))

        self.surf = pygame.image.load("images/22.png")
        self.surf.set_colorkey(GREEN_SCREEN)
        self.show_element(screen)
        screen.blit(BG, (0, 0))

        self.surf = pygame.image.load("images/11.png")
        self.surf.set_colorkey(GREEN_SCREEN)
        self.show_element(screen)
        screen.blit(BG, (0, 0))

    def winner(self, cowboy, indian, screen):


        if len(indian.health) == 0:

            self.surf = pygame.image.load("images/cowboy_wins.png")
            self.surf.set_colorkey(GREEN_SCREEN)
            self.show_element(screen)
            sleep(1)
            return True

        if len(cowboy.health) == 0:

            self.surf = pygame.image.load("images/indian_wins.png")
            self.surf.set_colorkey(GREEN_SCREEN)
            self.show_element(screen)
            sleep(1)
            return True


