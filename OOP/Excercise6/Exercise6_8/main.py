# File name: main
# Author: Pekka Lehtola
# Description: Main file for exercise6_8

#Importing function for creating each animal and creator for student and teacher.
from animal_creation import *
from person_creation import *

#Creates student pekka and teacher sanna that are global objects
student_creation()
teacher_creation()

#Creates each animal and set them as global objects
dog_creating()
cat_creating()
bear_creation()
platypus_creation()

#Sets up Pekkas animals
pekka.set_domestic_animal(dog)
pekka.set_wild_animal(bear)

#Sets up Sannas animals
sanna.set_domestic_animal(cat)
sanna.set_wild_animal(platypus)

#Frist prints Pekka object and then his animal attributes
print(pekka)
print("    Pekka has the following animals: ")
print(pekka.get_domestic_animal())
print(pekka.get_wild_animal())

#First prints Sanna object and then her animals.
print(sanna)
print("    Sanna has the following animals: ")
print(sanna.get_domestic_animal())
print(sanna.get_wild_animal())