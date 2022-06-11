import re

pattern = r"(?P<link>(?P<subdomain>\www)\.(?P<domainname>[A-Za-z0-9\-]+)\.(?P<domainextension>[a-z]+[\.a-z]*))"
string = input()
my_list = []

while string != "":
    matches = re.finditer(pattern, string)
    for i in matches:
        my_list.append(i.group("link"))
    string = input()

for j in my_list:
    print("".join(j))