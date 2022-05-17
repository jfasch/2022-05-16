import pytest
from person import Person


#@pytest.mark.xfail
def test_person_init_and_attributes():
    joerg = Person('1037190666', 'Joerg', 'Faschingbauer')
    assert joerg.firstname == 'Joerg'
    assert joerg.lastname == 'Faschingbauer'

#@pytest.mark.xfail
def test_invert():
    joerg = Person('1037190666', 'Joerg', 'Faschingbauer')

    joerg.invert()
    assert joerg.svnr == '1037190666'  # remains untouched
    assert joerg.firstname == 'greoJ'
    assert joerg.lastname == 'reuabgnihcsaF'
