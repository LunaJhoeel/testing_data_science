import pytest
from calculadora import suma, division

def test_suma():
    assert suma(2, 3) == 5

def test_division_con_error():
    with pytest.raises(ValueError):
        division(10, 0)
