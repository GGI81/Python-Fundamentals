string_input = input()
command = input().split(":")

while not command[0] == "Travel":
    if command[0] == "Add Stop":
        index = int(command[1])
        if 0 <= index < len(string_input):
            string = command[2]
            string_input = string_input[: index] + string + string_input[index:]
            print(string_input)
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(string_input) and 0 <= end_index < len(string_input):
            first_remaining = string_input[:start_index]
            second_remaining = string_input[end_index + 1]
            string_input = first_remaining + second_remaining
        print(string_input)
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in string_input:
            string_input = string_input.replace(old_string, new_string)
            print(string_input)
    command = input().split(":")

print(f"Ready for world tour! Planned stops: {string_input}")