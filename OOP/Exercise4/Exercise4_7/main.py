# File name: main
# Author: Pekka Lehtola
# Description: Main function for exercise 4_7

from car_class import Car

def main():

    honda = Car()

    honda.set_make()
    honda.set_model()
    honda.set_milage()
    honda.set_price()
    honda.set_color()
    honda.set_maximum_load()
    honda.set_size_of_trunk()

    print(honda)

main()