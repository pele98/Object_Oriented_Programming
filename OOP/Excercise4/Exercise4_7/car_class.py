# File name: car_class
# Author: Pekka Lehtola
# Description: car_class with private attributes and str method.

class Car:

    def __init__(self):

        self.__make = "make"
        self.__model = "model"
        self.__mileage = "mileage"
        self.__price = "price"
        self.__color = "color"
        self.__maximum_load = "maximum_load"
        self.__trunk_size = "trunk_size"

    #__str__ method for clean printing
    def __str__(self):
        return f"""
        Make: {self.__make}
        Model: {self.__model}
        Mileage: {self.__mileage} Km
        Price: {self.__price} $
        Color: {self.__color}
        Maximum load {self.__maximum_load} Kg
        Size of trunk {self.__trunk_size} m^3
        """

    #All of the set methods.
    def set_make(self):
        self.__make = input("Set make for the car: ")
    def set_model(self):
        self.__model = input("Set model for the car: ")
    def set_milage(self):
        self.__mileage = int(input("Set mileage for the car: "))
    def set_price(self):
        self.__price = float(input("Set price for the car: "))
    def set_color(self):
        self.__color = input("Set color for the car: ")
    def set_maximum_load(self):
        self.__maximum_load = input("Set maximum load for the car: ")
    def set_size_of_trunk(self):
        self.__trunk_size = input("Set the size of the trunk: ")

    #All of the get methods.
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_milage(self):
        return self.__mileage
    def get_price(self):
        return self.__price
    def get_color(self):
        return self.__color
    def get_maximum_load(self):
        return self.__maximum_load
    def get_size_of_trunk(self):
        return self.__trunk_size