# File name: main
# Author: Pekka Lehtola
# Description: Main function for Excersice5_6

from mammal_class import *
from student_class import *

#Student objects
matti = Student(123441, "Matti", "Koskinen")
pekka = Student(551212, "Pekka", "Lehtola")
linda = Student(489992, "Linda", "Laine")

#List of student objects
#List of students names
students = [matti, pekka, linda]
students_name = [matti.get_first_name(), pekka.get_first_name(), linda.get_first_name()]

#Mammal objects
dog = Mammal(1, "dog", "Pate", 55, 30, 90, 80)
cat = Mammal(2, "cat", "Snuffles", 20, 12, 40, 35)
rabbit = Mammal(3, "rabbit", "Fluffy", 7, 8, 15, 15)

#List of mammal objects
mammals = [dog, cat, rabbit]

#Dictionary of mammals, with key value as students first name.
students_dict = dict(zip(students_name, mammals))

id = 0

#For loop of dictionary object
#Id used to print students from the list.
for key, object in students_dict.items():
    print("Student information:")
    print(students[id])
    id += 1

    print(key ,"has the following mammal:" )
    print(object)