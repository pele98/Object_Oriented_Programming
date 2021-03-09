# File name: Cellphone_main
# Author: Pekka Lehtola
# Description: Cellphone class main function

from cellphone_class import Cellphone


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
    print("Here is the cellphones you created: ")

    for object in cellphone_object_list:
        print(object)

main()

