#File: Example
#Description: Simulate coin flip
#Author: Pekka Lehtola

import random

class Coin:
    #The __init__ method initializes the sideup data attribute with "heads"

    def __init__(self):
        self.sideup ="Heads"


    #Selects a random integer between 0 and 14. If the value is 0-4 side up is heads.
    #If the value is 5-9 tails is choosen. 10-12 coin lands upright.
    #13-14 coin falls into an rabbit hole...

    def toss(self):

        random_number = random.randint(0,14)

        if random_number in range(0,5):
            self.sideup = "Heads"

        elif random_number in range(5,10):
            self.sideup = "Tails"

        elif random_number in range(10, 13):
            self.sideup = "Coin landed upright"

        else:
            print("Coin landed into a rabbit hole...Game over, because you don't have a coin anymore.")
            exit()

    # The get_sideup method return the value referenced by sideup.

    def get_sideup(self):

        return self.sideup

# The main function

def main():

    #Create an object from the Coin class.
    my_coin = Coin()

    # Display the side of the coin that is facing up.
    print("This side is up: ", my_coin.get_sideup())

    print("To toss the coin press enter.", end="\n\n")

    while True:

        #Makes the user press enter before next toss.
        user_input = input()

        #Toss the coin.
        print("I am tossing the coin...")
        my_coin.toss()

        # Display the side of the coin that is facing up.
        print("This side is up: ", my_coin.get_sideup())


# Call the main function.
main()
