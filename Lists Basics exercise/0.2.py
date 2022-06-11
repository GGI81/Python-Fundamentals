factor = int(input())
count = int(input())

list_with_numbers = []

for i in range(factor * count + 1):
    if i % factor == 0:
        list_with_numbers.append(i)
        if list_with_numbers[0] == 0:
            list_with_numbers.pop()
print(list_with_numbers)