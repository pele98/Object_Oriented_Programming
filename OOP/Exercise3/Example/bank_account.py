#File name: bank_account
#Author: Pekka Lehtola
#Description: Example code from Anne


class Bank_account:

    def __init__(self, bal, owner):

        self.__balance = bal
        self.__owner = owner

    def deposit(self, ammount):

        self.__balance += ammount

    def withdraw(self, ammount):

        if self.__balance >= ammount:
            self.__balance -= ammount

        else:
            print("Error: Insufficient funds.")

    def get_ballance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    # The __str__ method returns a string
    # indicating the object's state.

    def __str__(self):

        return f""" Balance: {self.__balance} Owner: {self.__owner}"""