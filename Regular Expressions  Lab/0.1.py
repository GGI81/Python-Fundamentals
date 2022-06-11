import re

regex = r"\b[A-Z][a-z]+ \b[A-Z][a-z]+"
text = input()

result = re.findall(regex, text)
print(" ".join(result))
