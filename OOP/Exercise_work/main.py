# File name: main
# Author: Pekka Lehtola
# Description: main file exercise work

import pygame
from config import *
from character import *
import time

# Initialize pygame
pygame.init()


# Sets up screen size
screen = pygame.display.set_mode([SCREEN_SIZE_HOR, SCREEN_SIZE_VER])

running = True

# Indians initial location
indian.rect.x = 1820
indian.rect.y = 640

# Cowboys initial location
cowboy.rect.x = 100
cowboy.rect.y = 640

while running:

    # Detects events while game is running.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pygame detects what keys are pressed.
    pressed_keys = pygame.key.get_pressed()

    # The term used for rendering objects is blitting.
    # Surf : Surface, Rect : Rectangle.
    # Rectangle is used for collide detection
    # Surface can be image or color.

    for characters in all_sprites:
        screen.blit(characters.surf, characters.rect)

    # Reload function
    indian.reload(pressed_keys)
    cowboy.reload(pressed_keys)

    # Shooting function
    indian.shoot(pressed_keys)
    cowboy.shoot(pressed_keys)

    # Moving function
    indian.move(pressed_keys)
    cowboy.move(pressed_keys)

    # Bullet travel and hit detection
    for ammo in indian.shot_ammo:

        ammo.ammo_shot(indian, cowboy)
        screen.blit(ammo.surf, ammo.rect)

    for ammo in cowboy.shot_ammo:

        ammo.ammo_shot(cowboy, indian)
        screen.blit(ammo.surf, ammo.rect)


    # Update screen
    pygame.display.flip()

    # Background update
    screen.blit(BG, (0,0))

    # Sets Frame duration
    time.sleep(FRAME_DURATION)

pygame.quit()
