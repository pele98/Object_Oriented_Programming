# File name: teacher
# Author: Pekka Lehtola
# Description: Teacher class inherited from OOP_course class

from participant_of_OOP_course import *

#Teacher class inherited from OOP_course
class Teacher(OOP_course):

    #Teacher has additional attributes salary and years of teaching.
    def __init__(self):
        OOP_course.__init__(self)
        self.__salary = 0
        self.years_of_teaching = 0

    def set_salary(self, salary):
        self.__salary = salary

    def set_years_of_teaching(self, years_of_teaching):
        self.years_of_teaching = years_of_teaching

    def get_salary(self):
        return self.__salary

    def get_years_of_teaching(self):
        return self.years_of_teaching

    def __str__(self):

        return f"""
    Name: {self.get_name()}
    Date of birth: {self.get_date_of_birth()}
    Coding_level: {self.coding_level}
    Salary: {self.get_salary()}
    Years of teaching: {self.years_of_teaching} """