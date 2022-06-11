initial_health = 100
initial_bitcoins = 0

dungeons_rooms = input().split("|")
best_room = 0

is_alive = True

for room in dungeons_rooms:
    room_info = room.split(" ")
    command = room_info[0]
    number = int(room_info[1])
    best_room += 1
    if command == "potion":
        health_gained = number
        if initial_health + number > 100:
            health_gained = 100 - initial_health
        initial_health += health_gained
        print(f"You healed for {health_gained} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        monster = command
        damage = number
        if initial_health - damage > 0:
            initial_health -= damage
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {best_room}")
            is_alive = False
            break
if is_alive:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
