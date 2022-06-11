def odd_and_even_sum_of_digits(num: str):
    odd_sum = 0
    even_sum = 0
    for symbol in num:
        digit = int(symbol)
        if digit % 2 == 0:  #even
            even_sum += digit
        else:   #odd
            odd_sum += digit
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

number = input()

result = odd_and_even_sum_of_digits(number)
print(result)