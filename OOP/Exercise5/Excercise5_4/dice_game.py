# File name: dice_game
# Author: Pekka Lehtola
# Description: dice_game with three dices.

from dice_class import *

#Setting up player ones dices to a list.
def player_1_init():

    global player_1_dices

    player_1_dices = []
    id = 0

    for object in range(3):

        id +=1
        object = Dice()
        object.id = id
        player_1_dices.append(object)

#Setting up player twos dices to a list.
def player_2_init():
    global player_2_dices

    player_2_dices = []
    id = 0
    for object in range(3):

        id += 1
        object = Dice()
        object.id = id
        player_2_dices.append(object)

#Rolls player ones dices and prints the state of each dice.
def player_1_dice_rolls():
    print("Player 1 dices are: ")

    for object in player_1_dices:
        object.roll_the_dice()
        print(object)
    print()

#Rolls player twos dices and prints the state of each dice.
def player_2_dice_rolls():
    print("Player 2 dices are: ")

    for object in player_2_dices:
        object.roll_the_dice()
        print(object)
    print()

#Calculate sum from the list
def player_1_sum():
    sum = 0

    for object in player_1_dices:
        sum += object.side_up
    return sum

def player_2_sum():
    sum = 0

    for object in player_2_dices:
        sum += object.side_up
    return sum

def main():

    #Creates empty lists for the two players.
    player_1_dices = []
    player_2_dices = []

    player_1_init()
    player_2_init()

    #Game is played until winner is found.
    while True:

        player_1_dice_rolls()
        player_2_dice_rolls()

        print("Player 1 sum of dices is", player_1_sum())
        print("Player 2 sum of dices is", player_2_sum())

        if player_1_sum() == player_2_sum():
            print("Oh no ts a tie, dices are rolled again")
            print()

        #Prints out the winner and how much bigger the sum was.
        elif player_1_sum() > player_2_sum():
            print("Player 1 won by", player_1_sum() - player_2_sum())
            break

        else:
            print("Player 2 won by", player_2_sum() - player_1_sum())
            break
main()