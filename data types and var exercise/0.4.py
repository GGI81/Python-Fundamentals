n = int(input())
follow_letters = 0

for char in range(n):
    follow_letters += ord(input())
print(f"The sum equals: {follow_letters}")