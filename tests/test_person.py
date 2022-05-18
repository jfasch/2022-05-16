from person import Person, InvalidSVNR
import pytest


def test_valid_svnr():
    Person('1037190666', 'Joerg', 'Faschingbauer')

def test_valid_svnr_unusual():
    Person('12AB190666', 'Joerg', 'Faschingbauer')
    Person('ABAB190666', 'Joerg', 'Faschingbauer')

def test_invalid_svnr_1():
    try:
        Person('abc', 'Joerg', 'Faschingbauer')
        assert False
    except InvalidSVNR:
        pass

def test_invalid_svnr_2():
    try:
        Person([0,1,2,3,4,5,6,7,8,9], 'Joerg', 'Faschingbauer')
        assert False
    except InvalidSVNR:
        pass

def test_invalid_svnr_3():
    try:
        Person('abcdefghij', 'Joerg', 'Faschingbauer')
        assert False
    except InvalidSVNR:
        pass

def test_invalid_svnr_4():
    try:
        Person('-123456789', 'Joerg', 'Faschingbauer')
        assert False
    except InvalidSVNR:
        pass

