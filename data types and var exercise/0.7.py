n = int(input())
capacity_of_the_tank = 255
litters_total = 0
for litters in range(1, n + 1):
    follow_litters = int(input())
    if litters_total + follow_litters > capacity_of_the_tank:
        print("Insufficient capacity!")
    else:
        litters_total += follow_litters
print(litters_total)