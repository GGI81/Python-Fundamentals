pirate_ship = [int(i) for i in input().split(">")]
warship = [int(i) for i in input().split(">")]
max_health_capacity = int(input())
command = input().split()

stalemate = True

while not command[0] == "Retire":
    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break
    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ship):
            if pirate_ship[index] + health <= max_health_capacity:
                pirate_ship[index] += health
            else:
                pirate_ship[index] = max_health_capacity
    elif command[0] == "Status":
        sections_that_need_repair = [el for el in pirate_ship if el < max_health_capacity / 5]
        print(f"{len(sections_that_need_repair)} sections need repair.")

    command = input().split()

if stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")