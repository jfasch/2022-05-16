from person import Person
import csv
import sqlite3
import json


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

    def read_from_sqlite3(self, filename):
        connection = sqlite3.connect(filename)
        cursor = connection.cursor()

        resultset = cursor.execute('select * from persons;')
        for svnr, firstname, lastname in resultset:
            self.insert(Person(svnr, firstname, lastname))

    def export_to_json(self):
        l = []
        for p in self.persons.values():
            p_dict = {
                'svnr': p.svnr,
                'firstname': p.firstname,
                'lastname': p.lastname,
            }
            l.append(p_dict)

        return json.dumps(l)

    def read_from_json(self, filename):
        f = open(filename)
        json_string = f.read()
        person_dict_list = json.loads(json_string)

        for person_dict in person_dict_list:
            svnr = person_dict['svnr']
            firstname = person_dict['firstname']
            lastname = person_dict['lastname']

            self.insert(Person(svnr, firstname, lastname))


class DuplicateSVNRError(Exception):
    pass

class SVNRNotExist(Exception):
    pass

class ExactDuplicateError(Exception):
    pass
