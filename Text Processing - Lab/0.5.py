string = input()

letters = ""
numbers = ""
others = ""

for i in string:
    if i.isalpha():
        letters += i
    elif i.isdigit():
        numbers += i
    else:
        others += i

print(numbers)
print(letters)
print(others)