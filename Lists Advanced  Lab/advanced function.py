# map()
nums = ["1", "2", "3", "4"]

print([int(i) for i in nums])  # new way
print(list(map(int, nums)))    # old way

nums = [1, 2, 3, 4, 5]
print([el for el in nums if el % 2 == 0])        # new way
print(list(filter(lambda x: x % 2 == 0, nums)))  # old way
