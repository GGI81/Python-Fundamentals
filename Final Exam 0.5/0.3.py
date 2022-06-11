string = input()

my_dict = {}

while not string == "Sail":
    data = string.split("||")
    city = data[0]
    population = int(data[1])
    gold = int(data[2])
    if city not in my_dict:
        my_dict[city] = {"pl": population, "gl": gold}
    else:
        my_dict[city]["pl"] += population
        my_dict[city]["gl"] += gold
    string = input()

command = input()

while not command == "End":
    command_info = command.split("=>")
    if command_info[0] == "Plunder":
        city = command_info[1]
        people = int(command_info[2])
        gold = int(command_info[3])
        if my_dict[city]["gl"] - gold >= 0 or my_dict[city]["pl"] - people >= 0:
            gold_left = my_dict[city]["gl"] - gold
            people_left = my_dict[city]["pl"] - people
            my_dict[city]["gl"] = gold_left
            my_dict[city]["pl"] = people_left
            print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if my_dict[city]["gl"] - gold <= 0 or my_dict[city]["pl"] - people <= 0:
            if my_dict[city]["gl"] == 0 or my_dict[city]["pl"] == 0:
                print(f"{city} has been wiped off the map!")
                my_dict.pop(city)
    elif command_info[0] == "Prosper":
        city = command_info[1]
        gold = int(command_info[2])
        if gold <= 0:
            print("Gold added cannot be a negative number!")
        else:
            my_dict[city]["gl"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {my_dict[city]['gl']} gold.")
    command = input()

print(f"Ahoy, Captain! There are {len(my_dict)} wealthy settlements to go to:")

if len(my_dict) > 0:
    for key, value in sorted(my_dict.items(), key=lambda x: (-x[1]["gl"], x[0])):
        print(f"{key} -> Population: {value['pl']} citizens, Gold: {value['gl']} kg")
else:
    print(f"Ahoy Captain! All targets have been plundered and destroyed!")