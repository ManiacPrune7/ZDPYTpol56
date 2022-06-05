"""
    Nalezy zdefiniowac klase String
    __add__, __sub__, __mul__, __eq__

    class String:
        ...

    str1 = String("Abc")
    str2 = String("Xyz")
    str1 == str2  # True
    str1 + str2  # 6
"""

#
# class String:
#
#     def __init__(self, string):
#         self.string = string
#
#     def __add__(self, string2):
#         return len(self.string) + len(string2.string)
#
#     def __sub__(self, obj):
#         return len(self.string) - len(obj.string)
#
#     def __mul__(self, obj):
#         return len(self.string) * len(obj.string)
#
#     def __eq__(self, obj):
#         return len(self.string) == len(obj.string)
#     #
#     # def __len__(self):
#     #     return len(self.string)
#
#
# str1 = String("Abcdef")
# str2 = String("XYZ")
# print(str1 + str2)  # 9
# print(str1 - str2)  # 3
# print(str1 * str2)  # 18
# print(str1 == str2)  # False
# # print(len(str2))


class String:

    def __init__(self, string):
        self.string = string

    def __eq__(self, string2):
        print()
        return len(self.string) == len(string2.string)

s1 = "Abc"
s2 = "Xyz"

print(s1 == s2)