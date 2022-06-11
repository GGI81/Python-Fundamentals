"""
a = [1, 2, 3, 4]
i = 0

while i < len(a):
    print(a[i])
    i += 1
"""

my_list = ["dog", "cat", "fish"]

while my_list:  # while there are elements in my list
    print(my_list[0], end=" ")  # prints the element on index 0 for every iteration
    current_element = my_list[0]
    my_list.remove(current_element)
print()
print()

a = [1, 2, 3, 4, 1]

while 1 in a:
    a.remove(1)
print(a)