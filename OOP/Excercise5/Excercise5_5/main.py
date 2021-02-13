# File name: main
# Author: Pekka Lehtola
# Description: main file for player dictionary game.

from player_class import *
from dice_class import *

#Creating all of the objects.
matti = Player(1, "matti", "koskinen")
pekka = Player(2, "pekka", "lehtola")
linda = Player(3, "linda", "laine")

#Creating list of players and their id.s
players = [matti, pekka, linda]
players_id = [matti.get_id(), pekka.get_id(), linda.get_id()]

#Dice objects
dice_1 = Dice(1)
dice_2 = Dice(2)
dice_3 = Dice(3)

dices = [dice_1, dice_2, dice_3]

#Creating dictionary from the objects.
player_dict = dict(zip(players_id, dices))

#Firstly prints the name from players list
#then rolls the dice from dictionary.
for object in range(0, 3):

    print(players[object].get_first_name(), "rolled the dice and the result is: ")

    player_dict[object+1].roll_the_dice()

    print(player_dict[object+1])

    print()