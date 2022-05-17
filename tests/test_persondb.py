from person import Person
#from persondb import PersonDB

import pytest


@pytest.mark.xfail
def test_basic():
    db = PersonDB()

    db.insert(Person('1037190666', 'Joerg', 'Faschingbauer'))
    db.insert(Person('1234250497', 'Caro', 'Faschingbauer'))
    db.insert(Person('234511061995', 'Johanna', 'Faschingbauer'))

    assert db.number_of_persons() == 3

    caro = db.find('1234250497')
    assert caro is not None
    assert caro.svnr == '1234250497'
    assert caro.firstname == 'Caro'
    assert caro.lastname == 'Faschingbauer'


    hmm = db.find('4567123456')
    assert hmm is None
