a = [1, 2, 3, 4]
print(len(a))  # Prints the length: 4
print()
for element in a:
    print(element)  # Prints the elements in a: 1 2 3 4
print()
for index in range(0, len(a)):  # Prints the indexes in a: 0 1 2 3
    print(index)
print()
for i in range(0, len(a)):  # Prints the elements on its index ->ex. index 0 - element 1:  1 2 3 4
    print(a[i], end=" ")