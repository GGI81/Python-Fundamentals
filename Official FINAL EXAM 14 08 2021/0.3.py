command = input()

my_dict = {}

while not command == "Results":
    info = command.split(":")
    if info[0] == "Add":
        person_name = info[1]
        health = int(info[2])
        energy = int(info[3])
        if person_name not in my_dict:
            my_dict[person_name] = {"hl": health, "en": energy}
        else:
            my_dict[person_name]["hl"] += health
    elif info[0] == "Attack":
        attacker_name = info[1]
        defender_name = info[2]
        damage = int(info[3])
        if attacker_name in my_dict and defender_name in my_dict:
            my_dict[defender_name]["hl"] -= damage
            my_dict[attacker_name]["en"] -= 1
            if my_dict[defender_name]["hl"] <= 0:
                my_dict.pop(defender_name)
                print(f"{defender_name} was disqualified!")
            if my_dict[attacker_name]["en"] <= 0:
                my_dict.pop(attacker_name)
                print(f"{attacker_name} was disqualified!")
    elif info[0] == "Delete":
        username = info[1]
        if username in my_dict:
            my_dict.pop(username)
        elif username == "All":
            my_dict.clear()

    command = input()

print(f"People count: {len(my_dict)}")

for key, value in sorted(my_dict.items(), key=lambda x: (-x[1]["hl"], x[0])):
    print(f"{key} - {value['hl']} - {value['en']}")
