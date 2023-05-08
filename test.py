def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def mod(a, b):
    return a % b
def pow(a, b):
    return a ** b

def test_add():
    assert add(1, 2) == 3
    assert add(2, 1) == 3
    assert add(2, 2) == 4