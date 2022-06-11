class Person:  # Class (Name of the class always starts with capital letter)
    def __init__(self, name, age):  # Object
        self.name = name   # self is equal to the variable // Example
        self.age = age     # test_person.name = name
                           # self = Var(class)


test_person = Person("Georgi Ivanov", 5)
ines = Person("Ines", 27)

print(test_person.name, test_person.age)
print(ines.name, ines.age)

