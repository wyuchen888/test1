from src.calc import add, sub, multiply

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_multiply_type_error():
    try:
        multiply("a", 1)
        assert False
    except TypeError:
        assert True
