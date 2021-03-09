# File name: Exercise1_9
# Author: Pekka Lehtola
# Description: Returns random number between 1 and 6

import random
def rand_number_from_one_to_six():
    return random.randint(1,6)

for i in range(15):
    print(rand_number_from_one_to_six())