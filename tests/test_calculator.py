from cicd_demo.calculator import add, multiply


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_zero():
    assert add(0, 7) == 7


def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(10, 0) == 0
