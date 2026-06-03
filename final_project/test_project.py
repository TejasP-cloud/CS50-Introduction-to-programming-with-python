import pytest
from project import calculate


def test_addition():
    assert calculate(10, 5, "+") == 15

def test_subtraction():
    assert calculate(10, 5, "-") == 5

def test_multiplication():
    assert calculate(10, 5, "*") == 50

def test_division():
    assert calculate(10, 5, "/") == 2

def test_division_by_zero():
    assert calculate(10, 0, "/") is None

def test_float_addition():
    assert calculate(1.5, 2.5, "+") == 4.0

def test_float_division():
    assert calculate(7, 2, "/") == 3.5

def test_negative_numbers():
    assert calculate(-5, -3, "+") == -8

def test_negative_result():
    assert calculate(3, 10, "-") == -7