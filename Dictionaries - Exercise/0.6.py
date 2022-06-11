n = int(input())

my_dict = {}

for index in range(1, n + 1):
    parking_info = input().split()
    if parking_info[0] == "register":
        username = parking_info[1]
        license_plate_number = parking_info[2]
        if username not in my_dict and license_plate_number not in my_dict:
            my_dict[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif parking_info[0] == "unregister":
        username = parking_info[1]
        if username not in my_dict:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            my_dict.pop(username)

for key, value in my_dict.items():
    print(f"{key} => {value}")