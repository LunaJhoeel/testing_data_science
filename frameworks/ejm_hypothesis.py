from hypothesis import given
import hypothesis.strategies as st
from calculadora import suma, division
import pytest

@given(a=st.floats(), b=st.floats())
def test_suma_hypothesis(a, b):
    assert suma(a, b) == a + b

@given(a=st.floats(), b=st.floats().filter(lambda x: x != 0))
def test_division_hypothesis(a, b):
    assert division(a, b) == a / b
    
def test_division_error():
    with pytest.raises(ValueError):
        division(10, 0)
