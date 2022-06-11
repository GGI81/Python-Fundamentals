def calculate(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    elif num3 < num1 and num3 < num2:
        return num3

num1_input = int(input())
num2_input = int(input())
num3_input = int(input())

print(calculate(num1_input, num2_input, num3_input))