# File name: animals
# Author: Pekka Lehtola
# Description: Classes Wild_animal and Domestic_animal Inherited from Mammal class.

from mammal_class import *

#Inherits Wild_animals from Mammal class.
class Wild_animal(Mammal):

    #Wild animals have additional attributes Herbivore and Agression.
    def __init__(self):
        Mammal.__init__(self)
        self.is_herbivore = True
        self.is_agressive = False

    def set_herbivore(self):

        if self.is_herbivore:
            self.is_herbivore = False
        else:
            self.is_herbivore = True

    def set_agression(self):

        if self.is_agressive:
            self.is_agressive = False
        else:
            self.is_agressive = True

# Inherits Domestic_animal from Mammal class.
class Domestic_animal(Mammal):

    #Domestic animals have additional attributes Hairyness and Training.
    def __init__(self):
        Mammal.__init__(self)
        self.is_hairy = True
        self.is_trained = True

    def set_hairyness(self):

        if self.is_hairy:
            self.is_hairy = False
        else:
            self.is_hairy = True

    def set_training(self):

        if self.is_trained:
            self.is_trained = False
        else:
            self.is_trained = True