# File name: student
# Author: Pekka Lehtola
# Description: Student class


# Student class with attributes first name, last name, student ID and pet list
class Student:

    def __init__(self, first_name, last_name, student_ID):

        self.__fist_name = first_name
        self.__last_name = last_name
        self.__student_ID = student_ID
        self.__pets = []

    def set_first_name(self):
        self.__fist_name = input("First name: ")

    def get_first_name(self):
        return self.__fist_name

    def set_last_name(self):
        self.__last_name = input("Last name: ")

    def get_last_name(self):
        return self.__last_name

    def set_student_ID(self):
        self.__student_ID = input("Student ID: ")

    def get_student_ID(self):
        return self.__student_ID

    # Adds pets to pet list only if pet is not owned and is actually a pet.
    # Prints out successful pet addition.
    def add_pets(self, pet):

        try:
            if pet.get_owner() == None:

                self.__pets.append(pet)
                pet.set_owner(self.__fist_name)
                print(pet.get_name() + "s", "owner is now", self.get_first_name())

            else:
                print("Pet allready owned.")

        except:
            return print("Are you trying to add a student as a pet...")

    #Removes pet from pet list and sets pets owner as None
    def remove_pets(self, pet_name):

        for pets in self.__pets:

            if pets.get_name() == pet_name:
                print(pets.get_name(), "was removed from", self.get_first_name())
                pets.set_owner(None)
                self.__pets.remove(pets)

    #Prints out every owned pet.
    def print_pets(self):
        print(self.get_first_name() + "s", "pets:")
        for pet in self.__pets:
            print(pet)

    def __str__(self):

        return f"""
    Fist name:  {self.get_first_name()}
    Last name:  {self.get_last_name()}
    Student ID: {self.get_student_ID()}
    """
