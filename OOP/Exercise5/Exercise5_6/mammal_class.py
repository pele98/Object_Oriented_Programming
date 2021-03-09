# File name: mammal_class
# Author: Pekka Lehtola
# Description: class for creating mammals

class Mammal:

    def __init__(self, ID, species, name, weight, width, breadth, height):

        self.id = ID
        self.species = species
        self.name = name
        self.size =  float((width*breadth*height) / (1000 * 1000)) #Calculates cm^3 and converts it to m^3
        self.weight = weight
        self.width = width
        self.breadth = breadth
        self.height = height

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

    def set_name(self):
        self.name = str(input("Enter a name for the animal: "))

    def get_weight(self):
        return self.weight
    def get_species(self):
        return self.species
    def get_id(self):
        return self.id