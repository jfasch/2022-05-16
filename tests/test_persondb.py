from person import Person
from persondb import PersonDB

import pytest


def test_basic():
    db = PersonDB()

    assert db.number_of_persons() == 0

    joerg = Person('1037190666', 'Joerg', 'Faschingbauer')
    caro = Person('1234250497', 'Caro', 'Faschingbauer')
    johanna = Person('234511061995', 'Johanna', 'Faschingbauer')
    
    db.insert(joerg)
    db.insert(caro)
    db.insert(johanna)

    assert db.number_of_persons() == 3

    caro = db.find('1234250497')
    assert caro is not None
    assert caro.svnr == '1234250497'
    assert caro.firstname == 'Caro'
    assert caro.lastname == 'Faschingbauer'


    hmm = db.find('4567123456')
    assert hmm is None

def test_csv_basic():
    db = PersonDB()
    db.read_from_csv('data/standesregister.csv', encoding='cp1252')

    caro = db.find('1234250497')
    assert caro is not None
    assert caro.svnr == '1234250497'
    assert caro.firstname == 'Caro'
    assert caro.lastname == 'Faschingbauer'
    
