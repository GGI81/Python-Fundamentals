"""
gifts_input = input().split()
command = input()

out = False

while not command == "No Money":
    command_data = command.split()
    if command_data[0] == "OutOfStock":
        gift = command_data[1]
        for i in gifts_input:
            out = False
            if gift in gifts_input:
                gifts_input.remove(gift)
                out = True
    elif command_data[0] == "Required":
        gift = command_data[1]
        index = int(command_data[2])
        if 0 <= index < len(gifts_input):
            gifts_input.insert(index, gift)
            if out == False:
                gifts_input.remove(gifts_input[index - 1])
    elif command_data[0] == "JustInCase":
        gift = command_data[1]
        gifts_input.insert(gifts_input.index(gifts_input[-1]), gift)
        if out == False:
            gifts_input.remove(gifts_input[-1])

    command = input()
print(" ".join(gifts_input))
"""

gifts = input().split()
my_command = input()
while my_command != "No Money":
    command = my_command.split()
    for i in range(len(gifts)):
        if "OutOfStock" in command:
            if command[1] in gifts:
                if gifts[i] == command[1]:
                    gifts[i] = "None"
        if "Required" in command:
            command_int = int(command[2])
            if 0 <= command_int <= len(gifts):
                gifts[command_int] = command[1]
        if "JustInCase" in command:
            gifts.pop()
            gifts.insert(len(gifts), command[1])
    my_command = input()


for item in gifts:
    if item != "None":
        print(f"{item}", end=" ")