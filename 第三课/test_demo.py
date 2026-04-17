class TestClass:
    """@brief test class for demo"""

    def test_something(self):
        """@brief test something"""
        assert True

    def test_something_else(self):
        """@brief test something else"""
        assert False


def test_a():
    """@brief test a"""
    assert True

def test_b():
    """@brief test b"""
    assert True

def test_z():
    """@brief test z"""
    assert True

def testLogin():
    """@brief test login"""
    username = "admin"
    password = ""
    assert username == "admin"
    assert password == ""