import sys
import csv
from person import Person
from persondb import PersonDB


filename = sys.argv[1]
svnr_search = sys.argv[2]

db = PersonDB()

f = open(filename, encoding='cp1252')
rdr = csv.reader(f, delimiter=';', quotechar='"')
for svnr, firstname, lastname in rdr:
    db.insert(Person(svnr, firstname, lastname))

found = db.find(svnr_search)
if found:
    print(f'SVNR: {found.svnr}, Firstname: {found.firstname}, Lastname: {found.lastname}')
else:
    print('not found')
