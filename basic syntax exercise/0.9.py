budget = float(input())
one_kg_flour_price = float(input())
cozonacs_counter = 0
colored_eggs = 0
eggs_price = one_kg_flour_price * 0.75
milk_price_per_cozonacs = one_kg_flour_price * 1.25 / 4  # edin litur cena, a za edin kozunak e nujno 0.250 l za towa e wurhu 4
one_cozonac_price = one_kg_flour_price + eggs_price + milk_price_per_cozonacs

while budget - one_cozonac_price >= 0:
    budget -= one_cozonac_price
    cozonacs_counter += 1
    colored_eggs += 3
    if cozonacs_counter % 3 == 0:
        colored_eggs -= cozonacs_counter - 2
print(f"You made {cozonacs_counter} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")