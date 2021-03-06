# File name: Exercise1_7
# Author: Pekka Lehtola
# Description: Counts arithmetic progressions terms, sum of terms and the sum of squared terms.

def arithmetic_progression(maximum_value):

    #Setting up counters
    number_counter = 0
    sum_of_numbers = 0
    sum_of_numbers_squared = 0

    #Loops trought the numbers with steps of 2
    for i in range(2, maximum_value + 1, 2):

        if i % 2 == 0:
            number_counter += 1
            sum_of_numbers += i
            sum_of_numbers_squared += i ** 2

    print(number_counter)
    print(sum_of_numbers)
    print(sum_of_numbers_squared)
    return exit()

#Asks for user input
arithmetic_progression(int(input("Please insert maximum value: ")))
