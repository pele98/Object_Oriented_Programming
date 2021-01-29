#File name: Exercise1_4
#Author: Pekka Lehtola
#Description: Reads user inputs until 0 is given. Prints out all negative integers.


# Defining main function
def reader():

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
        return print("Program ended.")

    #Prints out negative numbers
    elif user_given_int <= 0:
        print("Negative number: ", user_given_int)
        reader()

    else:
        reader()

reader()

