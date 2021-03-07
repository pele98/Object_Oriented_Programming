# File:         main.py
# Author:       
# Description:  Main function for exercise 7.5

from pet import *
from student import *

# Main function for testing classes.
def main():

    # Creating student and pet objects.
    pekka = Student("Pekka", "Lehtola", 140124)
    mikko = Student("Mikko", "Lehtola", 198112)

    sampo = Pet("Cat", "Sampo")
    mauno = Pet("Dog", "Mauno")

    # Adding pets to owners and trying to add Student as a pet.
    pekka.add_pets(sampo)
    mikko.add_pets(mauno)
    pekka.add_pets(mikko)
    print()

    # Prints out Students and Pets states.
    print("Student printing:")

    print(pekka)
    print(mikko)

    print("Pet printing")

    print(sampo)
    print(mauno)

    # Printing out Pekkas and Mikkos pets.
    pekka.print_pets()

    mikko.print_pets()

    print("Trying to add allready owned pet")
    print()
    pekka.add_pets(mauno)
    print()

    print("Removing Mauno from Mikko and trying to add it again")
    print()

    mikko.remove_pets("Mauno")
    mikko.print_pets()
    print()

    pekka.add_pets(mauno)
    pekka.print_pets()


main()
