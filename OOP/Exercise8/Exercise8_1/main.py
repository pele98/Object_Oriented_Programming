# File:         main.py
# Author:
# Description:  Main function fro exercise 8_1

from house import House

def main():

    my_house = House()

    print(my_house)

    my_house.set_windows_and_bed()
    my_house.set_floors_and_surfaces()
    my_house.set_shopping()
    my_house.set_pandemic_shopping()

main()
