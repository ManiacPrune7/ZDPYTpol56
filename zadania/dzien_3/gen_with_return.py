"""
    jak dziala generator ze slowem kluczowym return wewnatrz
"""


def ret():
    for i in range(5):
        if i == 3:
            return
        else:
            yield i

iterator = ret()

for x in iterator:
    print(x)

print("druga petla:")

for x in iterator:
    print(x)

gen1 = ret()
gen2 = ret()

print(list(gen1))
print(list(gen1))
