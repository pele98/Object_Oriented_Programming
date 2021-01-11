#File name: Int_and_Str_lst
#Author: Pekka Lehtola
#Description: Prints a list of numbers inserted by user, prints a list of strings inserted by user and
#             prints number list filled with random numbers.

#importing random
import random

#creating the two lists.
intlst = []
strlst = []

#appending lists by user inputs.
for i in range(10):
    x = int(input("Insert an integer: "))
    intlst.append(x)
for i in range(10):
    y = str(input("Insert a string: "))
    strlst.append(y)

#printing lists
print(intlst)
print(strlst)

#Replaces numbers in list with random numbers between 0 and 100
for i in range(len(intlst)):
    intlst[i] = random.randint(0,100)

print(intlst)