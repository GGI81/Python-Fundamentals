dwarfs = {}
hats = {}
command = input()

while not command == "Once upon a time":
    name, color, physic = command.split(" <:> ")
    physic = int(physic)
    name = name + ":" + color
    if name not in dwarfs:
        if color not in hats:
            hats[color] = 1
        else:
            hats[color] += 1
        dwarfs[name] = (physic, color)
    else:
        if dwarfs[name][0] <= physic:
            dwarfs[name] = (physic, color)
    command = input()

for el in sorted(dwarfs.items(), key=lambda x: (x[1][0], hats[x[1][1]]), reverse=True):
    name, color = el[0].split(":")
    physic = el[1][0]
    print(f"({color}) {name} <-> {physic}")