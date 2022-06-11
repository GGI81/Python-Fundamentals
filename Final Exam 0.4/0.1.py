string = input()
command = input().split()

my_list = []

while not command[0] == "Done":
    if command[0] == "TakeOdd":
        for i in range(0, len(string)):
            if i % 2 != 0:
                my_list.append(string[i])
        string = "".join(my_list)
        print(string)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        if 0 <= index < len(string):
            taken_part = string[index: length + index]
            string = string.replace(taken_part, "")
            print(string)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print(f"Nothing to replace!")
    command = input().split()

print(f"Your password is: {string}")
