import re

regex_pattern = r"(?P<emoji>(?P<beginning>(\:\:|\*\*))(?P<word>[A-Z][a-z]{2,})(?P=beginning))"
text = input()

threshold = 1

for i in text:
    if i.isdigit():
        threshold *= int(i)

matches = re.finditer(regex_pattern, text)
all_emojis = []
cool_emojis = []
for i in matches:
    all_emojis.append(i.group("emoji"))
    all_ord = 0
    for j in i.group("word"):
        all_ord += ord(j)
    if all_ord >= threshold:
        cool_emojis.append(i.group("emoji"))

print(f"Cool threshold: {threshold}")
print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
for i in cool_emojis:
    print(i)