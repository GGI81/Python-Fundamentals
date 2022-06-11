# Keys() method to get all keys
# Items()
my_dict = {"a": ["Ines", "Georgi"], "b": ["Test1", "Test2"]}

print(my_dict.keys())
print(my_dict.items())

print()
print()
print()

for key in my_dict:
    print(key)  # returns the keys

print()
print()
print()

for value in my_dict.values():
    print(value)  # returns value

print()
print()
print()

for key, value in my_dict.items():   # it will work only with .items()
    print(key)
    print(value)

print()
print()
print()

print(my_dict.items())  # tuple

print()
print()
print()

for key in my_dict:
    print(key)  # Gives the key name
    print(my_dict[key])  # Gives the Value

print()
print()
print()

for key in my_dict:
    my_dict[key].append("from the loop")
print(my_dict)
