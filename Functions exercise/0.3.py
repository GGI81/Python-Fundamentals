def function(string1: str, string2: str):
    for i in range(ord(string1) + 1, ord(string2)):
        print(chr(i), end=" ")

string1_input = input()
string2_input = input()

function(string1_input, string2_input)
