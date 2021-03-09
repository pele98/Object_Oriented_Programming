# File name: main
# Author: Pekka Lehtola
# Description: Main file for exercise6_7

from student import *
from teacher import *

#Creates student object from Student class
def student_creation():

    pekka = Student()

    #Attribute values are set here.
    pekka.set_name("Pekka")
    pekka.set_date_of_birth("04021998")
    pekka.set_coding_level("Good")
    pekka.set_student_number("199321")
    pekka.set_grade(5)

    #Object printing
    print(pekka)

#Creates Teacher object from Teacher class
def teacher_creation():

    sanna = Teacher()

    sanna.set_name("Sanna")
    sanna.set_date_of_birth("03031990")
    sanna.set_coding_level("Exelent")
    sanna.set_salary(3200)
    sanna.set_years_of_teaching(8)

    print(sanna)

#Function activation happens here.
student_creation()
teacher_creation()