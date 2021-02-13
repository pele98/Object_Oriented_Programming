# File name: player_class
# Author: Pekka Lehtola
# Description: player_class with private attributes and str method.

class Player:

    def __init__(self, id, first_name, last_name):

        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name

    #__str__ method for clean printing
    def __str__(self):
        return f"""
        ID: {self.__id}
        First name: {self.__first_name}
        Last name: {self.__last_name}
        """

    #All of the set methods.
    def set_first_name(self):
        self.__first_name = input("Set a new first name for the player: ")
    def set_last_name(self):
        self.__last_name = input("Set a new last name for the player: ")
    def set_id(self):
        self.__id = int(input("Set a new id for the player:  "))

    #All of the get methods.
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_id(self):
        return self.__id