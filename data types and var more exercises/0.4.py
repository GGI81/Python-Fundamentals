n = int(input())
opening_brackets_count = 0
closing_brackets_count = 0
is_balanced = True
for i in range(0, n):
    text = input()
    if text == "(":
        opening_brackets_count += 1
    elif text == ")":
        closing_brackets_count += 1
    if closing_brackets_count > opening_brackets_count:
        is_balanced = False
        break
    elif opening_brackets_count - 1 > closing_brackets_count:
        is_balanced = False
        break
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")