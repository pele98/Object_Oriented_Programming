class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        for card in self.hand:
            card.show_card()


    def sum_of_cards(self):

        sum = 0
        for card in self.hand:
            sum += card.value

        return print("Sum of cards is", sum)