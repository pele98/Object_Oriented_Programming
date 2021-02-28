# File name: domestic_animals
# Author: Pekka Lehtola
# Description: Dog and Cat classes inherited from Domestic_animals class.

from animals import *

# Inherits Dog from Domestic animals.
class Dog(Domestic_animal):

    def __init__(self):

        Domestic_animal.__init__(self)
        self.is_scent_dog = True

    # Calling this function changes the boolean value.
    def set_is_scent(self):

        if self.is_scent_dog:
            self.is_scent_dog = False
        else:
            self.is_scent_dog = True

    # Defining Dog printing.
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
    Diet is: {self.diet}
    Is hairy: {self.is_hairy}
    Is trained: {self.is_trained}
    Is scent dog: {self.is_scent_dog}
        """

# Inherits Cat from Domestic animals.
class Cat(Domestic_animal):
    
    def __init__(self):
        Domestic_animal.__init__(self)
        self.is_agressive = True

    # Calling this function changes the boolean value.
    def set_agression(self):

        if self.is_agressive:
            self.is_agressive = False
        else:
            self.is_agressive = True

    #Defining Cat printing.
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
    Diet is: {self.diet}
    Is_hairy: {self.is_hairy}
    Is trained: {self.is_trained}
    Is agressive: {self.is_agressive}
        """
