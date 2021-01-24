#File name: Exercise2_3
#Author: Pekka Lehtola
#Description: Gives grade based on accepted exercises.

class Grading_algorithm:

    # __init__ method intializes data attributes to 0

    def __init__(self):

        self.accepted_exercises = 0
        self.grade = 0


    # num_of_exercises checks if the number of accepted exercises is between 0 and 13
    # if the number is unacceptable the method tells the user whats wrong with the number.
    # method sets number of accepted exercises to given number.

    def num_of_exercises(self, number_of_accepted_exercises):

        if number_of_accepted_exercises < 0:
            self.accepted_exercises = number_of_accepted_exercises
            return print("Number cant be smaller than 0")

        elif number_of_accepted_exercises > 13:
            self.accepted_exercises = number_of_accepted_exercises
            return print("Number cant be greater than 13")

        else:
            self.accepted_exercises =  number_of_accepted_exercises


    #If number of accepted exercises is in range 0 to 9 method sets the grade to 0.
    #If the number is in grading scale dictionary method sets grade with the dictionary.
    #if the number of accepted exercises is anything else, the grade is set as "Undefined".

    def grading(self):

        grading_scale = {13:5, 12:4, 11:3, 10:2, 9:1}

        if self.accepted_exercises in grading_scale:

            self.grade = grading_scale[self.accepted_exercises]
            return print("Your grade is", self.grade, end="\n\n")

        elif self.accepted_exercises in range(0, 9):
            self.grade = 0
            return print("Your grade is", self.grade, end="\n\n")

        else:
            self.grade = "Undefined"
            return print("Your grade is", self.grade, end="\n\n")


#Main function that takes the number of accepted exercises from user.

def main():

    my_grade = Grading_algorithm()

    try:
        my_grade.num_of_exercises(int(input("Input the number of accepted exercises: ")))

    except:
        return print("Value error :( ", end="\n\n")
        
    my_grade.grading()

    

while True:

    main()

