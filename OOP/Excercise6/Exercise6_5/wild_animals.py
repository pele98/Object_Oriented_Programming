from animals import *

class Bear(Wild_animal):

    def __init__(self):

        Wild_animal.__init__(self)
        self.colour = "Brown"
        self.likes_honey = True

    def set_colour(self, colour):
        self.colour = colour

    def set_likes_honey(self):

        if self.likes_honey:
            self.likes_honey = False
        else:
            self.likes_honey = True

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
    is herbivore: {self.is_herbivore}
    is agressive: {self.is_agressive}
    Colour is: {self.colour}
    Likes honey: {self.likes_honey}
        """

class Platypus(Wild_animal):

    def __init__(self):

        Wild_animal.__init__(self)
        self.is_the_best_animal = True

    def set_is_the_best_animal(self):

        if self.is_the_best_animal:
            self.is_the_best_animal = True
        else:
            self.is_the_best_animal = True

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
    is herbivore: {self.is_herbivore}
    is agressive: {self.is_agressive}
    Is the best animal: {self.is_the_best_animal}
        """
