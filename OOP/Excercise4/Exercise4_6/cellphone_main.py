# File name: Cellphone_main
# Author: Pekka Lehtola
# Description: Cellphone main function, returned cellphone
#              selected with dice roll.

from cellphone_class import Cellphone
from dice_class import Dice

#List of all cellphone objects
cellphone_object_list = []

def create_cellphones():

    global cellphone_object_list
    ID = 0

    #Ask user how many objects are created
    #ID is given automaticly for phone.
    #Lastly add object to list
    for i in range(int(input("How many cellphones you want to create: "))):

        users_cellphone = input("Enter objects name: ")

        users_cellphone = Cellphone()
        users_cellphone.set_manufact()
        users_cellphone.set_model()
        users_cellphone.set_retail_price()

        ID += 1
        users_cellphone.set_id(ID)

        cellphone_object_list.append(users_cellphone)

        print()

#Prints every cellphone using __str__ method
def main():


    create_cellphones()

    #Imported Dice class
    #Dice rolls random number and with that cellphone is selected
    dice = Dice()
    dice.roll_the_dice()
    dice.get_side_up()

    print("Here is the cellphones you created: ")

    #Returns every object in list
    for object in cellphone_object_list:

        print(object)

    print("Here is cellphone selected with dice roll: ")

    #Returns object that has same ID as dices side up value.
    for object in cellphone_object_list:

        if dice.side_up == int(object.get_only_id()):
            print(object)

main()

