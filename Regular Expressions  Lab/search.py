import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
text = input()

result = re.search(pattern, text)

start_index = result.start()
end_index = result.end()
print(text[start_index: end_index])
# Returns Peter Smith
print(result.group())
# Returns Peter Smith

# USE FINDALL instead
