#File name: Exercise3_5
#Author: Pekka Lehtola
#Description: Roll a dice.

import random

class Dice:

    def __init__(self):

        self.color = "White"
        self.side_up = 6
        self.sum_of_throws = 0

    def toss(self):

        numbers = [1, 2, 3, 4, 5, 6]
        colors = {1: "Red", 2: "Blue", 3: "Green", 4: "Yellow", 5: "Black", 6: "White"}

        self.side_up = numbers[random.randint(0,5)]
        self.color = colors[self.side_up]

        print(self)


    def __str__(self):

        return f"""Dices color is {self.color} and the sideup is {self.side_up}\n """


my_dice = Dice()

my_dice.toss()