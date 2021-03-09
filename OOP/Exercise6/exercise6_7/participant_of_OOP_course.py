# File name: participants_of_OOP_course
# Author: Pekka Lehtola
# Description: OOP_course class with common attributes.

#OOP course class
class OOP_course:

    #Common attributes in course name, date of birth and coding level.
    def __init__(self):

        self.__name = "Jokunen"
        self.__date_of_birth = "01012000"
        self.coding_level = 1

    def set_name(self, name):
        self.__name = name

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def set_coding_level(self, coding_level):
        self.coding_level = coding_level

    def get_name(self):
        return self.__name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_coding_level(self):
        return self.coding_level

    def __str__(self):

        return f"""
    Name: {self.__name}
    Date of birth: {self.__date_of_birth}
    Coding_level: {self.coding_level} """