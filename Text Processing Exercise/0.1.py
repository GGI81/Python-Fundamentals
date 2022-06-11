string = input().split(", ")

for i in string:
    if 3 < len(i) < 16:
        if "-" in i or "_" in i or i.isalnum():
            print(i)