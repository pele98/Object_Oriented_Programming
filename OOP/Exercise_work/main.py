# File name: main
# Author: Pekka Lehtola
# Description: main file exercise work

import pygame
from config import *
from character import *
from ui import *
from time import perf_counter, sleep

running = True

def main():

        # Initialize pygame
        pygame.init()

        # Sets up screen size
        screen = pygame.display.set_mode([SCREEN_SIZE_HOR, SCREEN_SIZE_VER])


        global running

        # Creates indian and cowboy objects.
        # Also define graphigs to them.
        indian = Character("images/indian_1.png", "Indian")
        cowboy = Character("images/cowboy_1.png", "Cowboy")

        # Adds indian and cowboy to sprite group.
        all_sprites = pygame.sprite.Group()
        all_sprites.add(indian)
        all_sprites.add(cowboy)

        # Indians initial location
        indian.rect.x = 1820
        indian.rect.y = 640

        # Cowboys initial location
        cowboy.rect.x = 100
        cowboy.rect.y = 640

        hearth = Ui("images/hearth_1.png")
        reload = Ui("images/circle1.png")

        hearth.set_up_hearts(character=cowboy)
        hearth.set_up_hearts(character=indian)

        # Background update
        screen.blit(BG, (0, 0))

        # start countdown
        start = Ui("images/11.png")
        start.game_start(ONE, TWO, THREE, screen)
        start.kill()

        while running:

            time = perf_counter()

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

            # Ui elements
            hearth.show_hearts(cowboy, screen)
            hearth.show_hearts(indian, screen)

            hearth.show_ammo(cowboy, screen)
            hearth.show_ammo(indian, screen)

            reload.show_reload(indian, screen)
            reload.show_reload(cowboy, screen)


            # Reload function
            indian.reload(pressed_keys, time)
            cowboy.reload(pressed_keys, time)

            # Shooting function
            indian.shoot(pressed_keys, time)
            cowboy.shoot(pressed_keys, time)

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

            # Starts game over when either character dies.
            if len(indian.health) == 0 or len(cowboy.health) == 0:

                main()

        pygame.quit()

main()