import pytest


def func_add(x, y):
    """@brief add two numbers"""
    return x + y

def myAssert_func():
    """@brief test_func_add"""
    assert func_add(1, 2) == 3

def myAssert_expression():
    """@brief test_exception"""
    a = 5
    assert a % 2 == 0

def myAssert_compare():
    """@brief test_compare"""
    assert 1 < 3
    assert 5 >= 3
    assert 5 != 3
    assert 1 in [1, 2, 3]
    assert 'a' in "abc"
    assert (3 == 3) is True

def myAssert_compare_one():
    """@brief test_compare"""
    assert 1 > 3

def myAssert_compare_two():
    """@brief test_compare"""
    assert (3 == 3) is False

def myAssert_type():
    """@brief test_type"""
    assert type(3) == int
    assert {'a': 1, 'b': 2} == {'a': 1, 'b': 2}
    a = [1, 2, 3]
    b = [4, 5, 6]
    assert a == b

def myfunc():
    """@brief myfunc"""
    raise ValueError("给定数据不匹配。")

def myAssert_myfunc():
    """@brief test myfunc"""
    with pytest.raises(ValueError):
        myfunc()

def myAssert_myfunc2():
    """@brief test myfunc2"""
    assert func_add(1, 2) == 3, "1加2应该是3."
    assert func_add(1, 2) == 4, "1加2应该是3."