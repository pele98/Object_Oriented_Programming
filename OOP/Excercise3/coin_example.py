# File: Example
# Description: Simulate coin flip
# Author: Pekka Lehtola

import random

class Coin:
    # The __init__ method initializes the sideup data attribute with "heads"

    def __init__(self):
        self.__sideup = "Heads"
        self.currency = "Euro"


    # Selects a random integer between 0 and 14. If the value is 0-4 side up is heads.
    # If the value is 5-9 tails is choosen. 10-12 coin lands upright.
    # 13-14 coin falls into an rabbit hole...

    def toss(self):

        random_number = random.randint(0,14)

        if random_number in range(0,5):
            self.__sideup = "Heads"

        elif random_number in range(5,10):
            self.__sideup = "Tails"

        elif random_number in range(10, 13):
            self.__sideup = "Upright"

        else:
            self.__sideup = "in a rabbit hole...Game over, because you don't have a coin anymore."
            print(self)
            exit()

    # The get_sideup method return the value referenced by sideup.
    def get_sideup(self):

        return self.__sideup

    # Returns a random currency from the list.
    def get_currency(self):

        currency_list = ["Euro", "Pound", "Dollar", "Ruble", "Yen"]
        self.currency = str(currency_list[random.randint(0, 4)])
        return self.currency

    # Str method for printing objects status.
    def __str__(self):
        return f"""Currency is {self.currency} and the coin is {self.get_sideup()} \n  """

# The main function
def main():

    # Create an object from the Coin class.
    my_coin = Coin()

    # Get random currency
    my_coin.get_currency()

    # Display the side of the coin that is facing up.
    print(my_coin)

    # Atempting to change private attribute sideup in main.
    my_coin.__sideup= input("This is a test to change private attribute sideup: ")
    print(my_coin.get_sideup())
    print(my_coin, end="\n\n")

    print("To toss the coin press enter. Type random for random currency")
    print("Or type the Currency you want", end="\n\n")

    while True:

        # Makes the user press enter before next toss.
        # If input is None currency stays the same.
        # If user types random, new currency is chosen.
        # If input is anything else currency changes to that.

        user_input = input()

        if user_input !="":
            if user_input =="random":
                my_coin.get_currency()
            else:
                my_coin.currency = user_input

        # Toss the coin.
        print("I am tossing the coin...")
        my_coin.toss()

        # Display the side of the coin that is facing up.
        print(my_coin)


# Call the main function.
main()
