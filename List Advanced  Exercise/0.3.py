"""
string = input().split()
result = []
for i in string:
    if len(i) % 2 == 0:
        result.append(i)

for i in result:
    print(i, end="\n")
"""

string = input().split()
result = [i for i in string if len(i) % 2 == 0]

for i in result:
    print(i)