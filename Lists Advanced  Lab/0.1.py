string = input()
result = []
for i in string:
    result.append(i)
    if i == "a" or i == "o" or i == "u" or i == "e" or i == "i":
        result.remove(i)
print("".join(result))