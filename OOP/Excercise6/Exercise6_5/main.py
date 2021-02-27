# File name: main
# Author: Pekka Lehtola
# Description: Main function for exercise 6_3

from domestic_animals import *
from wild_animals import *

def dog_creating():

    dog = Dog()

    dog.set_id(1)
    dog.set_species("Dog")
    dog.set_name("Martti")
    dog.set_weight(60)
    dog.set_width(40)
    dog.set_breadth(70)
    dog.set_height(55)
    dog.set_noice("BArk")
    dog.set_diet("300g dog food twice a day.")
    dog.set_is_scent()

    print(dog)

def cat_creating():

    cat = Cat()

    cat.set_id(2)
    cat.set_species("Cat")
    cat.set_name("Liisa")
    cat.set_weight(13)
    cat.set_width(10)
    cat.set_breadth(26)
    cat.set_height(24)
    cat.set_noice("Meow")
    cat.set_training()
    cat.set_diet("One can of cat food three time a day")

    print(cat)

def bear_creation():

    bear = Bear()

    bear.set_id(3)
    bear.set_species("Bear")
    bear.set_name("Pooh")
    bear.set_weight(700)
    bear.set_width(80)
    bear.set_breadth(130)
    bear.set_height(99)
    bear.set_noice("Roar")
    bear.set_diet("One moose a day")
    bear.set_herbivore()
    bear.set_agression()
    bear.set_colour("Black")
    bear.set_likes_honey()

    print(bear)

def platypus_creation():

    platypus = Platypus()

    platypus.set_id(4)
    platypus.set_species("Platypus")
    platypus.set_name("Perry")
    platypus.set_weight(30)
    platypus.set_width(14)
    platypus.set_breadth(60)
    platypus.set_height(26)
    platypus.set_noice("GRRrr")
    platypus.set_diet("Plenty of lillypads")


    print(platypus)


dog_creating()
cat_creating()
bear_creation()
platypus_creation()