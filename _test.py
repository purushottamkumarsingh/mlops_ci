import pytest

def square(n):
    return n * n

def cube(n):
    return n * n * n

def fifth_power(n):
    return n ** 5


# ------------------ Tests ------------------

def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0

def test_cube():
    assert cube(2) == 8
    assert cube(-3) == -27
    assert cube(0) == 0

def test_fifth_power():
    assert fifth_power(2) == 32
    assert fifth_power(-2) == -32
    assert fifth_power(0) == 0
