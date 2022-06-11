"""
nums = [-2, 50, 10, 0]

result = []

for el in nums:
    if el > 0:
        result.append(el**2)
print(result)
"""

nums = [-2, 50, 10, 0]
print([el**2 for el in nums if el > 0])