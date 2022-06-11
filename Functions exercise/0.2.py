def sum_numbers(num1, num2,):
    total = num1 + num2
    return total


def subtract(sum1, num3):
    total = sum1 - num3
    return total


def add_and_subtract(num1, num2, num3):
    sum1 = sum_numbers(num1, num2)
    result = subtract(sum1, num3)
    return result

num1_input = int(input())
num2_input = int(input())
num3_input = int(input())

print(add_and_subtract(num1_input, num2_input, num3_input))