class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def invert(self):
        self.firstname = self.firstname[::-1]
        self.lastname = self.lastname[::-1]

    def marry(self, other):
        self.lastname += '-' + other.lastname
