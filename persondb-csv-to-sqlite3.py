import sys
import sqlite3
from persondb import PersonDB


csvname = sys.argv[1]
sqlname = sys.argv[2]


csvdb = PersonDB()
csvdb.read_from_csv(csvname, encoding='cp1252')

connection = sqlite3.connect(sqlname)
cursor = connection.cursor()

for person in csvdb.persons.values():
    # print(f'SVNR: {person.svnr}, Firstname: {person.firstname}, Lastname: {person.lastname}')

    cursor.execute(f'insert into persons values ("{person.svnr}", "{person.firstname}", "{person.lastname}");')

connection.commit()
