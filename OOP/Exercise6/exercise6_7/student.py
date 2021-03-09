# File name: student
# Author: Pekka Lehtola
# Description: Student class inherited from OOP_course class

from participant_of_OOP_course import *

#Student class inherited from OOP_course
class Student(OOP_course):

    #Student has additional attributes student number and grade
    def __init__(self):

        OOP_course.__init__(self)
        self.__student_number = "000000"
        self.__grade = "N/A"

    def set_student_number(self, student_numer):
        self.__student_number = student_numer

    def set_grade(self, grade):
        self.__grade = grade

    def get_student_number(self):
        return self.__student_number

    def get_grade(self):
        return self.__grade

    def __str__(self):
        return f"""
        
    Name: {self.get_name()}
    Date of birth: {self.get_date_of_birth()}
    Coding_level: {self.coding_level} 
    Student number: {self.get_student_number()}
    Grade: {self.get_grade()} """