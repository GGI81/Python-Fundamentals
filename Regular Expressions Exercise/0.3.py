import re

string = input().lower()
searched_word = input().lower()

pattern = fr"\b{searched_word}\b"

matches = re.findall(pattern, string)

print(len(matches))