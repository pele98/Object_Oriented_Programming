# File:         cookie.py
# Author:
# Description:  Cookie class

# Cookie class with data attributes baked, frosting and frosting_list (Used to choose frosting.)
class Cookie:

    def __init__(self):

        self.baked = False
        self.frosting = None

        self.frosting_list = ["Vanilla", "Chocolate", "Mint"]

    # Sets cookies baked to True and prints out that cookie is baked.
    def bake_cookie(self, index):

        self.baked = True
        print(f"Cookie No.{index} baked")

    # Sets cookies frosting to random choice that is defined in main
    # Prints out cookie with index and chosen frosting.
    def frost_cookie(self, choice, index):

        self.frosting = self.frosting_list[choice]
        print(f"Cookie No.{index} frosted with {self.frosting_list[choice]}")

    def get_baked(self):
        return self.baked

    def get_frosting(self):
        return self.frosting

    #Printing function for Cookie class.
    def __str__(self):
        return f"""Cookie is baked {self.baked} and frosting is {self.frosting}"""