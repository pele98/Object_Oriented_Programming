# File name: main
# Author: Pekka Lehtola
# Description: main

import pygame
from config import *
from character import *

pygame.init()


pressed_keys = pygame.key.get_pressed()

screen = pygame.display.set_mode([SCREEN_SIZE_HOR, SCREEN_SIZE_VER])

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    for characters in all_sprites:
        screen.blit(characters.surf, characters.rect)

    indian.move(pressed_keys)
    cowboy.move(pressed_keys)

    pygame.display.flip()

    screen.blit(BG, (0,0))

pygame.quit()