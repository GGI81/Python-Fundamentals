array = input().split()
command = input().split()
amount = 0
# new_array = []

while not command == "end":
    if command[0] == "swap":
        array[int(command[1])], array[int(command[2])] = array[int(command[2])], array[int(command[1])]
    elif command[0] == "multiply":
        amount = int(array[int(command[1])]) * int(array[int(command[2])])
        array.remove(array[int(command[1])])
        array.insert(int(command[1]), str(amount))
    elif command[0] == "decrease":
        array = list(map((lambda x: x - 1), array))
        # for item in array:
        #     new_array.append(int(item) - 1)
    command = input().split()
    if command[0] == "end":
        break

print(", ".join(map(str, array)))