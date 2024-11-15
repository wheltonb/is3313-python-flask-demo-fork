import mymath

def test_mymath_add():
    assert mymath.add_three(1,2, 3) == 6

def test_mymath_sub():
    assert mymath.subtract_three(8, 2, 1) == 5

def test_mymath_multiply():
    assert mymath.multiply_three(8, 2, 1) == 16

def test_mymath_power():
    assert mymath.power(2, 3) == 8