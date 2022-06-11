n = int(input())

my_dict = {}

for i in range(n):
    car_info = input().split("|")
    car = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])
    my_dict[car] = {"ml": mileage, "fl": fuel}
data = input()

while not data == "Stop":
    cmd_info = data.split(" : ")
    command = cmd_info[0]
    if command == "Drive":
        car = cmd_info[1]
        distance = int(cmd_info[2])
        fuel = int(cmd_info[3])
        if my_dict[car]["fl"] - fuel <= 0:
            print(f"Not enough fuel to make that ride")
        else:
            my_dict[car]["fl"] -= fuel
            my_dict[car]["ml"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if my_dict[car]["ml"] >= 100000:
                print(f"Time to sell the {car}!")
                my_dict.pop(car)
    elif command == "Refuel":
        car = cmd_info[1]
        fuel = int(cmd_info[2])
        if my_dict[car]["fl"] + fuel <= 75:
            my_dict[car]["fl"] += fuel
            print(f"{car} refueled with {fuel} liters")
        else:
            print(f"{car} refueled with {75 - my_dict[car]['fl']} liters")
            my_dict[car]["fl"] = 75
    elif command == "Revert":
        car = cmd_info[1]
        kilometers = int(cmd_info[2])
        if my_dict[car]["ml"] - kilometers >= 10000:
            my_dict[car]["ml"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            my_dict[car]["ml"] = 10000
    data = input()

for key, value in sorted(my_dict.items(), key=lambda x: (-x[1]["ml"], x[0])):
    print(f"{key} -> Mileage: {value['ml']} kms, Fuel in the tank: {value['fl']} lt.")