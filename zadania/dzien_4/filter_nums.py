"""
    usuwanie liczb z listy - for, list comprehension, filter
"""

numbers = list(range(1, 11))


def for_filter(nums):
    new_nums = []
    for num in nums:
        if num % 2 == 0:
            new_nums.append(num)
    return new_nums


def comprehension_filter(nums):
    return [num for num in nums if num % 2 == 0]


def filter_filter(nums):
    return list(filter(lambda num: num % 2 == 0, nums))


print(for_filter(numbers))
print(comprehension_filter(numbers))
print(filter_filter(numbers))
