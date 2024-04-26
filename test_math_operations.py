import math_operations

def test_addition():
    assert math_operations.add(2, 3) == 5

def test_subtraction():
    assert math_operations.subtract(5, 2) == 3

def test_multiplication():
    assert math_operations.multiply(4, 3) == 12

def test_division():
    assert math_operations.divide(10, 2) == 5
