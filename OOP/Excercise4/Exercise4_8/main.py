# File name: main
# Author: Pekka Lehtola
# Description: Main function for exercise 4_8

#Required imports
from car_class import Car
from mammal_class import Mammal
from dice_class import Dice

#List for storing mamal objects
mammal_list = []

#Automated mamal object creator
def create_mammals():

    global mammal_list

    ID = [1, 2, 3, 4, 5, 6]
    obj = ["dog", "horse", "cat", "cow", "rabbit", "monkey"]
    species = ["Dog", "Horse", "Cat", "Cow", "Rabbit", "Monkey"]
    name = ["Fluffy", "Linda", "Snuffles", "Mansikki", "Bucks", "George"]
    weight = [60, 400, 10, 700, 3, 30]
    width = [40, 70, 10, 90, 8, 20]
    breadth = [100, 200, 50, 170, 40, 20]
    height = [60, 160, 30, 120, 50, 60]

    #Takes the same index from every list and combines it to one mamal object.
    #And when every mamal created prints them out.
    for i in range(len(ID)):

        obj[i] = Mammal(ID[i], species[i], name[i], weight[i], width[i], breadth[i], height[i])
        mammal_list.append(obj[i])

    for object in mammal_list:
        print(object)

#If the animal wasn't too heavy, check if animals dimension are too big for trunk.
def check_size_of_trunk(car, mammal):

    if car.get_size_of_trunk() < float(mammal.size):

        print("Sorry mammal too big to fit into trunk...")
        return print("Trunk size was", car.get_size_of_trunk(), "m^3 and animal was", mammal.size, "m^3")

    else:
        return print("congratulations you managed to fit the mammal into car! ")

#Check if animals weight is bigger than cars maximum weight limit.
def check_car_max_load(car, mammal):

    if car.get_maximum_load() < int(mammal.weight):

        print("Sorry mammal is too heavy...")
        return print("Max weight was: ", car.get_maximum_load(), "Kg and animal weighted", mammal.weight, "Kg")

    else:
        print("Mammal not too heavy. ")
        check_size_of_trunk(car, mammal)

# First main creates all mamals. Then car object is created. Then dice is rolled.
#Dice value is compared to mamals ID values in mammal_list. Finally main runs weight and size
#validation.
def main():

    create_mammals()

    car = Car()

    car.set_make()
    car.set_model()
    car.set_milage()
    car.set_price()
    car.set_color()
    car.set_maximum_load()
    car.set_size_of_trunk()

    print(car)

    dice = Dice()
    dice.roll_the_dice()
    dice.get_side_up()

    for object in mammal_list:

        if object.id == dice.side_up:
            print("Selected animal: ")
            print(object)
            check_car_max_load(car, object)

main()

