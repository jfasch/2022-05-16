class PersonDB:
    def __init__(self):
        self.persons = {}  # svnr -> Person

    def number_of_persons(self):
        return len(self.persons)

    def insert(self, person):
        self.persons[person.svnr] = person
        
    def find(self, svnr):
        return self.persons.get(svnr)
