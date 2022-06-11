products_input = input().split("|")
command = input().split("%")

while not command[0] == "Shop!":
    if command[0] == "Important":
        product = command[1]
        if product in products_input:
            products_input.remove(product)
            products_input.insert(0, product)
    elif command[0] == "Add":
        product = command[1]
        if product not in products_input:
            products_input.append(product)
        else:
            print("The product is already in the list.")
    elif command[0] == "Swap":
        product1 = command[1]
        product2 = command[2]
        if product1 in products_input and product2 in products_input:
            a, b = products_input.index(product1), products_input.index(product2)
            products_input[a], products_input[b] = products_input[b], products_input[a]
        if product1 not in products_input:
            print(f"Product {product1} missing!")
        if product2 not in products_input:
            print(f"Product {product2} missing!")
    elif command[0] == "Remove":
        product = command[1]
        if product in products_input:
            products_input.remove(product)
        else:
            print(f"Product {product} isn't in the list.")
    elif command[0] == "Reversed":
        products_input = products_input[::-1]
    command = input().split("%")


if command[0] == "Shop!":
    counter = 0
    for i in products_input:
        counter += 1
        print(f"{counter}. {i}")
