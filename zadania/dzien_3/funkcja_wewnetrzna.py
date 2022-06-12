"""
    definicja i pokaz mozliwosci funkcji wewnetrznych
"""


def outer(text):
    print("OUTER")

    def inner(txt):

        def abc():
            return "abc"

        print("INNER")
        big_str = txt.upper()
        print(text)  # *******
        print(txt)
        return big_str

    # abc()
    result = inner(text)
    return result


# print(inner("abcd"))

print(outer("Co tam slychac"))
