from persondb import PersonDB
import sys

filename = sys.argv[1]

PersonDB().read_from_csv(filename, encoding='cp1252')
