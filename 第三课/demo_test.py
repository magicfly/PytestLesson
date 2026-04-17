def add(x, y):
    """@brief add two numbers
    @param x int
    @param y int
    @return int"""
    return x + y

def test_addition():
    """@brief test case for addition function"""
    result = add(2, 3)
    assert result == 5, "Addition failed"

def test_subtraction():
    """@brief test case for subtraction function"""
    result = add(5, 3)
    assert result == 2, "Subtraction failed"

def another_function():
    """@brief test case for another function"""
    assert False