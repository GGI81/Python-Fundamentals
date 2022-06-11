string = input().split(", ")
my_command = input()

while not my_command == "Craft!":
    command_info = my_command.split(" - ")
    command = command_info[0]
    item = command_info[1]
    if command == "Collect":
        if item not in string:
            string.append(item)
    elif command == "Drop":
        if item in string:
            string.remove(item)
    elif command == "Combine Items":
        items = item.split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in string:
            string.insert(string.index(old_item) + 1, new_item)
    elif command == "Renew":
        if item in string:
            string.remove(item)
            string.append(item)

    my_command = input()

print(", ".join(string))