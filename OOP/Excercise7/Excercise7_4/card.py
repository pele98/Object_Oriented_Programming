# File:         card.py
# Author:       Pekka Lehtola
# Description:  Card class

# Card object that has attributes suit and value.
class Card:

    def __init__(self, suit, val):

        self.suit = suit
        self.value = val

    #Prints out card with set format
    def show_card(self):

        print("{} of {}".format(self.value, self.suit))

    #Str function used to print out extended print that is used in Higest value game.
    def __str__(self):
        return "Card is {} of {}.".format(self.value, self.suit)



