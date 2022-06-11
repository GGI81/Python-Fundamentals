string = input().split()

my_dict = {}

for i in range(0, len(string), 2):
    product = string[i]
    quantity = int(string[i + 1])
    my_dict[product] = quantity

print(my_dict)