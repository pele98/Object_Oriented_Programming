# File name: Main
# Author: Pekka Lehtola
# Description: Main file for dice example

import Exercise3_5 as dice

def roll_dice(demo_dice):

    demo_dice.roll_the_dice()
    print(demo_dice)

def main():

    my_dice = dice.Dice()

    print(my_dice)

    roll_dice(my_dice)

    print(my_dice)

main()