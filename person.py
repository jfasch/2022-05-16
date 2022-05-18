import re


svnr_pattern = re.compile(r'^(\d|[A-Z])(\d|[A-Z])(\d|[A-Z])(\d|[A-Z])\d\d\d\d\d\d$')

class Person:
    def __init__(self, svnr, firstname, lastname):
        # if type(svnr) is not str:
        #     raise InvalidSVNR(f'{svnr} is not str')
        # if len(svnr) != 10:
        #     raise InvalidSVNR(f'{svnr} is not 10 characters long')
        # try:
        #     svnr_as_int = int(svnr)
        #     if svnr_as_int < 0:
        #         raise InvalidSVNR(f'{svnr} is negative')
        # except ValueError:
        #     raise InvalidSVNR(f'{svnr} is not numerical')

        if type(svnr) is not str:
            raise InvalidSVNR(f'{svnr} must be str')

        match = svnr_pattern.search(svnr)
        if not match:
            raise InvalidSVNR(f'{svnr} is not valid')

        self.svnr = svnr
        self.firstname = firstname
        self.lastname = lastname

    def invert(self):
        self.firstname = self.firstname[::-1]
        self.lastname = self.lastname[::-1]

class InvalidSVNR(Exception):
    pass
