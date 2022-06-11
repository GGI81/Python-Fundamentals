n = [int(i) for i in input().split(", ")]

for index in n:
    number = int(index)
    if number == 0:
        n.remove(index)
        n.append(0)
print(n)