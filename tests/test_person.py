import pytest

@pytest.mark.xfail
def test_valid_svnr():
    try:
        Person('abc', 'Joerg', 'Faschingbauer')
        assert False
    except InvalidSVNR:
        pass
