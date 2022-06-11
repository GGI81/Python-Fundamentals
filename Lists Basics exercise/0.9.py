items_input = input().split("|")
budget = int(input())
profit = 0
all_money = 0
for item in items_input:
    item = item.split("->")
    item_name = item[0]
    item_price = float(item[1])
    buy = False
    if item_name == "Clothes":
        if 0 < item_price <= 50:
            buy = True
    elif item_name == "Shoes":
        if 0 < item_price <= 35:
            buy = True
    elif item_name == "Accessories":
        if 0 < item_price <= 20.50:
            buy = True
    if buy:
        if budget >= item_price:
            budget -= item_price
            print(f"{item_price * 1.4:.2f}", end = " ")
            profit += item_price * 0.4
            all_money += item_price * 1.4
all_money = all_money + budget
print()
print(f"Profit: {profit:.2f}")
if all_money >= 150:
    print("Hello, France!")
else:
    print("Time to go.")