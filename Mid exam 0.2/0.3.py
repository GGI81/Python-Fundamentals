numbers_input = [int(i) for i in input().split()]

average_number = sum(numbers_input) // len(numbers_input)

my_list = []

for el in numbers_input:
    if el > average_number:
        my_list.append(el)
        my_list.sort(reverse=True)
                                               #reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
                                               # Reverse ги връща в нисходящ ред
                                               # syntax = sort.(reverse=True)

if len(my_list) == 0:
    print("No")
else:
    print(*my_list[:5])



