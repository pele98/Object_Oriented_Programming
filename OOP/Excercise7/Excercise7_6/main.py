# File:         main.py
# Author:       
# Description:  Main function fro exercise 7.6

import random

countrys = {}

# Opens countrys txt file and seperates it into keys and values.
# Also removes linebreak at the end of capitals

with open("countrys.txt") as c:

    for line in c:
        (key, capital) = line.split(" : ")
        (val, space) = capital.split("\n")
        countrys[key] = val

# Add countrys into a list and puts them into a random order.
# Adds shuffled countrys back to the dictionary.
# Also creates list of Countrys that can be called with index number

shuffle = list(countrys.items())
random.shuffle(shuffle)
countrys = dict(shuffle)
country_lst = list(countrys)


print("The Capital quiz")
print("Write the capital of the country")
print()

while True:

    points = 0

    # With country lists index value checks if user input matches dictionarys
    # key value. Correct awnser gives user a point and íncorret awnser returns correct
    # awnser.

    for i in range(10):

        print(country_lst[i])

        user_input = input(": ")

        if user_input == countrys[country_lst[i]]:
            print("Correct!")
            print()
            points += 1

        else:
            print("Wrong, correct awnser is", countrys[country_lst[i]])
            print()

    # Prints out users score and prompts user if game is played again.

    print("Your score was", str(points) + "/10")
    print()
    user_input = input("Want to play again (Yes or No): ")

    while True:

        if user_input == "Yes":
            print()
            break

        if user_input == "No":
            exit()
