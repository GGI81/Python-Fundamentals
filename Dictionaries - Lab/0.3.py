string = input().split(": ")

my_dict = {}

while not string[0] == "statistics":
    product = string[0]
    quantity = int(string[1])
    if product not in my_dict:
        my_dict[product] = quantity
    else:
        my_dict[product] += quantity

    string = input().split(": ")

print(f"Products in stock:")

for key, value in my_dict.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")