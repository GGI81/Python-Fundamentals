key = int(input())
n = int(input())

for i in range(1, n + 1):
    charachter = ord(input())
    new_char = charachter + key
    new_letter = chr(new_char)
    print(f'{new_letter}', end="")

