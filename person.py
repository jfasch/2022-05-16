class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def invert(self):
        self.firstname = self.firstname[::-1]
        self.lastname = self.lastname[::-1]

    @staticmethod
    def marry(l, r):
        lastname = l.lastname
        l.lastname += '-' + r.lastname
        r.lastname += '-' + lastname
