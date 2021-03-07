# File:         player.py
# Author:       Pekka Lehtola
# Description:  Player class

# Player class with attributes name, hand, and sum(Sum of cards in hand)
class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.sum = 0

    # Takes card from deck and adds it to hand list
    def draw(self, deck):
        self.hand.append(deck.draw_card())

    # Prints out each card in hand
    def show_hand(self):
        for card in self.hand:
            card.show_card()

    # Calculates sum of cards in hand
    def sum_of_cards(self):
        self.sum = 0

        for card in self.hand:

            self.sum += card.value

    # Calculates sum of cards in hand using Blackjack rules.
    # 11, 12, 13 counted as 10. Ace counted as 11 except when sum would go over 21.
    def sum_of_cards_blackjack(self):

        self.sum = 0
        ace_counter = 0 # Ace counter used to check if hand has aces that can be reduced to one.
        for card in self.hand:

            if card.value > 10 and card.value != 1:
                self.sum += 10

            elif card.value == 1 and (self.sum + 11) < 21:
                self.sum += 11
                ace_counter += 1

            else:
                self.sum += card.value

                if self.sum > 21 and ace_counter > 0:
                    print("Sum of cards greater than 21, Ace reduced to one")
                    self.sum -= 10

        print("Sum of cards is", self.sum)
        print()
