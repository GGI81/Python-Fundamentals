username = input()
command = input()

while not command == "Registration":
    info = command.split()
    if info[0] == "Letters":
        if info[1] == "Lower":
            username = username.lower()
            print(username)
        elif info[1] == "Upper":
            username = username.upper()
            print(username)
    elif info[0] == "Reverse":
        start_index = int(info[1])
        end_index = int(info[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            part = username[start_index:end_index + 1]
            reversed_part = part[::-1]
            print(reversed_part)
    elif info[0] == "Substring":
        substring = info[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif info[0] == "Replace":
        char = info[1]
        if char in username:
            username = username.replace(char, "-")
            print(username)
    elif info[0] == "IsValid":
        char = info[1]
        if char in username:
            print(f"Valid username.")
        else:
            print(f"{char} must be contained in your username.")

    command = input()