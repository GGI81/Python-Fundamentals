n = int(input())
special_word = input()

list_with_all_words = []
list_with_special_words = []

for i in range(n):
    words = input()
    list_with_all_words.append(words)
    if special_word in words:
        list_with_special_words.append(words)
print(list_with_all_words)
print(list_with_special_words)