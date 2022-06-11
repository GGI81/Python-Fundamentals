def another_function():
    multiply_numbers(1, 2)
    print(multiply_numbers())
another_function()

def multiply_numbers(num1, num2):
    result = num1 * num2
    print(result)

a = multiply_numbers(5, 6)
print(a)
multiply_numbers(20, 30)