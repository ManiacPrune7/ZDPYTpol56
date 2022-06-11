"""
    iterator - potega dwojki
"""


class PowTwo:

    def __init__(self, maximum=0):
        self.maximum = maximum
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.maximum:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration


pow = PowTwo(5)
print(pow.n, pow.maximum)

for i in pow:
    print(i)

print(pow.n, pow.maximum)

for i in pow:
    print(i)
print(pow.n, pow.maximum)
