# File:         deck.py
# Author:       Pekka Lehtola
# Description:  Deck class

from card import *
import random

#Deck class that has card list and build function.
class Deck:

    def __init__(self):

        self.cards = []
        self.build()

    #Adds every suit from 1 to 13 to deck list.
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for n in range(1, 14):
                self.cards.append(Card(s, n))

    #Prints out the entire deck of cards.
    def show_deck(self):
        for card in self.cards:
            card.show_card()

    #Shuffles deck into random order.
    def shuffle_deck(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # Pops out last item from list and returns it.
    def draw_card(self):
        return self.cards.pop()
