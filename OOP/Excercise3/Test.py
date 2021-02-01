
class Test():

    def __init__(self):

        self.__private = ""
        self.public = "Test"

    def set_private(self, set):

        self.__private = set

    def get_private(self):
        print(self.__private)

my_test = Test()

my_test.set_private("Test")
my_test.get_private()

my_test.__private = "1234"
print(my_test.__private)
my_test.get_private()

