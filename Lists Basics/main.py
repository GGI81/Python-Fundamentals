a = [1, 2, 3, 4]
a.remove(4)
print(a)
# removing something

b = [1, 2, 3, 4]
index = int(input())
if index in range(len(b)):
    a.pop(index)
print(b)