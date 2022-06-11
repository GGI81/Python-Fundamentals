import re

text = input()
regex_pattern = r"(?P<beginning>\#|\@)(?P<word>[A-Za-z]{3,}(?P=beginning)(?P=beginning)[A-Za-z]{3,})"

matches = re.finditer(regex_pattern, text)
mirror_words = []
all_words = []
for i in matches:
    match = i.group("word")
    if "##" in match:
        match = match.replace("##", " ")
    elif "@@" in match:
        match = match.replace("@@", " ")
    all_words.append(match)
    b = match.split()
    first = b[0]
    second = b[1]
    if first == second[::-1]:
        mirror_words.append(f"{first} <=> {second}")

if len(all_words) == 0:
    print("No word pairs found!")
    if len(mirror_words) == 0:
        print(f"No mirror words!")
else:
    print(f"{len(all_words)} word pairs found!")
    if len(mirror_words) > 0:
        print(f"The mirror words are:")
        print(", ".join(mirror_words))
    else:
        print(f"No mirror words!")
