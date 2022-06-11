string = input()

my_dict = {}

while not string == "stop":
    quantity = int(input())
    if string not in my_dict:
        my_dict[string] = quantity
    else:
        my_dict[string] += quantity
    string = input()

for key, value in my_dict.items():
    print(f"{key} -> {value}")