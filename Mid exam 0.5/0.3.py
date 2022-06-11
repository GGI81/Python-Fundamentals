string = input().split(", ")
command = input()

while not command == "Craft!":
    command_info = command.split(" - ")
    command_type = command_info[0]
    item = command_info[1]
    if command_type == "Collect":
        if item not in string:
            string.append(item)
    elif command_type == "Drop":
        if item in string:
            string.remove(item)
    elif command_type == "Combine Items":
        item_info = item.split(":")
        old_item = item_info[0]
        new_item = item_info[1]
        if old_item in string:
            string.insert(string.index(old_item) + 1, new_item)
    elif command_type == "Renew":
        if item in string:
            string.remove(item)
            string.append(item)

    command = input()

print(", ".join(string))
