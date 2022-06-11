def factorial_divider(n_1, n_2):
    sum_num_1 = n_1
    sum_num_2 = n_2

    for number_below_n_1 in range(1, n_1):
        sum_num_1 *=number_below_n_1

    for number_below_n_2 in range(1, n_2):
        sum_num_2 *= number_below_n_2

    answer = sum_num_1 // sum_num_2

    return answer


n_1_input = int(input())
n_2_input = int(input())

print(f"{factorial_divider(n_1_input, n_2_input):.2f}")