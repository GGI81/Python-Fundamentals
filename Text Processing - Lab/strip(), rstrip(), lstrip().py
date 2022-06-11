# Remove with spaces in start/end or both

a = "  Hello    "
print(a)
print(a.strip())   # removes spaces
print(a.rsplit())  # removes the spaces from the right side
print(a.lstrip())  # removes the spaces from the left side

print()
print()
print()

b = "...Hello...."
print(b)
print(b.strip("."))
