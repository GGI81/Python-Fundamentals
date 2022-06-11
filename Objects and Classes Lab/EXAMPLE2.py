# We can set it to zero
# Example -> age=0

class Person:
    def __init__(self, name, age=0):  # Here!!!
        self.name = name
        self.age = age


georgi = Person("Georgi")   # Here age is missing
ivo = Person("Ivo", 36)     # Here age is declared

print(georgi.age, ivo.age)
# Result = 0 36
