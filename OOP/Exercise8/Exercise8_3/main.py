# File:         main.py
# Author:
# Description:  Main file for exercise 8_3

from cookie import *
import random

#Takes user or customers flavour request.
while True:

    flavours = ["Vanilla", "Chocolate", "Mint"]
    user_flavour = input("Choose flavour: Vanilla, Chocolate, Mint: ")

    if user_flavour in flavours:
        break

def main(user_flavour):

    # Chooses randomly what flavour of cookies is baked.
    # Creates a list of Cookie objects.
    choice = random.randint(0, 2)
    cookie_list = []

    # In this example 10 cookies are created and added to the list.
    for object in range(0,10):

        object = Cookie()

        cookie_list.append(object)

    # Bakes every cookie in the list one by one
    # And prints out cookies baked state.
    # and lastly checks if every cookie has been baked
    baked = 0
    for object in cookie_list:

        object.bake_cookie(baked+1)

        baked += 1

        if baked == len(cookie_list):
            print("All cookies baked")
            print()

    # Frosts every cookie in the list one by one
    # And prints out cookies frosting flavour.
    # and lastly checks if every cookie has been frosted.
    frosted = 0
    for object in cookie_list:

        object.frost_cookie(choice, frosted+1)

        frosted += 1

        if frosted == len(cookie_list):
            print("All cookies frosted")
            print()

    # Checks if the frosting is the same as customer wanted.
    test_cookie = cookie_list[0]

    if test_cookie.get_frosting() != user_flavour:

        print("Oops i frosted the cookies with wrong flavour...")
        print("Let me just start from the beginning.")
        print()

        main(user_flavour)

    # If frosting was correct prints all the cookies out.
    else:

        print("All cookies baked with the right frosting!")
        print("Here are all the cookies once more:")
        print()

        for object in cookie_list:
            print(object)

main(user_flavour)