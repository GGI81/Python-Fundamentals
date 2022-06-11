"""
coins = [int(num) for num in input().split(", ")]
beggars = int(input())
count_beggars = 0
beggars_list = [0] * beggars
for coin in coins:
    beggars_list[count_beggars] += coin
    count_beggars += 1
    if count_beggars >= beggars:
        count_beggars = 0
print(beggars_list)
"""

# Прочитаме от конзолата сумите, които ще раздадем
list_of_numbers_as_string = input().split(", ")
# Прочитаме от конзолата броя просяци
number_of_beggars = int(input())
sums_of_each_beggar = []
start_index = 0
# Цикъл с итерации, колкото са броя просяци
for beggar in range(1, number_of_beggars + 1):
    current_sum = 0
    # Вложен цикъл, който разпределя сума за текущия просяк
    for sum in range(start_index, len(list_of_numbers_as_string), number_of_beggars):
        # Прибавяме сумите за текущия просяк
        current_sum += int(list_of_numbers_as_string[sum])
    sums_of_each_beggar.append(current_sum)
    start_index += 1
print(sums_of_each_beggar)