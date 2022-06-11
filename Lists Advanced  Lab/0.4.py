string = input().split()
searching_palindrome = input()
my_list = [el for el in string if el == el[::-1]]
print(my_list)
print(f"Found palindrome {my_list.count(searching_palindrome)} times")