string = input()

my_dict = {}

for i in string:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

for key, value in my_dict.items():
    if key != " ":
        print(f"{key} -> {value}")
