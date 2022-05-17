class Person:
    def __init__(self, svnr, firstname, lastname):
        self.svnr = svnr
        self.firstname = firstname
        self.lastname = lastname

    def invert(self):
        self.firstname = self.firstname[::-1]
        self.lastname = self.lastname[::-1]
