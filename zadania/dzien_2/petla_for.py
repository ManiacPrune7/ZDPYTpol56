"""
    zaprezentowanie dzialanie petli for dla roznych obiektow
"""

x = [1, 2, 3, 4]
y = {'a': 1, 'b': 2, 'c': 3}


class Numbers:
    def __init__(self, nums: list):
        self.n = nums
        self.iteration_no = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration_no != len(self.n):
            elem = self.n[self.iteration_no]
            self.iteration_no += 1
            return elem
        else:
            raise StopIteration


z = Numbers([5, 6, 7, 8])

for num in z:  # z.__next__()
    print(num)
print("KONIEC!")

# raise StopIteration
# for number in x:
#     print(number)
#
# for key in y:
#     print(key)

