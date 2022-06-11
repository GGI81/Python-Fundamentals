def function(num1: int, num2: int, num3: int):
    result = num1 * num2 * num3
    if result < 0:
        print("negative")
    elif result == 0:
        print("zero")
    elif result > 0:
        print("positive")


num1_input = int(input())
num2_input = int(input())
num3_input = int(input())

function(num1_input, num2_input, num3_input)