import re

regex_pattern = r"(?P<beginning>\#|\|)(?P<word>[A-Za-z\s]+)(?P=beginning)(?P<date>[0-9]{2,}\/[0-9]{2,}\/[0-9]{2,})(?P=beginning)(?P<calories>[0-9]+)(?P=beginning)"
text = input()

kcal_per_day = 2000

matches = re.finditer(regex_pattern, text)
total = 0
days = 0
my_list = []
for i in matches:
    total += int(i.group("calories"))
    my_list.append(f"Item: {i.group('word')}, Best before: {i.group('date')}, Nutrition: {i.group('calories')}")

while total - kcal_per_day >= 0:
    days += 1
    total -= kcal_per_day

print(f"You have food to last you for: {days} days!")
for i in my_list:
    print(i)