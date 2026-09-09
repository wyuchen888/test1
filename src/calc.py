def add(a, b):
    return a + b

def sub(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("sub only supports numbers")
    return a - b
