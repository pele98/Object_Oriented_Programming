# File:         card.py
# Author:       Pekka Lehtola
# Description:  Card class

class Card:

    def __init__(self, suit, val):

        self.suit = suit
        self.value = val

    def show_card(self):

        print("{} of {}".format(self.value, self.suit))

    def __str__(self):
        return "Card is {} of {}.".format(self.value, self.suit)



