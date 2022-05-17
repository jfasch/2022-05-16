from person import Person
import csv


class PersonDB:
    def __init__(self):
        self.persons = {}  # svnr -> Person

    def number_of_persons(self):
        return len(self.persons)

    def insert(self, person):
        self.persons[person.svnr] = person
        
    def find(self, svnr):
        return self.persons.get(svnr)

    def read_from_csv(self, filename, encoding):
        f = open(filename, encoding=encoding)
        rdr = csv.reader(f, delimiter=';', quotechar='"')
        for svnr, firstname, lastname in rdr:
            self.persons[svnr] = Person(svnr, firstname, lastname)

