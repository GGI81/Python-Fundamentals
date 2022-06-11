"""
initial_loot = input().split("|")
command = input()

while not command == "Yohoho!":
    cmd_data = command.split()
    if cmd_data[0] == "Loot":
        for index in range(len(cmd_data)):
            if cmd_data[index] not in initial_loot:
                initial_loot.insert(0, cmd_data[index])
    elif cmd_data[0] == "Drop":
        index = int(cmd_data[1])
        if 0 <= index < len(initial_loot):
            initial_loot.remove(cmd_data[index])
            initial_loot.append(cmd_data[index])
    elif cmd_data[0] == "Steal":
        count = cmd_data[1]
        stolen_items = []



    command = input()
print(initial_loot)
not completed code!!!
"""

loot = input().split("|")
command = input().split()

while not command[0] == "Yohoho!":
    if command[0] == "Loot":
        for el in range(1, len(command)):
            if command[el] not in loot:
                loot.insert(0, command[el])
    elif command[0] == "Drop":
        if 0 <= int(command[1]) < len(loot):
            loot.append(loot[int(command[1])])
            loot.pop(int(command[1]))
    elif command[0] == "Steal":
        if int(command[1]) >= len(loot):
            print(", ".join(loot))
            loot = []
        else:
            print(", ".join(loot[len(loot) - int(command[1]):]))
            loot = loot[:len(loot) - int(command[1])]
    command = input().split()

if len(loot) == 0:
    print("Failed treasure hunt.")
else:
    average_gain = sum([len(el) for el in loot]) / len(loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")