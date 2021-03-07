# File name: pet
# Author: Pekka Lehtola
# Description: Pet class

# Pet class with attributes species, name and owner.
class Pet:

    def __init__(self, species, name):

        self.__species = species
        self.__name = name

        self.__owner = None

    def set_species(self):

        self.__species = input("Set species: ")

    def get_species(self):
        return self.__species

    def set_name(self):

        self.__name = input("Set name: ")

    def get_name(self):

        return self.__name

    def set_owner(self, owner):

        self.__owner = owner

    def get_owner(self):

        return (self.__owner)

    def __str__(self):

        return f"""
    Pets name:  {self.__name}
    Species:    {self.__species}
    Owner:      {self.__owner}
    """