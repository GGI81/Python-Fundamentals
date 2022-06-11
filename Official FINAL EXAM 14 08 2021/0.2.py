import re

regex_pattern = r"^(?P<beginning>.+)\>(?P<number>\d+)\|(?P<lowword>[a-z]+)\|(?P<upword>[A-Z]+)\|(?P<symbols>.[^<>]+)\<(?P=beginning)"
n = int(input())

for i in range(n):
    command = input()
    match = re.match(regex_pattern, command)
    if match is not None:
        print(f"Password: {match.group('number')}{match.group('lowword')}{match.group('upword')}{match.group('symbols')}")
    else:
        print("Try another password!")
