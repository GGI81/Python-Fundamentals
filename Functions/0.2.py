def calculate(type_operator, num1, num2):
    if type_operator == "multiply":
        return num1 * num2
    elif type_operator == "divide":
        return  num1 // num2
    elif type_operator == "add":
        return num1 + num2
    elif type_operator == "subtract":
        return num1 - num2

operator = input()
number1 = int(input())
number2 = int(input())

print(calculate(operator, number1, number2))