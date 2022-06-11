energy = int(input())
won_battles = 0
lost = False

while True:
    command = input()
    if command == "End of battle":
        break
    distance = int(command)
    if energy - distance >= 0:
        energy -= distance
        won_battles += 1
        if won_battles % 3 == 0:
            energy += won_battles
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        lost = True
        break

if not lost:
    print(f"Won battles: {won_battles}. Energy left: {energy}")