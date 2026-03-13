from function_library import *
import pytest


@pytest.fixture
def setup():
    """@brief a fixture for set up test case"""
    print("Start to set up test case.")
    yield
    print("End to set up test case.")

def test_add(setup):
    """@brief test case for add function
    """
    assert add(1,2) == 3
    assert add("a","b") == "ab"

@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize('a, b, c', [(5, 2, 3), (10, 4, 6)])
def test_subtract(a, b, c):
    """@brief test case for subtract function
    """
    assert subtract(a,b) == c


if __name__ == '__main__':
    """@brief main function"""
    pytest.main(["-v", "-s"])