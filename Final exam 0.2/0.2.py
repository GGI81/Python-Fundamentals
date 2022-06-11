import re

regex = r"(?P<beginning>(\=|\/))(?P<word>[A-Z][a-z]{2,})(?P=beginning)"

data = re.findall(regex, input())

destinations = []
travel_points = 0
for match in data:
    destinations.append(match[1])
    travel_points += len(match[1])

print(f'Destinations: {", ".join([x for x in destinations])}')
print(f'Travel Points: {travel_points}')
