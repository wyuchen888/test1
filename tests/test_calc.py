from src.calc import add, sub

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(5, 3) == 2

def test_sub_type_error():
    try:
        sub("a", 1)
        assert False
    except TypeError:
        assert True
