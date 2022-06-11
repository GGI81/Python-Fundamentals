string = input().split()
searched_product = input().split()

my_dict = {}

for i in range(0, len(string), 2):
    product = string[i]
    quantity = int(string[i + 1])
    my_dict[product] = quantity

for i in searched_product:
    if i not in my_dict:
        print(f"Sorry, we don't have {i}")
    else:
        print(f"We have {my_dict[i]} of {i} left")