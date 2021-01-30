# File name: Exercise3_7_v2
# Author: Pekka Lehtola
# Description: Three player dice game

import random

#Dice class with player name and side up attribute.
class Dice:

    def __init__(self, name):

        self.name = name
        self.side_up = 1

    #If player allready lost they dont roll the dice
    def roll_the_dice(self):

        if self.side_up == 7:
            pass
        else:
            self.side_up = random.randint(1, 6)
            print(self.name, "rolls the dice...and gets", self.side_up)

#Setup players name attribute
player_1 = Dice(input("Name of player one: "))
player_2 = Dice(input("Name of player two: "))
player_3 = Dice(input("Name of player three: "))


#Checks if there are multiple of the same numbers that are not 7
def check_duplicates():

    if player_1.side_up == player_2.side_up and player_1.side_up != 7:

        print(player_1.name, "and", player_2.name, "rolls again")
        player_1.roll_the_dice()
        player_2.roll_the_dice()

    elif player_1.side_up == player_3.side_up and player_3.side_up != 7:

        print(player_1.name, "and", player_3.name, "rolls again")
        player_1.roll_the_dice()
        player_3.roll_the_dice()

    elif player_3.side_up == player_2.side_up and player_2.side_up != 7:

        print(player_3.name, "and", player_2.name, "rolls again")
        player_3.roll_the_dice()
        player_2.roll_the_dice()

    #If every player rolls the same number all players roll again.
    elif player_1.side_up and player_2.side_up == player_3.side_up:
        print("all players need to roll again: ")
        player_1.roll_the_dice()
        player_2.roll_the_dice()
        player_3.roll_the_dice()

#Check_list contains players dice rolls
#Check_list_dict is used for connecting players dice roll with players name
def check_winner():

    check_list = [player_1.side_up, player_2.side_up, player_3.side_up]
    check_list_without_removed_players = []
    check_list_dict = {player_1.side_up: player_1.name, player_2.side_up: player_2.name, player_3.side_up: player_3.name}

    #Fills check_list_without_removed_players with players with out dice side_up 7
    for i in range(len(check_list)):
        if int(check_list[i]) != 7:
            check_list_without_removed_players.append(check_list[i])

    #If two other player has side_up 7 declare remaining player as winner.
    if len(check_list_without_removed_players) == 1:
        winner = check_list_without_removed_players[0]

        print("Winner of the game is", check_list_dict[winner])
        exit()

    #Removes player with the smallest number by setting its side_up value as 7
    else:
        smallest_number = min(check_list_without_removed_players)
        player_name = check_list_dict[smallest_number]

        if player_name == player_1.name:
            player_1.side_up = 7
            print(player_1.name, "Had the smallest number and was removed from the game")

        if player_name == player_2.name:
            player_2.side_up = 7
            print(player_2.name, "Had the smallest number and was removed from the game")

        if player_name == player_3.name:
            player_3.side_up = 7
            print(player_3.name, "Had the smallest number and was removed from the game")


def main():

    player_1.roll_the_dice()
    player_2.roll_the_dice()
    player_3.roll_the_dice()

    check_duplicates()
    check_winner()

    player_1.roll_the_dice()
    player_2.roll_the_dice()
    player_3.roll_the_dice()

    check_duplicates()
    check_winner()
    check_winner()

main()