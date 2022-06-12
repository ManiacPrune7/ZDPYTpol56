"""
    generator liczb parzystych
"""


# def liczby():
#     for i in range(4):  # 0 1 2 3
#         return i * 2


# def liczby():
#     for i in range(4):  # 0 1 2 3
#         yield i * 2
#
#
# for i in liczby():
#     print(i)


class Liczby:

    def __init__(self, how_many):
        self.how_many = how_many
        self.n = 0

    def __iter__(self):
        return self

    # def __next__(self):
    #     if self.n < self.how_many:
    #         num = self.n
    #         self.n += 1
    #         return num * 2
    #     else:
    #         raise StopIteration

    # !!!!!!!!!!!!!!!
    def __next__(self):
        for i in range(4):  # 0 1 2 3
            return i * 2


x = Liczby(4)
for i in x:
    print(i)
