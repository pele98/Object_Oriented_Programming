# File name: Exercise3_6
# Author: Pekka Lehtola
# Description: Roll two dices. can calculate sum of them.

import random

class Dice:

    # Dice with three attributes: Color,
    def __init__(self):

        self.color = "White"
        self.side_up = 6


    # Selecting random number between 1 and 6, form that selectin predefined side color.
    # Modifying dices values and calculating new sum.
    def roll_the_dice(self):

        random_number = random.randint(1,6)
        colors = {1: "Red", 2: "Blue", 3: "Green", 4: "Yellow", 5: "Black", 6: "White"}

        self.side_up = random_number
        self.color = colors[self.side_up]

    #Calculates sum of dices.
    def calculate_sum(self, second):

        sum = self.side_up + second.side_up
        print ("Sum of dices is", sum)

    # Prints objects str method.
    def get_side_up(self):

        print(self)

    # Runs init method again to reset the sum of throws
    def restart_game(self):

        self.__init__()

    # Defining printing of the object.
    def __str__(self):

        return f"""Dices color is {self.color}, the sideup is {self.side_up} \n """

# Setting first_dice and second_dice as Dice objects
first_dice = Dice()
second_dice = Dice()

print("options are = roll the dices / get side up / calculate sum / restart game")

# Infinite loop for the game. user input defines what method is used.
while True:

    user_input = str(input(": "))

    if user_input == "roll the dices":
        print("Rolling both dices...")
        first_dice.roll_the_dice()
        second_dice.roll_the_dice()

    elif user_input == "get side up":
        print("First dice: ")
        first_dice.get_side_up()
        print("Second dice: ")
        second_dice.get_side_up()

    elif user_input == "calculate sum":

        first_dice.calculate_sum(second_dice)

    elif user_input == "restart game":
        first_dice.restart_game()
        second_dice.restart_game()
        print("Restarting the game...", end="\n\n")

    else:
        print("Value error.")
