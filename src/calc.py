def add(a, b):
    return a + b  # main 侧审计修改（保留）

def sub(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("sub only supports numbers")
    return a - b

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("multiply only supports numbers")
    return a * b
