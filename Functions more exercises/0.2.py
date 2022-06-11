import math


def function(a, b):
    result = abs(a) + abs(b)
    return math.floor(result)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

one = function(x1, y1)
two = function(x2, y2)
if one >= two:
    print(f"({math.floor(x2)}, {math.floor(y2)})")
else:
    print(f"({math.floor(x1 )}, {math.floor(y1)})")