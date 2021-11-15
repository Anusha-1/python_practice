import pytest

def capital_case(str):
    return str.capitalize()

def test_capital_case():
    assert capital_case('welcome')=='Welcome'

    #pytest --verbose test_capital.py
    #nose2 --with-coverage
