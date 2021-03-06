# File:         main.py
# Author:       Pekka Lehtola
# Description:  Deck of cards and card games.

import card
import deck
from player import *
import time

def main():

    print("Let's test that a single card works...")

    my_card = card.Card("Hearts", 12)
    my_card.show_card()
    print(my_card)

    print("Single card testing is over.\n")

    print("Let's test that a deck of card is created...")

    my_deck = deck.Deck()
    my_deck.show_deck()

    print("Card deck testing is over.\n")

    print("Let's shuffle the deck.")
    my_deck.shuffle_deck()

    print("Let's test that a deck of card is shuffled...")

    my_deck.show_deck()

    print("Cards should be suffled now.\n")

    print("Let's draw 2 cards and show them.")
    print("You draw:")
    card1 = my_deck.draw_card()
    card1.show_card()
    print("Your opponent draw:")
    card1 = my_deck.draw_card()
    card1.show_card()

    # Code your Exercise 7 taks 4 game here.

    #My code starts here
    print()

def restart():

    user_input = input("Write exit to exit or something else to play again: ")

    if user_input != "Exit":
        highest_value()

    else:
        exit()

def highest_value():

    print("You have choosen highest value game")

    print("Building deck and shuffeling it")
    my_deck = deck.Deck()
    my_deck.shuffle_deck()

    while True:

        card_1 = my_deck.draw_card()
        print("Player 1 draws:")
        card_1.show_card()
        print()

        card_2 = my_deck.draw_card()
        print("Player 2 draws:")
        card_2.show_card()
        print()

        card_3 = my_deck.draw_card()
        print("Player 3 draws:")
        card_3.show_card()
        print()

        check_lst = [card_1.value, card_2.value, card_3.value]

        if len(set(check_lst)) < 3:
            print("Ohno there is duplicates of numbers, lets try that again.")

        elif max(check_lst) == check_lst[0]:
            print("Player 1 Wins!", end="\n\n")
            restart()

        elif max(check_lst) == check_lst[1]:
            print("Player 2 Wins!", end="\n\n")
            restart()

        else:
            print("Player 3 Wins!", end="\n\n")
            restart()

def black_jack():

    print("You have chosen Blackjack")

    print("Building deck and shuffeling it")
    my_deck = deck.Deck()
    my_deck.shuffle_deck()

    dealer = Player("Dealer")
    player = Player("Player")

    print("Dealer draws two cards and shows one")
    print("Dealers revealed card:")
    dealer.draw(my_deck)
    dealer.show_hand()
    dealer.draw(my_deck)

    print("Players turn")
    print("Player draws two cards and they are:")
    player.draw(my_deck)
    player.draw(my_deck)
    player.show_hand()
    player.sum_of_cards_blackjack()

    while True:

        if player.sum == 21:
            print("Player has BLACKJACK.")
            print("Player wins")
            print("Restarting game")
            print()
            time.sleep(3)
            black_jack()

        user_input = input("Options 'hit me' or 'stop' ")

        if user_input == "stop":
            break

        elif user_input == "hit me":
            player.draw(my_deck)
            player.show_hand()
            player.sum_of_cards_blackjack()

            if player.sum > 21:
                print("Sum is over 21, Dealer wins!")
                print("Restarting game.")
                print()
                time.sleep(3)
                black_jack()

    print("Dealers turn")
    print("Dealers cards:")
    dealer.show_hand()
    dealer.sum_of_cards_blackjack()

    while True:

        if dealer.sum == player.sum and dealer.sum < 21:
            print("Sums are tied. Dealer draws another:")


        elif dealer.sum > 21:
            print("Dealers sum over 21. Player wins!")
            print("Restarting game")
            time.sleep(3)
            black_jack()

        elif dealer.sum > player.sum:
            print("Dealer wins! ")
            print("Restarting game")
            print()
            time.sleep(3)
            black_jack()

        else:
            print("Dealers hand lower than players")
            print("Dealer draws another")

        time.sleep(2)
        dealer.draw(my_deck)
        dealer.show_hand()
        dealer.sum_of_cards_blackjack()




# Calling the main function here, do not change...
main()

#highest_value()

black_jack()
