from animals import *

class Dog(Domestic_animal):

    def __init__(self):

        Domestic_animal.__init__(self)
        self.is_scent_dog = True

    def set_is_scent(self):

        if self.is_scent_dog:
            self.is_scent_dog = False
        else:
            self.is_scent_dog = True

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

class Cat(Domestic_animal):
    
    def __init__(self):
        Domestic_animal.__init__(self)
        self.is_agressive = True

    def set_agression(self):

        if self.is_agressive:
            self.is_agressive = False
        else:
            self.is_agressive = True

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
