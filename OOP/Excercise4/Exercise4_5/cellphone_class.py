# File name: Cellphone class
# Author: Pekka Lehtola
# Description: Cellphone class

class Cellphone:

    def __init__(self):

        self.__manufact = "N/A"
        self.__model = "N/A"
        self.__retail_price = 0
        self.__id = 0

    def __str__(self):
        return f"""
    Manufacturer: {self.__manufact}
    Model number: {self.__model}
    Retail price: {self.__retail_price}
    Cellphone ID: {self.__id} 
    """


    def set_manufact(self):

        self.__manufact = str(input("Enter the manufacturer : "))

    def set_model(self):

        self.__model = str(input("Enter the model number : "))

    def set_retail_price(self):

        self.__retail_price = float(input("Enter the retail price : "))

    def set_id(self, id):

        self.__id = id

    def get_manufact(self):

        return print("Manufacturer:", self.__manufact)

    def get_only_manufact(self):

        return print(self.__manufact)

    def get_model_number(self):
        return print("Model number:", self.__model)

    def get_retail_price(self):
        return print("Retail price:", self.__retail_price)

    def get_id(self):
        return print("Cellphone ID: ", self.__id)
