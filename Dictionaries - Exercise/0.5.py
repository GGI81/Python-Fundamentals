products = {}

command = input()
while command != "buy":
    product, price, quantity = command.split()
    price, quantity = float(price), int(quantity)

    if product not in products:
        products[product] = {'price': price, 'quantity': quantity}
        command = input()
        continue

    products[product]['price'] = price
    products[product]['quantity'] += quantity
    command = input()

products = {p: i['price'] * i['quantity'] for p, i in products.items()}  # price * quantity in products.items()

for p, i in products.items():
    print(f"{p} -> {i:.2f}")