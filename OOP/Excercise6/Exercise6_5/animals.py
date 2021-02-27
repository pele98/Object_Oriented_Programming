
from mammal_class import *

class Wild_animal(Mammal):

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

class Domestic_animal(Mammal):

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