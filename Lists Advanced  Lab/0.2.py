number_wagons = int(input())
train = [0] * number_wagons
command = input()

while not command == "End":
    data = command.split()
    if data[0] == "add":
        train[-1] += int(data[1])
    elif data[0] == "insert":
        index = int(data[1])
        people = int(data[2])
        train[index] += people
    elif data[0] == "leave":
        index = int(data[1])
        people = int(data[2])
        train[index] -= people
    command = input()
print(train)