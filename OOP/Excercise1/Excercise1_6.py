#File name: Exercise1_6
#Author: Pekka Lehtola
#Description: Reads user inputs until 0 is given. Prints out all negative integers. Counts amount of even numbers.

even_number_counter = 0
sum_of_numbers_divisible_by_3 = 0

# Defining main function
def reader():

    global even_number_counter, sum_of_numbers_divisible_by_3

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
        print("Program ended. Number of even numbers were:", even_number_counter, ", Sum of numbers divisible by 3 is:",
              sum_of_numbers_divisible_by_3)
        return exit()


    #Prints out negative numbers
    elif user_given_int <= 0:
        print("Negative number: ", user_given_int)
        reader()

#Checks if number is divisible by 2
    elif user_given_int % 2 == 0:
        even_number_counter += 1

        # Checks if number is divisible by 3
        if user_given_int % 3 == 0:
            sum_of_numbers_divisible_by_3 += user_given_int
            reader()

        reader()


    else:
        reader()

reader()