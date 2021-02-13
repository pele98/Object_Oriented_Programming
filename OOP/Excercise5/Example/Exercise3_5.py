# File name: Exercise3_5
# Author: Pekka Lehtola
# Description: Roll a dice.

import random

class Dice:

    # Dice with three attributes: Color,
    def __init__(self):

        self.color = "White"
        self.side_up = 6
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

    # Prints objects str method.
    def get_side_up(self):

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

# Setting my_dice as a Dice object
my_dice = Dice()
print("options are = roll the dice / get side up / restart game")

# Infinite loop for the game. user input defines what method is used.
#while True:

    #user_input = str(input(": "))

    #if user_input == "roll the dice":
        #my_dice.roll_the_dice()

    #elif user_input == "get side up":
        #my_dice.get_side_up()

    #elif user_input == "restart game":
        #my_dice.restart_game()

    #else:
    #    print("Value error.")
