# list
a = [1, 2, 3, 4]
print([el for el in a if el % 2 == 0])

print()
print()
print()

# dictionary comprehension
my_dict = {"Peter": 21, "George": 18, "John": 45}
print({key: value for key, value in my_dict.items() if value % 2 == 0})

print()
print()
print()

# regular solving
even_years = {}

for key, value in my_dict.items():
    if value % 2 == 0:
        even_years[key] = value
print(even_years)

