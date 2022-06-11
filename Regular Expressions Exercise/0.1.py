import re

pattern = r"\d+"
text = input()
my_list = []

while text:
    matches = re.findall(pattern, text)
    for i in matches:
        my_list.append(i)
    text = input()
print(" ".join(my_list))