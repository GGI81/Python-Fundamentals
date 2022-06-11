"""
While instance attributes are specific to each object,
class attributes are the same for all instances
"""


class Person:
    species = "mammal"   # Here is the class Attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age


me = Person("George", 25)
you = Person("John", 44)

print(me.name, me.age, me.species)  # me.species
print(you.name, you.age, you.species)   # you.species

print()
print()
print()
print()
print()


class Person2:
    species = "mammal"  # Here is the class Attribute

    def __init__(self, name, age, kg):
        self.name = name
        self.age = age
        self.kg = kg

    def eat(self):
        print("eating")
        self.kg += 0.30


me2 = Person2("George", 25, 70)
print(me2.kg)
me2.eat()
print(me2.kg)


print()
print()
print()
print()
print()


class Person3:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


me3 = Person3("Peter", "Johnson", 64)
print(me3.get_full_name())
