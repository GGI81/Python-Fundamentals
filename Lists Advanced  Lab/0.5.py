input_numbers = [int(el) for el in input().split(", ")]

print([index for index in range(len(input_numbers)) if input_numbers[index] % 2 == 0])

"""
nums = [int(el) for el in input().split(", ")]
result = []
for index in range(len(nums))
    if nums[index] % 2 == 0"
    result.append(index)
print(result)
"""