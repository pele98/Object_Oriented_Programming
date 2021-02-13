# File name: dice_class
# Author: Pekka Lehtola
# Description: Creates dice object and dice can be rolled.

import random

class Dice:

    def __init__(self):

        self.id = 0
        self.side_up = 1

    # Selecting random number between 1 and 6
    def roll_the_dice(self):

        random_number = random.randint(1,6)

        self.side_up = random_number

    def get_side_up(self):
        return self.side_up


    # Defining printing of the object.
    def __str__(self):

        return f"""Dice {self.id} side up is {self.side_up} """
