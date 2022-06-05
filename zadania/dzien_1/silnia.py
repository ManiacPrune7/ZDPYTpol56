"""
    obliczanie silni n! iteracyjnie
"""


def factorial(n):
    """Wylicza silnie z n.

    :param n: liczba naturalna
    :return: wyliczoną silnię
    """
    result = 1

    for i in range(1, n+1):  # 1 2 3 4 ... n
        result *= i  # 1 * 2 * 3 * 4 * 5

    return result


# print(factorial(5))
# print(factorial(0))
# print(factorial(1))
# print(factorial(4))


def silnia(n):
    for i in range(n-1, 1, -1):  # 4, 3, 2
        n *= i  # 5 * 4 * 3 * 2
    return n


print(silnia(5))