"""
    przyklad dzialania modulu pickle - zapisywanie i odczyta plikow binarnych
"""

import pickle


class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def hello(self):
        return f"Hej, jestem {self.name}"


joe = Human("Joe", "Smith")


with open(r'C:\Users\lukie\OneDrive\Dokumenty\SDA\zajecia_repos\ZDPYTpol56\materialy\example.pickle', 'wb') as bin_file:
    pickle.dump(joe, bin_file)

with open(r'C:\Users\lukie\OneDrive\Dokumenty\SDA\zajecia_repos\ZDPYTpol56\materialy\example.pickle', 'rb') as bin_file:
    obj = pickle.load(bin_file)
    print(obj)
    print(obj.hello())
    print(id(joe))
    print(id(obj))
