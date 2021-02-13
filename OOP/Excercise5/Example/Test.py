
class Test:

    def __init__(self):

        self.test = "Test"

    def __str__(self):

        return f""" {self.test} """

test = Test()

test.__str__()

print(test, "2")