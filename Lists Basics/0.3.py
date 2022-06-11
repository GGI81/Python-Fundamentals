n = int(input())
p_numbers = []
n_numbers = []
p_numbers_count = 0
for i in range(1, n + 1):
    follow_numbers = int(input())
    if follow_numbers >= 0:
        p_numbers.append(follow_numbers)
        p_numbers_count += 1
    else:
        n_numbers.append(follow_numbers)
print(p_numbers)
print(n_numbers)
print(f"Count of positives: {p_numbers_count}. Sum of negatives: {sum(n_numbers)}")
# sum function !!!       or !!!len(p_numbers)!!!
