# File name: Cellphone_main
# Author: Pekka Lehtola
# Description: Cellphone class main function

from cellphone_class import Cellphone

def main():

    my_cellphone = Cellphone()

    my_cellphone.set_manufact()
    my_cellphone.set_model()
    my_cellphone.set_retail_price()
    my_cellphone.set_id()

    print("Here is the data that you provided :")

    my_cellphone.get_manufact()
    my_cellphone.get_model_number()
    my_cellphone.get_retail_price()
    my_cellphone.get_id()

    print(my_cellphone)

main()