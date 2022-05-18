from persondb import PersonDB
import sys


sqlname = sys.argv[1]

db = PersonDB()
db.read_from_sqlite3(sqlname)

json_string = db.export_to_json()

print(json_string)
