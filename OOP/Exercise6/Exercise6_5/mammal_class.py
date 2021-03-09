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
        self.noice = ""
        self.diet = ""

    #str method for clean output printing with correct units
    def __str__(self):

        return f"""
    ID: {self.id}
    Species: {self.species}
    Name: {self.name}
    Size: {self.size} m^3
    Weight: {self.weight} Kg
    Width: {self.width} cm
    Breadth: {self.breadth} cm
    Height: {self.height} cm
    Noice: {self.noice}
    Diet is {self.diet}
        """

    def set_id(self, id):
        self.id = int(id)
    def set_species(self, species):
        self.species = species
    def set_name(self, name):
        self.name = name
    def set_weight(self, weight):
        self.weight = int(weight)
    def set_width(self, width):
        self.width = int(width)
        self.size = float((self.width * self.breadth * self.height) / (1000 * 1000))
    def set_breadth(self, breadth):
        self.breadth = int(breadth)
        self.size = float((self.width * self.breadth * self.height) / (1000 * 1000))
    def set_height(self, height):
        self.height = int(height)
        self.size = float((self.width * self.breadth * self.height) / (1000 * 1000))
    def set_noice(self, noice):
        self.noice = noice
    def set_diet(self, diet):
        self.diet = diet

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
    def get_noice(self):
        return self.noice
    def get_diet(self):
        return self.diet
