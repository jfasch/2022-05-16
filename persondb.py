class PersonDB:
    def __init__(self):
        self.persons = []

    def number_of_persons(self):
        return len(self.persons)

    def insert(self, person):
        self.persons.append(person)
        
    def find(self, svnr):
        for p in self.persons:
            if p.svnr == svnr:
                return p
        else:
            return None
