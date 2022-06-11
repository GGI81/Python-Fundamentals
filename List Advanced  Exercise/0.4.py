numbers = [int(i) for i in input().split(", ")]

positive_numbers = [str(i) for i in numbers if i >= 0]
negative_numbers = [str(i) for i in numbers if i < 0]
even_numbers = [str(i) for i in numbers if i % 2 == 0]
odd_numbers = [str(i) for i in numbers if i % 2 == 1]

print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")