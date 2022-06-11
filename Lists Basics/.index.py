"""
a = ["dog", "cat"]

print(a.index("dog"))
                    it will return 0
"""
a = ["dog", "cat"]

index_of_element = a.index("dog")

for i in range(len(a[index_of_element])):
    if "o" == a[index_of_element][i]:
        print(i)