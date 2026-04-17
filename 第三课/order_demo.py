import pytest

pytest.mark.run(order=1)
def order_z_demo_two():
    """@brief z demo two"""
    print("z_demo_two")
    assert True

pytest.mark.run(order=2)
def order_b_demo_two():
    """@brief b demo two"""
    print("b_demo_two")
    assert True

pytest.mark.run(order=3)
def order_a_demo_two():
    """@brief a demo two"""
    print("a_demo_two")
    assert True

def order_a_demo():
    """@brief a demo"""
    print("a_demo")
    assert True

def order_b_demo():
    """@brief b demo"""
    print("b_demo")
    assert True

def order_z_demo():
    """@brief z demo"""
    print("z_demo")
    assert True
