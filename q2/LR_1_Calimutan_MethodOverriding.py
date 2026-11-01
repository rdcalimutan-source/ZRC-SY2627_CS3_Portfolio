class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        pass

    def make_sound(self):
        pass

class Lion(Animal):
    def eat(self):
        print(f"The {self.name} eats fresh meat.")

    def make_sound(self):
        print(f"The {self.name} roars loudly.")

class Elephant(Animal):
    def eat(self):
        print(f"The {self.name} eats grass and fruits.")

    def make_sound(self):
        print(f"The {self.name} trumpets.")

class Monkey(Animal):
    def eat(self):
        print(f"The {self.name} eats bananas.")

    def make_sound(self):
        print(f"The {self.name} chatters.")

lion = Lion("lion")
elephant = Elephant("elephant")
monkey = Monkey("monkey")

zoo_animals = [lion, elephant, monkey]

for animal in zoo_animals:
    animal.make_sound()
    animal.eat()
    print() 