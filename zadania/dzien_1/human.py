"""
    definicja klasy reprezentujacej czlowieka
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


if __name__ == '__main__':
    # print(Human.number_of_ppl)
    joe = Human("Joe", "Smith", 40, 100)
    # print(Human.number_of_ppl)
    susan = Human("Susan", "Smith", 40, 120)
    print(Human.number_of_ppl)
    # print(susan.number_of_ppl, joe.number_of_ppl)

    peter = Human("Peter", "Smith", 40, 120)
    joe.tell_hello()
    susan.tell_hello()
    Human.tell_hello()
    # print(joe.name, joe.surname, joe.age, joe.energy)
    # print(joe.age is susan.age)
    # print(susan.name, susan.surname, susan.age, susan.energy)
    # print(susan.introduce())
    # joe.eat()
    # joe.sleep(2)
    # print(joe.energy)
    # print(susan.energy)
