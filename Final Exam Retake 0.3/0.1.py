string = input()
command = input()

while command != "Reveal":
    data = command.split(":|:")
    command_name = data[0]
    if command_name == "InsertSpace":
        index = int(data[1])
        string = string[:index] + " " + string[index:]
        print(string)
    elif command_name == "Reverse":
        substring = data[1]
        reversed_string = substring[::-1]
        if substring in string:
            string = string.replace(substring, reversed_string, 1)
            print(string)
        else:
            print(f"error")
    elif command_name == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        if substring in string:
            for i in string:
                if i == substring:
                    string = string.replace(i, replacement)
            print(string)
    command = input()
print(f"You have a new text message: {string}")

"""
message = input()

while True:
    command_input = input()

    if command_input == "Reveal":
        break

    command_args = command_input.split(":|:")
    command_name = command_args[0]

    if command_name == "InsertSpace":
        index = int(command_args[1])

        message = message[:index] + " " + message[index:]
        print(message)
    elif command_name == "Reverse":
        substr = command_args[1]

        old_message = message
        message = message.replace(substr, "", 1)

        if old_message == message:
            print("error")
            continue

        # subsrt_list = list(substr)
        # subsrt_list.reverse()
        # substr_reversed = "".join(subsrt_list)
        substr_reversed = substr[::-1]

        message += substr_reversed
        print(message)
    elif command_name == "ChangeAll":
        substr = command_args[1]
        replacement = command_args[2]
        message = message.replace(substr, replacement)
        print(message)

print(f"You have a new text message: {message}")
"""