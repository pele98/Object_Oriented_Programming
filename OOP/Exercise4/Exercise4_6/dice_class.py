# File name: dice_class
# Author: Pekka Lehtola
# Description: Roll a dice.

import random

class Dice:

    # Dice with three attributes: Color,
    def __init__(self):

        self.color = "White"
        self.side_up = 1
        self.sum_of_throws = 0

    # Selecting random number between 1 and 6, form that selectin predefined side color.
    # Modifying dices values and calculating new sum.
    def roll_the_dice(self):

        random_number = random.randint(1,6)
        colors = {1: "Red", 2: "Blue", 3: "Green", 4: "Yellow", 5: "Black", 6: "White"}

        self.sum_of_throws += random_number
        self.side_up = random_number
        self.color = colors[self.side_up]

        print("Rolling the dice...")

    def get_side_up(self):

        return print("Dices side up is:", self.side_up)

    # Prints objects str method.
    def get_dice_state(self):

        print("Checking dice...")
        print(self)

    # Runs init method again to reset the sum of throws
    def restart_game(self):

        self.__init__()
        print("Restarting the game...", end="\n\n")

    # Defining printing of the object.
    def __str__(self):

        return f"""Dices color is {self.color}, the sideup is {self.side_up}
and sum of throws is {self.sum_of_throws} \n """
