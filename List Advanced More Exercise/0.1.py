numbers = [int(i) for i in input().split(", ")]
minimum = int(input())

for i in range(len(numbers)):
    if numbers[i] < minimum:
        c = minimum - numbers[i]
        max_number = max(numbers)
        if max_number - c >= minimum:
            numbers[numbers.index(max_number)] -= c
            numbers[i] += c
if sum(numbers) >= len(numbers) * minimum:
    print(numbers)
else:
    print("No equal distribution possible")