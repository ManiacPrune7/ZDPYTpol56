"""
    pokaz dzialania slowka yield w generatorze
"""


def wznowienia():
    print("wstrzymuje dzialanie")
    yield 1
    print("wznawiam dzialanie")

    print("wstrzymuje dzialanie")
    yield 2
    print("wznawiam dzialanie")
    # yield 3
    # return None -> StopIteration


gen = wznowienia()

print(next(gen))
print(next(gen))
try:
    print(next(gen))
except StopIteration:
    print("Oho, generator skonczyl dzialanie...")


for i in wznowienia():
    print(f"Zwrocono wartosc: {i}")
