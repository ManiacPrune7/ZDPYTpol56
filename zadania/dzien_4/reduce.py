"""
    wyliczenie iloczynu za pomoca petli for i funkcji reduce
"""

from functools import reduce

nums = list(range(10, 21))


def for_multiplication(numbers: list) -> int:
    result = 1
    for number in numbers:
        result *= number
    return result


def reduce_multiplication(numbers: list) -> int:
    return reduce(lambda prev_num, num: prev_num * num, numbers)


print(for_multiplication(nums))
print(reduce_multiplication(nums))
