# File:         deck.py
# Author:       Pekka Lehtola
# Description:  Deck class

from card import *
import random

class Deck:

    def __init__(self):

        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for n in range(1, 14):
                self.cards.append(Card(s, n))
    def show_deck(self):
        for c in self.cards:
            c.show_card()

    def shuffle_deck(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        return self.cards.pop()
