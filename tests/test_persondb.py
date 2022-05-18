from person import Person
from persondb import PersonDB, DuplicateSVNRError, SVNRNotExist, ExactDuplicateError

import pytest


def test_basic():
    db = PersonDB()

    assert db.number_of_persons() == 0

    joerg = Person('1037190666', 'Joerg', 'Faschingbauer')
    caro = Person('1234250497', 'Caro', 'Faschingbauer')
    johanna = Person('2345110695', 'Johanna', 'Faschingbauer')
    
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

def test_csv_basic(tmpdir):
    # create file -> "fixture"
    f = open(tmpdir / 'test.csv', 'w')
    f.write('\n'.join([
        '1037190666;Joerg;Faschingbauer',
        '1234250497;Carolin;Faschingbauer',
        ]))
    f.close()

    # test ...
    db = PersonDB()
    db.read_from_csv(tmpdir / 'test.csv', encoding='cp1252')

    caro = db.find('1234250497')
    assert caro is not None
    assert caro.svnr == '1234250497'
    assert caro.firstname == 'Carolin'
    assert caro.lastname == 'Faschingbauer'
    
def test_csv_duplicate(tmpdir):
    # create file -> "fixture"
    f = open(tmpdir / 'test.csv', 'w')
    f.write('\n'.join([
        '1037190666;Joerg;Faschingbauer',
        '1037190666;Hansjoerg DI;Faschingbauer',
        ]))
    f.close()

    # test ...
    db = PersonDB()
    try:
        db.read_from_csv(tmpdir / 'test.csv', encoding='cp1252')
        assert False
    except DuplicateSVNRError:
        pass
    
def test_duplicate_svnr():
    db = PersonDB()

    joerg = Person('1037190666', 'Joerg', 'Faschingbauer')
    db.insert(joerg)
    try:
        db.insert(Person('1037190666', 'Hansjoerg', 'Faschingbauer'))
        assert False
    except DuplicateSVNRError as e:
        pass

def test_update_sunnycase():
    db = PersonDB()

    db.insert(Person('1037190666', 'Joerg', 'Faschingbauer'))
    db.update(Person('1037190666', 'Hansjoerg, DI', 'Faschingbauer'))

    found = db.find('1037190666')
    assert found.svnr == '1037190666'
    assert found.firstname == 'Hansjoerg, DI'
    assert found.lastname == 'Faschingbauer'

def test_update_notexist():
    db = PersonDB()

    try:
        db.update(Person('1234190666', 'Hansjoerg, DI', 'Faschingbauer'))
        assert False
    except SVNRNotExist:
        pass

def test_update_exact_duplicate():
    db = PersonDB()

    db.insert(Person('1037190666', 'Joerg', 'Faschingbauer'))

    try:
        db.update(Person('1037190666', 'Joerg', 'Faschingbauer'))
        assert False
    except ExactDuplicateError:
        pass
