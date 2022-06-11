items = input().split(", ")
command = input().split(" - ")

while command[0] != "Craft!":

    if command[0] == "Collect":
        if command[1] not in items:
            items.append(command[1])

    elif command[0] == "Drop":
        if command[1] in items:
            items.remove(command[1])
    elif command[0] == "Combine Items":
        element = command[1].split(":")
        if element[0] in items:
            items.insert(items.index(element[0]) + 1, element[1])
    elif command[0] == "Renew":
        if command[1] in items:
            items.remove(command[1])
            items.append(command[1])
    command = input().split(" - ")
print(", ".join(items))