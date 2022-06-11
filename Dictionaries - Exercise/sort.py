# sort()
a = [100, 50, 70]

print(sorted(a, reverse=True))


# sorted(iterable, key=None, reverse=False)

# SORTING !!!
my_dict = {"Peter": 21, "George": 18, "John": 45}
print(my_dict.items())
sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
print(sorted_dict)
# SORTING !!!

print()
print()
print()
print()

# REVERSED !!!!!
my_dict = {"Peter": 21, "George": 18, "John": 45}
print(my_dict.items())
sorted_dict = sorted(my_dict.items(), key=lambda x: x[0], reverse=True)
print(sorted_dict)
# Reverse=True

print()

for key, value in sorted_dict:
    print(f"key is {key} and value is {value}")

print()
print()
print()

my_dict = {"Peter": 21, "George": 18, "John": 45}
print(my_dict)

sorted_dict = sorted(my_dict.items(), key=lambda x: x[0])

for key, value in sorted_dict:
    print(f"key is {key} and value is {value}")

print()
print()
print()

# lambda with more than one argument
my_dict = {"Peter": 21, "George": 18, "John": 45}
print(my_dict)

sorted_dict = sorted(my_dict.items(), key=lambda x: (x[0], x[1]))

for key, value in sorted_dict:
    print(f"key is {key} and value is {value}")

