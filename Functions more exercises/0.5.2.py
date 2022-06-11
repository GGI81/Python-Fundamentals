# WITHOUT MULTIPLYING THE 3 NUMBERS.

def function(num1: int, num2: int, num3: int):
    if num1 < 0 or num2 < 0 or num3 < 0:
        print(f"negative")
    elif num1 == 0 or num2 == 0 or num3 == 0:
        print("zero")
    elif num1 > 0 and num2 > 0 and num3 > 0:
        print("positive")

num1_input = int(input())
num2_input = int(input())
num3_input = int(input())

function(num1_input, num2_input, num3_input)