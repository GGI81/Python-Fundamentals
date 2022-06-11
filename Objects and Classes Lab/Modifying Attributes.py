class Person:
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age


me = Person("Peter", "Johnson", 25)
me.age += 1
print(me.age)  # 26
