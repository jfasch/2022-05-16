from person import Person


def test_person_init_and_attributes():
    joerg = Person('Joerg', 'Faschingbauer')
    assert joerg.firstname == 'Joerg'
    assert joerg.lastname == 'Faschingbauer'

    erich = Person('Erich', 'Zimmermann')
    assert erich.firstname == 'Erich'
    assert erich.lastname == 'Zimmermann'

def test_invert():
    joerg = Person('Joerg', 'Faschingbauer')

    joerg.invert()
    assert joerg.firstname == 'greoJ'
    assert joerg.lastname == 'reuabgnihcsaF'

