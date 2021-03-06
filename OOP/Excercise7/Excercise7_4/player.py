class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.sum = 0

    def draw(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        for card in self.hand:
            card.show_card()


    def sum_of_cards_blackjack(self):

        self.sum = 0
        ace_counter = 0
        for card in self.hand:

            if card.value == 11 or 12 or 13:
                print("over 10")
                self.sum += 10

            elif card.value == 1 and (self.sum + 11) < 21:
                print("Ace")
                self.sum += 11
                ace_counter += 1

            else:
                self.sum += card.value

                if self.sum > 21 and ace_counter < 0:
                    self.sum -= 10

        return print("Sum of cards is", self.sum)
