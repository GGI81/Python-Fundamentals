def calculate(product, quantity):
    if product == "coffee":
        return 1.50 * quantity
    elif product == "water":
        return 1.00 * quantity
    elif product == "coke":
        return 1.40 * quantity
    elif product == "snacks":
        return 2.00 * quantity

product_input = input()
quantity_input = int(input())

print(f"{calculate(product_input, quantity_input):.2f}")