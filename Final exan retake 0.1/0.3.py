n = int(input())

my_dict = {}

for i in range(n):
    info = input().split("|")
    piece = info[0]
    composer = info[1]
    piece_key = info[2]
    my_dict[piece] = {"cmp": composer, "pck": piece_key}

command = input()

while not command == "Stop":
    cmd_info = command.split("|")
    if cmd_info[0] == "Add":
        piece = cmd_info[1]
        composer = cmd_info[2]
        piece_key = cmd_info[3]
        if piece in my_dict:
            print(f"{piece} is already in the collection!")
        else:
            my_dict[piece] = {"cmp": composer, "pck": piece_key}
            print(f"{piece} by {composer} in {piece_key} added to the collection!")
    elif cmd_info[0] == "Remove":
        piece = cmd_info[1]
        if piece in my_dict:
            print(f"Successfully removed {piece}!")
            my_dict.pop(piece)
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif cmd_info[0] == "ChangeKey":
        piece = cmd_info[1]
        new_key = cmd_info[2]
        if piece in my_dict:
            print(f"Changed the key of {piece} to {new_key}!")
            my_dict[piece]['pck'] = new_key
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for key, value in sorted(my_dict.items(), key=lambda x: (x[0], x[1]["cmp"])):
    print(f"{key} -> Composer: {value['cmp']}, Key: {value['pck']}")