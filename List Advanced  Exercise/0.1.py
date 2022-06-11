string1 = input().split(", ")
string2 = input().split(", ")

result = []

for i in string1:
    for j in string2:
        if i in j:
            if i not in result:
                result.append(i)
print(result)
