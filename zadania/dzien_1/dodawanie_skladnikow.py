"""
    przyklady przeciazania operatorow
"""


class Skladnik:

    def __init__(self, skl):
        self.skladnik = skl

    def __add__(self, obj):
        return self.skladnik - obj.skladnik

    def __mul__(self, obj):
        return self.skladnik * obj.skladnik

    def __sub__(self, obj):
        return self.skladnik - obj.skladnik


skl1 = Skladnik(10)
skl2 = Skladnik(20)

print(skl1 + skl2)
print(skl1.__add__(skl2))

print(skl2 * skl1)
print(skl1.__mul__(skl2))

print(skl1 - skl2)
print(skl1.__sub__(skl2))

print(skl2 - skl1)
print(skl2.__sub__(skl1))
