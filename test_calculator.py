from calculator import add, subtract, Calculator

def test_add():
    # module-level function
    assert add(2, 3) == 5

    # class method should behave the same
    assert Calculator.add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2
    assert Calculator.subtract(5, 3) == 2
