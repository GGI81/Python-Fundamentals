string = input().split()

my_dict = {}

for i in string:
    lower_words = i.lower()
    if lower_words not in my_dict:
        my_dict[lower_words] = 0
    my_dict[lower_words] += 1

for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=" ")