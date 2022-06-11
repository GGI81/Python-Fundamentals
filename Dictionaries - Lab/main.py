dict_names_age = {"Ivo": 43, "Georgi": 32, "Alex": 29}
print(dict_names_age.items())
sorted_dict = sorted(dict_names_age.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict)

print()
print()
print()

my_dict = {"Peter": 21, "George": 18, "John": 45}
print(my_dict)
# sorting with more than one argument
sorted_dict = sorted(my_dict.items(), key=lambda x: (x[1], x[0]))

for key, value in sorted_dict:
    print(f"key is {key} and value is {value}")
