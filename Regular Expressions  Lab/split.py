import re
str = "The rain in Spain"
x = re.split("\s", str)
y = str.split()
print(x)
# ['The', 'rain', 'in', 'Spain']
