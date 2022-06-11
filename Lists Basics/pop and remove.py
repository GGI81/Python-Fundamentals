a = [1, 2, 3, 4]

el = a.pop(0)
print(el)
# returns the popped index

b = [1, 2, 3, 4]
element = b.remove(2)
print(element)
# Returns nothing
print()



c = [1, 2, 3, 4]

index = int(input())

if index in range(len(c)):
    c.pop(index)
print(c)
