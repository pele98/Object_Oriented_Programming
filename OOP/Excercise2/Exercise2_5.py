#File name: Exercise2_5
#Author: Pekka Lehtola
#Description: Counts grade average from all students. New students can be added.


class Student:

    #Initializing student with attributes

    def __init__(self, name, grade):

        self.name = name
        self.grade = grade

class Class:

    #Setting up class named Class.

    def __init__(self, class_name):

        self.class_name = class_name
        self.sum_of_grades = 0
        self.class_average = 0
        self.students_in_class = []


    # Appends the list of students in class wit students name.
    # Calculates new grade sum with new students grade.
    # Calculates class average with new sum.

    def add_student_to_class(self, student):

        self.students_in_class.append(student.name)
        self.sum_of_grades += student.grade
        self.class_average = self.sum_of_grades / len(self.students_in_class)

    def print_average(self):

        return print(self.class_average)


def main():

    # Convert user input to Class object with user given name.

    user_input_for_class_name = str(input("Give name to the class: "))
    class_room = Class(user_input_for_class_name)

    while True:

        #Uses user input to navigate options.
        user_input = str(input("add students, class average or exit: "))

        if user_input == "add students":

            while True:

                new_students_name = input("Give name to the student or exit: ")

                #If the name is "exit" returns back to main function.
                if new_students_name == "exit":
                    break

                new_students_grade = int(input("Give a grade to the student: "))

                # Create new student object with user given name and grade.
                new_student = Student(new_students_name, new_students_grade)

                #Adds the new student to Class, calculate sum and class average
                class_room.add_student_to_class(new_student)

                #Printing confirmation of succesful addition and prints out current students in class room.
                print(new_student.name, "added to classroom ", class_room.class_name)
                print("Classroom consists from the following students", class_room.students_in_class)

        #Printing class average.
        elif user_input == "class average":

            class_room.print_average()

        #Ends program
        elif user_input == "exit":

            exit()

        else:

            continue

main()
