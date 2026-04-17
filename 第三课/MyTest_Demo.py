def test_default_prefix():
    """@brief test default prefix"""
    assert 1 + 1 == 2

def myTest_Demo():
    """@brief test MyTest_Demo"""
    assert 1 + 1 == 2

class TestClass:
    """@brief test class for demo"""

    def test_something(self):
        """@brief test something"""
        assert True

    def test_something_else(self):
        """@brief test something else"""
        assert False

class myTestClass:
    """@brief test class for myTest demo"""

    def myTest_something(self):
        """@brief test something"""
        assert True

    def test_something_else(self):
        """@brief test something else"""
        assert False