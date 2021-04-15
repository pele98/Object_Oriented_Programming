# File name: main
# Author: Pekka Lehtola
# Description: main file exercise work

import pygame
from config import *
from character import *
from ui import *
from time import perf_counter, sleep
from heart_ui import *
from ammo_ui import *
from heart_power_up import *
from super_ammo import Ammo_power_up
from random import randint

running = True

def main():

        # Initialize pygame
        pygame.init()

        # Sets up screen size
        screen = pygame.display.set_mode([SCREEN_SIZE_HOR, SCREEN_SIZE_VER])

        heart_timer = randint(7, 12) + 3
        super_ammo_timer = randint(14, 20) + 3

        timer = perf_counter()

        if timer > 5:
            heart_timer += timer
            super_ammo_timer += timer


        global running

        # Creates indian and cowboy objects.
        # Also define graphigs to them.

        indian = Character(INDIAN_STANDING, "Indian", INDIAN_LEFT, INDIAN_RIGHT, indian_x, indian_y)
        cowboy = Character(COWBOY_STANDING, "Cowboy", COWBOY_LEFT, COWBOY_RIGHT, cowboy_x, cowboy_y)

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

        heart = Heart_ui()
        reload = Ammo_ui("images/circle1.png")

        heart_power_up_list = []
        super_ammo_power_up_list = []

        heart.set_up_hearts(character=cowboy)
        heart.set_up_hearts(character=indian)

        # Background update
        screen.blit(BG, (0, 0))

        # start countdown
        countdown = Ui("images/11.png")
        countdown.countdown(screen)

        winner = Ui("images/cowboy_wins.png")

        while running:

            timer = perf_counter()

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
            heart.show_hearts(cowboy, screen)
            heart.show_hearts(indian, screen)

            reload.show_ammo(cowboy, screen)
            reload.show_ammo(indian, screen)

            reload.show_reload(indian, screen)
            reload.show_reload(cowboy, screen)


            # Reload function
            indian.reload(pressed_keys, timer)
            cowboy.reload(pressed_keys, timer)

            # Shooting function
            indian.shoot(pressed_keys, timer)
            cowboy.shoot(pressed_keys, timer)

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

            # Power ups

            if timer > heart_timer:

                heart_timer = timer + randint(11, 17)
                heart_power_up = Heart_power_up()
                heart_power_up.add_power_up(heart_power_up_list)

            for hearts in heart_power_up_list:
                hearts.show_power_up(screen)
                hearts.heart_pickup(indian, cowboy, heart)

            if timer > super_ammo_timer:

                super_ammo_timer = timer + randint(20, 26)
                super_ammo = Ammo_power_up()
                super_ammo.add_power_up(super_ammo_power_up_list)

            for super_ammo in super_ammo_power_up_list:

                super_ammo.show_power_up(screen)
                super_ammo.super_pickup(indian, cowboy)

            # Update screen
            pygame.display.flip()

            # Background update
            screen.blit(BG, (0,0))

            # Starts game over when either character dies.

            if winner.winner(cowboy, indian, screen):
                main()

        pygame.quit()

main()