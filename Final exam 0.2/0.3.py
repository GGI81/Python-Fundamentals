n = int(input())

my_dict = {}

for i in range(n):
    plants_info = input().split("<->")
    plant = plants_info[0]
    rarity = int(plants_info[1])
    my_dict[plant] = {"rty": rarity, "rtg": []}

command = input().split(": ")

while not command[0] == "Exhibition":
    if command[0] == "Rate":
        plant_rating = command[1].split(" - ")
        plant = plant_rating[0]
        rating = int(plant_rating[1])
        my_dict[plant]["rtg"].append(rating)
    elif command[0] == "Update":
        plant_new_rarity = command[1].split(" - ")
        plant = plant_new_rarity[0]
        new_rarity = int(plant_new_rarity[1])
        my_dict[plant]["rty"] = new_rarity
    elif command[0] == "Reset":
        plant = command[1]
        my_dict[plant]["rtg"].clear()
    command = input().split(": ")

print(f"Plants for the exhibition:")

for key, value in sorted(my_dict.items(), key=lambda x: (x[1]["rty"], x[1]["rtg"]), reverse=True):
    if sum(value["rtg"]) == 0 or len(value["rtg"]) == 0:
        average = 0
    else:
        average = sum(value["rtg"]) / len(value["rtg"])
    print(f"- {key}; Rarity: {value['rty']}; Rating: {average:.2f}")
