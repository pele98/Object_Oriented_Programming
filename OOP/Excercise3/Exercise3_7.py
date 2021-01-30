# File name: Exercise3_7
# Author: Pekka Lehtola
# Description: Three player dice game

import random

class Dice:

    def __init__(self, name):

        self.name = name
        self.side_up = 1

    def roll_the_dice(self):
        if self.side_up == 7:
            pass
        else:
            print(self.name, "rolls the dice...")
            self.side_up = random.randint(1,6)

class Game:

    def __init__(self, player_1, player_2, player_3):

        self.player_list = [player_1.name, player_2.name, player_3.name]
        self.dice_values = [player_1.side_up, player_2.side_up, player_3.side_up]

    def check_duplicates(self):


        if self.dice_values[0] == self.dice_values[1]:
            print(player_1.name, "and", player_2.name, "has duplicates and must reroll")
            player_1.roll_the_dice()
            player_2.roll_the_dice()
            self.dice_values = [player_1.side_up, player_2.side_up, player_3.side_up]

        elif self.dice_values[0] == self.dice_values[2]:
            print(player_1.name, "and", player_3.name, "has duplicates and must reroll")
            player_1.roll_the_dice()
            player_3.roll_the_dice()
            self.dice_values = [player_1.side_up, player_2.side_up, player_3.side_up]

        elif self.dice_values[1] == self.dice_values[2]:
            print(player_2.name, "and", player_3.name, "has duplicates and must reroll")
            player_1.roll_the_dice()
            player_3.roll_the_dice()
            self.dice_values = [player_1.side_up, player_2.side_up, player_3.side_up]

        elif len(set(self.dice_values)) == 1:
            print("All players rolled the same value: ")

            player_1.roll_the_dice()
            player_2.roll_the_dice()
            player_3.roll_the_dice()
            self.dice_values = [player_1.side_up, player_2.side_up, player_3.side_up]

        else:
            print("No duplicates")

    def check_winner(self):

        if len(self.player_list) == 1:

            print(*self.player_list, "Is the winner!")

        if len(self.player_list) == 2:

            self.dice_values = [player_1.side_up, player_2.side_up, player_3.side_up]
            self.dice_values.remove(min(self.dice_values))

        elif self.dice_values[0] == min(self.dice_values):
            print(player_1.name, "Had the smallest number and was removed from the game.")
            player_1.side_up = 7
            self.player_list.remove(player_1.name)

        elif self.dice_values[1] == min(self.dice_values):
            print(player_2.name, "Had the smallest number and was removed from the game.")
            player_2.side_up = 7
            self.player_list.remove(player_2)

        elif self.dice_values[2] == min(self.dice_values):
            print(player_2.name, "Had the smallest number and was removed from the game.")
            player_3.side_up = 7
            self.player_list.remove(player_3)




player_1 = Dice(input("Name of player one: "))
player_2 = Dice(input("Name of player two: "))
player_3 = Dice(input("Name of player three: "))

dice_game = Game(player_1, player_2, player_3)

print("First round")

def main():

    player_1.roll_the_dice()
    player_2.roll_the_dice()
    player_3.roll_the_dice()

    dice_game.check_duplicates()
    dice_game.check_winner()

    print("Second round")

    player_1.roll_the_dice()
    player_2.roll_the_dice()
    player_3.roll_the_dice()

    dice_game.check_duplicates()
    dice_game.check_winner()

main()