import re


patter = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()

valid_nums = re.finditer(patter, text)
valid_nums = [num.group() for num in valid_nums]
print(*valid_nums)