#File name: Exercise1_5
#Author: Pekka Lehtola
#Description: Reads user inputs until 0 is given. Prints out all negative integers. Counts amount of even numbers.

even_number_counter = 0

# Defining main function
def reader():

    global even_number_counter

    #Takes user input
    user_given_int = input("Insert an integer: ")

    #Checks if input is integer
    try:
        val = int(user_given_int)
    except ValueError:
        print("That is not an integer, please insert an integer.")
        reader()

    user_given_int = int(user_given_int)

    #if number is 0 program ends
    if user_given_int == 0:
        return print("Program ended. Number of even numbers were:", even_number_counter)

    #Prints out negative numbers
    elif user_given_int <= 0:
        print("Negative number: ", user_given_int)
        reader()

    elif user_given_int % 2 == 0:
        even_number_counter += 1
        reader()

    else:
        reader()

reader()