import re

text = "The rain in Spain"
pattern = r"ain"

result = re.findall(pattern, text)
print(" ".join(result))