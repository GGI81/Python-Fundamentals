import re

regex_pattern = r"\b(?P<beginning>\_)(?P<word>[A-Za-z0-9]+)\b"
text = input()

matches = re.finditer(regex_pattern, text)
my_list = []
for i in matches:
    my_list.append(i.group("word"))

print(",".join(my_list))