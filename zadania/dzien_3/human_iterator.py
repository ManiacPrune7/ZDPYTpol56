"""
    wykorzystanie iteratora w obiekcie klasy Human
"""

a = 10


class Human:

    number_of_ppl = 0

    def __init__(self, name, surname, age, energy):
        # temporary_var = 10
        self.name = name
        self.surname = surname
        self.age = age
        self.energy = energy
        Human.number_of_ppl += 1
        # zmienna do iteracji
        self.n = 0

    def introduce(self):
        return f"Hello, my name is {self.name}"

    def eat(self):
        self.energy += 20

    def sleep(self, hours):
        self.energy += 5*hours

    def run(self, hours):
        self.energy -= 15*hours

    @staticmethod
    def tell_hello():
        print("Hello!")

    def __iter__(self):
        return self

    def __next__(self):
        welcome = self.introduce()  # "Hello, my name is Joe"
        words = welcome.split()

        if self.n != len(words):
            result = words[self.n]
            self.n += 1
            return result

        raise StopIteration


if __name__ == '__main__':
    # print(Human.number_of_ppl)
    joe = Human("Joe", "Smith", 40, 100)

    for word in joe:  # x = joe.__iter__(), i = joe.__next__(), i = joe.__next__()
        print(word)
