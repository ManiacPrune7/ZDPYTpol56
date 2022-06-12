"""
    definicja my_range iterujacego od 0 do n
"""


class MyRange:

    def __init__(self, up_to):
        self.up_to = up_to
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.up_to:
            num_temp = self.n
            self.n += 1
            return num_temp, num_temp+1
        else:
            print("Koniec petli!")
            raise StopIteration


my_range = MyRange(4)

for num in my_range:  # num = my_range.__next__()
    print(num)
    # print(f"num: {num} | next_num: {next_num}")

numbers = [6, 3, 9, 11, 2]

# for i, number in enumerate(numbers):
#     print(f"index: {i} | number: {number}")
