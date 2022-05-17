import sys
import csv
from person import Person


filename = sys.argv[1]
svnr_search = sys.argv[2]

persons = []

f = open(filename, encoding='cp1252')
rdr = csv.reader(f, delimiter=';', quotechar='"')
for svnr, firstname, lastname in rdr:
    p = Person(svnr, firstname, lastname)
    persons.append(p)

for p in persons:
    if p.svnr == svnr_search:
        print(f'SVNR: {p.svnr}, Firstname: {p.firstname}, Lastname: {p.lastname}')
        break
else:
    print('not found')
