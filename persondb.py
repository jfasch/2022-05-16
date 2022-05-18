from person import Person
import csv


class PersonDB:
    def __init__(self):
        self.persons = {}  # svnr -> Person

    def number_of_persons(self):
        return len(self.persons)

    def insert(self, person):
        if person.svnr in self.persons:
            raise DuplicateSVNRError(f'{person.svnr} already exists')
        self.persons[person.svnr] = person

    def update(self, person):
        # low hanging fruit: errors
        existing_person = self.persons.get(person.svnr)
        if existing_person is None:
            raise SVNRNotExist(f'{person.svnr} does not exist')
        if existing_person.firstname == person.firstname and existing_person.lastname == person.lastname:
            raise ExactDuplicateError(f'{person.svnr}: nothing to update')

        self.persons[person.svnr] = person
                
    def find(self, svnr):
        return self.persons.get(svnr)

    def read_from_csv(self, filename, encoding):
        f = open(filename, encoding=encoding)
        rdr = csv.reader(f, delimiter=';', quotechar='"')
        for svnr, firstname, lastname in rdr:
            self.insert(Person(svnr, firstname, lastname))

class DuplicateSVNRError(Exception):
    pass

class SVNRNotExist(Exception):
    pass

class ExactDuplicateError(Exception):
    pass
