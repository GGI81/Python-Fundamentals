groceries = input().split("!")
while True:
    command = input()
    if command == "Go Shopping!":
        break
    item = command.split(" ")
    if len(item) == 2:
        if item[0] == "Urgent":
            if item[1] not in groceries:
                groceries.insert(0, item[1])
        elif item[0] == "Unnecessary":
            if item[1] in groceries:
                groceries.remove(item[1])
        elif item[0] == "Rearrange":
            if item[1] in groceries:
                groceries.remove(item[1])
                groceries.append(item[1])
    else:
        if item[1] in groceries:
            index = groceries.index(item[1])
            groceries[index] = item[2]
print(", ".join(groceries))
