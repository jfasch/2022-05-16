from person import Person


def test_marry():
    joerg = Person('Joerg', 'Faschingbauer')
    isi = Person('Isi', 'Haubenhofer')
    joerg.marry(isi)
    assert joerg.lastname == 'Faschingbauer-Haubenhofer'

    # isi.marry(joerg)
    # assert isi.lastname == 'Haubenhofer-Faschingbauer'
