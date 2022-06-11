def function(string, number):
    if string == "int":
        result = int(number) * 2
        return result
    elif string == "real":
        result = float(number) * 1.5
        return f"{result:.2f}"
    elif string == "string":
        result = "$" + number + "$"
        return result


string_input = input()
number = input()
print(function(string_input, number))