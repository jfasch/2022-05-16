import pytest


@pytest.mark.xfail
def test_read_csv(tmpdir):
    filename = tmpdir / 'persons.csv'

    with open(filename, 'w') as f:
        f.write('\n'.join([
            '1037190666;Joerg;Faschingbauer',
            '1234250497;Caro;Faschingbauer',
            '2345110695;Johanna;Faschingbauer',
        ]))

    db = PersonDB()
    db.read_csv(filename)

    joerg = db.find('1037190666')
    assert joerg.firstname == 'Joerg'
    assert joerg.lastname == 'Faschingbauer'
    assert joerg.svnr == '1037190666'
