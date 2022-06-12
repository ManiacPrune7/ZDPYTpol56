"""
    implementacja ciagu fibonacciego iteracyjnie i przez generator
"""


def fibo_i(n: int):
    # (a, b) = (0, 1)
    a = 0
    b = 1
    for _ in range(n):
        # (a, b) = (b, a+b)
        temp = a
        a = b
        b = temp+b
    return a


def fibo_g(n: int):
    a, b = 0, 1
    yield a
    for _ in range(n):
        a, b = b, a+b
        yield a


print(fibo_i(5))
print(list(fibo_g(5)))
