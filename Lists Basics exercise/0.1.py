string = input().split()

inverted_numbers = []

for i in string:
    element = int(i) * -1
    inverted_numbers.append(element)
print(inverted_numbers)