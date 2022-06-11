import re

regex_pattern = r"(?P<beginning>\@\#{1,})(?P<word>[A-Z][A-Za-z0-9]+[A-Z])(?P=beginning)"
number = int(input())

for i in range(number):
    command = input()
    matches = re.match(regex_pattern, command)
    if matches is not None:
        word = matches.group("word")
        digits = ""
        if len(word) >= 6 and len(word) > 0:
            for j in word:
                if j.isdigit():
                    digits += j
            if digits == "":
                digits = "00"
            print(f"Product group: {digits}")
    else:
        print(f"Invalid barcode")