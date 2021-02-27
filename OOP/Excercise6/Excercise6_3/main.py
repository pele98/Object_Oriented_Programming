# File name: main
# Author: Pekka Lehtola
# Description: Main function for exercise 6_3

from mammal_class import Mammal

#Dog inherited from Mammal class
class Dog(Mammal):

    #Two new attributes noice and diet
    #Rest are inherited
    def __init__(self):
        Mammal.__init__(self)
        self.noice = "noice"
        self.diet = "diet"

    #Set and Get methods
    def set_noice(self):
        self.noice = str(input("Enter a noice for the animal: "))
    def set_diet(self):
        self.diet = str(input("Enter a diet for the animal: "))

    def get_noice(self):
        return self.noice
    def get_diet(self):
        return self.diet

    #Str function for clear output prints.
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

#Setting dog as object and giving it values.
dog = Dog()

dog.set_id()
dog.set_species()
dog.set_name()
dog.set_weight()
dog.set_width()
dog.set_breadth()
dog.set_height()
dog.set_diet()
dog.set_noice()

print(dog)
