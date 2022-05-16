from person import Person


def test_marry():
    joerg = Person('Joerg', 'Faschingbauer')
    isi = Person('Isi', 'Haubenhofer')

    Person.marry(joerg, isi)

    assert joerg.lastname == 'Faschingbauer-Haubenhofer'
    assert isi.lastname == 'Haubenhofer-Faschingbauer'
