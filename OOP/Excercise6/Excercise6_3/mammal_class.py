# File name: mammal_class
# Author: Pekka Lehtola
# Description: class for creating mammals

class Mammal:

    def __init__(self):

        self.id = "ID"
        self.species = "species"
        self.name = "name"
        self.weight = "weight"
        self.width = 1
        self.breadth = 1
        self.height = 1
        self.size =  float((self.width * self.breadth * self.height) / (1000 * 1000)) #Calculates cm^3 and converts it to m^3

    #str method for clean output printing with correct units
    def __str__(self):

        return f"""
    ID: {self.id}
    Species: {self.species}
    Name: {self.name}
    Size {self.size} m^3
    Weight {self.weight} Kg
    Width {self.width} cm
    Breadth {self.breadth} cm
    Height {self.height} cm
        """

    def set_id(self):
        self.id = int(input("Enter an id for the animal: "))
    def set_species(self):
        self.species = (input("Enter a species for the animal: "))
    def set_name(self):
        self.name = str(input("Enter a name for the animal: "))
    def set_weight(self):
        self.weight = int(input("Enter a weight for the animal: "))
    def set_width(self):
        self.width = int(input("Enter a width for the animal: "))
        self.size = float((self.width * self.breadth * self.height) / (1000 * 1000))
    def set_breadth(self):
        self.breadth = int(input("Enter a breadth for the animal: "))
        self.size = float((self.width * self.breadth * self.height) / (1000 * 1000))
    def set_height(self):
        self.height = int(input("Enter a height for the animal: "))
        self.size = float((self.width * self.breadth * self.height) / (1000 * 1000))

    def get_id(self):
        return self.id
    def get_species(self):
        return self.species
    def get_name(self):
        return self.name
    def get_weight(self):
        return self.weight
    def get_width(self):
        return self.width
    def get_breadth(self):
        return self.breadth
    def get_height(self):
        return self.height
