biscuits_input = input().split(", ")
my_command = input()

out = False

while not my_command == "No More Money":
    command_data = my_command.split()
    if command_data[0] == "OutOfStock":
        biscuit = command_data[1]
        for i in biscuits_input:
            out = False
            if biscuit in biscuits_input:
                biscuits_input.remove(biscuit)
                out = True
                position = int(biscuit.index(biscuits_input))
                list_nums.pop(position)
                list_nums.insert(position, "None")

    elif command_data[0] == "Required":
        biscuit = command_data[1]
        index = int(command_data[2])
        if 0 <= index < len(biscuits_input):
            biscuits_input.insert(index, biscuit)
            if out == True:
                biscuits_input.remove(biscuits_input[index - 1])
    elif command_data[0] == "Last":
        biscuit = command_data[1]
        biscuits_input.append(biscuit)

    my_command = input()

print(" ".join(biscuits_input))