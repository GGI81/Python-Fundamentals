# List
my_list = [1, 2, 3]

if 2 in my_list:
    print("Number is in list!")

print(2 in my_list)  # Like this returns True or False

print()
print()
print()

# Dictionary
my_dict = {"a": 5, "b": 6}

for key, value in my_dict.items():
    pass

print(6 in my_dict.values())  # True

print()
print()
print()

my_dict = {"a": ["Ines", "Georg"], "b": ["Test1", "Test2"]}

for key, value in my_dict.items():
    pass

print("a" in my_dict.keys())  # True