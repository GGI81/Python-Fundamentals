n = int(input())

my_dict = {}

for i in range(n):
    heroes = input().split()
    hero_name = heroes[0]
    if int(heroes[1]) <= 100 and int(heroes[2]) <= 200:
        hero_HP = int(heroes[1])
        hero_MP = int(heroes[2])
        my_dict[hero_name] = {"hp": hero_HP, "mp": hero_MP}

command = input().split(" - ")

while not command[0] == "End":
    if command[0] == "CastSpell":
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if mp_needed <= my_dict[hero_name]["mp"]:
            mp_left = my_dict[hero_name]["mp"] - mp_needed
            my_dict[hero_name]["mp"] = mp_left
            print(f"{hero_name} has successfully cast {spell_name} and now has {mp_left} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        if my_dict[hero_name]["hp"] - damage > 0:
            hp_left = my_dict[hero_name]["hp"] - damage
            my_dict[hero_name]["hp"] = hp_left
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hp_left} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            my_dict.pop(hero_name)
    elif command[0] == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        if my_dict[hero_name]["mp"] + amount <= 200:
            my_dict[hero_name]["mp"] += amount
            print(f"{hero_name} recharged for {amount} MP!")
        else:
            recharged_health = 200 - my_dict[hero_name]["mp"]
            print(f"{hero_name} recharged for {recharged_health} MP!")
            my_dict[hero_name]["mp"] = 200
    elif command[0] == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        if my_dict[hero_name]["hp"] + amount <= 100:
            my_dict[hero_name]["hp"] += amount
            print(f"{hero_name} healed for {amount} HP!")
        else:
            recharged_health = 100 - my_dict[hero_name]["hp"]
            print(f"{hero_name} healed for {recharged_health} HP!")
            my_dict[hero_name]["hp"] = 100
    command = input().split(" - ")

for key, value in sorted(my_dict.items(), key=lambda x: (-x[1]["hp"], x[0])):
    print(key)
    print(f"  HP: {value['hp']}")
    print(f"  MP: {value['mp']}")