import re

text = "The rain in Spain"
pattern = r"ain"
print(re.findall(pattern, text))
# Returns list
