import sys
from person import Person
from persondb import PersonDB


filename = sys.argv[1]
svnr_search = sys.argv[2]

db = PersonDB()
db.read_from_sqlite3(filename)

found = db.find(svnr_search)
if found:
    print(f'SVNR: {found.svnr}, Firstname: {found.firstname}, Lastname: {found.lastname}')
else:
    print('not found')
