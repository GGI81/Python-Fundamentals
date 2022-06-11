n = int(input())

even = []
odd = []
negative = []
positive = []

for i in range(n):
    follow_numbers = int(input())
    if follow_numbers % 2 == 0:
        even.append(follow_numbers)
    if follow_numbers >= 0:
        positive.append(follow_numbers)
    if follow_numbers < 0:
        negative.append(follow_numbers)
    if follow_numbers % 2 == 1:
        odd.append(follow_numbers)
command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
elif command == "positive":
    print(positive)