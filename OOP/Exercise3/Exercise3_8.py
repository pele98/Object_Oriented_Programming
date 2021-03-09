# File name: Exercise3_8
# Author: Pekka Lehtola
# Description: Creates cellphone class from user inputs

class Cellphone:

    def __init__(self):

        self.manufact = ""
        self.model = ""
        self.retail_price = 0

    def set_manufact(self):

        self.manufact = str(input("Enter the manufacturer : "))

    def set_model(self):

        self.model = str(input("Enter the model number : "))

    def set_retail_price(self):

        self.retail_price = float(input("Enter the retail price : "))

    def get_manufact(self):

            return print("Manufacturer:", self.manufact)

    def get_model_number(self):
        return print("Model number:", self.model)

    def get_retail_price(self):
        return print("Retail price:", self.retail_price)

def main():

    my_cellphone = Cellphone()

    my_cellphone.set_manufact()
    my_cellphone.set_model()
    my_cellphone.set_retail_price()

    print("Here is the data that you provided :")

    my_cellphone.get_manufact()
    my_cellphone.get_model_number()
    my_cellphone.get_retail_price()

main()